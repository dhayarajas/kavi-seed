"""
Canopy stress detection model: CNN-ViT hybrid architecture.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models


class CNNViTHybrid(nn.Module):
    """Hybrid CNN-ViT model for canopy stress detection."""
    
    def __init__(self, num_classes=4, img_size=256, patch_size=16, embed_dim=768, num_heads=12, num_layers=6):
        super(CNNViTHybrid, self).__init__()
        
        # CNN backbone (ResNet-50)
        resnet = models.resnet50(pretrained=True)
        self.cnn_backbone = nn.Sequential(*list(resnet.children())[:-2])
        cnn_feat_dim = 2048
        
        # Reduce CNN features
        self.cnn_proj = nn.Conv2d(cnn_feat_dim, embed_dim, kernel_size=1)
        
        # ViT components
        self.patch_size = patch_size
        self.num_patches = (img_size // patch_size) ** 2
        self.embed_dim = embed_dim
        
        # Patch embedding
        self.patch_embed = nn.Conv2d(3, embed_dim, kernel_size=patch_size, stride=patch_size)
        
        # Positional embedding
        self.pos_embed = nn.Parameter(torch.randn(1, self.num_patches, embed_dim))
        
        # Transformer encoder
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=num_heads,
            dim_feedforward=embed_dim * 4,
            dropout=0.1,
            batch_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(embed_dim * 2, embed_dim),  # CNN + ViT features
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(embed_dim, num_classes)
        )
        
    def forward(self, x):
        # CNN features
        cnn_feat = self.cnn_backbone(x)  # [B, 2048, H', W']
        cnn_feat = self.cnn_proj(cnn_feat)  # [B, embed_dim, H', W']
        cnn_feat = F.adaptive_avg_pool2d(cnn_feat, (1, 1)).flatten(1)  # [B, embed_dim]
        
        # ViT features
        # Patch embedding
        patches = self.patch_embed(x)  # [B, embed_dim, H/p, W/p]
        B, C, H, W = patches.shape
        patches = patches.flatten(2).transpose(1, 2)  # [B, num_patches, embed_dim]
        
        # Add positional embedding
        patches = patches + self.pos_embed
        
        # Transformer
        vit_feat = self.transformer(patches)  # [B, num_patches, embed_dim]
        vit_feat = vit_feat.mean(dim=1)  # [B, embed_dim]
        
        # Concatenate CNN and ViT features
        combined = torch.cat([cnn_feat, vit_feat], dim=1)  # [B, embed_dim * 2]
        
        # Classification
        logits = self.classifier(combined)
        
        return logits


def train_canopy_model(model, train_loader, val_loader, epochs=50, device='cpu'):
    """Train the canopy stress detection model."""
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4, weight_decay=1e-5)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=5)
    
    best_val_acc = 0.0
    train_losses = []
    val_accs = []
    
    for epoch in range(epochs):
        # Training
        model.train()
        train_loss = 0.0
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
        
        train_loss /= len(train_loader)
        train_losses.append(train_loss)
        
        # Validation
        model.eval()
        val_correct = 0
        val_total = 0
        with torch.no_grad():
            for data, target in val_loader:
                data, target = data.to(device), target.to(device)
                output = model(data)
                _, predicted = torch.max(output.data, 1)
                val_total += target.size(0)
                val_correct += (predicted == target).sum().item()
        
        val_acc = val_correct / val_total
        val_accs.append(val_acc)
        
        scheduler.step(train_loss)
        
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_canopy_model.pth')
        
        if (epoch + 1) % 10 == 0:
            print(f'Epoch {epoch+1}/{epochs}, Train Loss: {train_loss:.4f}, Val Acc: {val_acc:.4f}')
    
    return train_losses, val_accs, best_val_acc
