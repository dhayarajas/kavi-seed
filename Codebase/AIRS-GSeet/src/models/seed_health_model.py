"""
Seed Health Index (SHI) prediction model with multi-modal fusion.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class SeedHealthModel(nn.Module):
    """Multi-modal model for Seed Health Index prediction."""
    
    def __init__(self, hyperspectral_dim=2151, uav_feat_dim=128, env_feat_dim=10, hidden_dim=256):
        super(SeedHealthModel, self).__init__()
        
        # Hyperspectral encoder (1D CNN)
        self.hyperspectral_encoder = nn.Sequential(
            nn.Conv1d(1, 64, kernel_size=7, stride=2, padding=3),
            nn.ReLU(),
            nn.Conv1d(64, 128, kernel_size=5, stride=2, padding=2),
            nn.ReLU(),
            nn.Conv1d(128, 256, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1),
            nn.Flatten()
        )
        
        # UAV feature encoder (MLP)
        self.uav_encoder = nn.Sequential(
            nn.Linear(uav_feat_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 64)
        )
        
        # Environment feature encoder (MLP)
        self.env_encoder = nn.Sequential(
            nn.Linear(env_feat_dim, 64),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(64, 32)
        )
        
        # Attention-based fusion
        self.attention = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=8,
            batch_first=True
        )
        
        # Fusion layers
        self.fusion = nn.Sequential(
            nn.Linear(256 + 64 + 32, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_dim // 2, 1)  # SHI output (0-100)
        )
        
    def forward(self, hyperspectral, uav_features, env_features):
        # Encode each modality
        h_feat = self.hyperspectral_encoder(hyperspectral.unsqueeze(1))  # [B, 256]
        u_feat = self.uav_encoder(uav_features)  # [B, 64]
        e_feat = self.env_encoder(env_features)  # [B, 32]
        
        # Concatenate features
        combined = torch.cat([h_feat, u_feat, e_feat], dim=1)  # [B, 352]
        
        # Fusion and prediction
        shi = self.fusion(combined)  # [B, 1]
        shi = torch.sigmoid(shi) * 100  # Scale to 0-100
        
        return shi.squeeze(1)


class AflatoxinRiskModel(nn.Module):
    """Aflatoxin Risk Score (ARS) prediction model."""
    
    def __init__(self, hyperspectral_dim=2151, field_feat_dim=50, storage_feat_dim=4, hidden_dim=256):
        super(AflatoxinRiskModel, self).__init__()
        
        # Hyperspectral branch
        self.hyperspectral_branch = nn.Sequential(
            nn.Conv1d(1, 64, kernel_size=7, stride=2, padding=3),
            nn.ReLU(),
            nn.Conv1d(64, 128, kernel_size=5, stride=2, padding=2),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1),
            nn.Flatten(),
            nn.Linear(128, 64)
        )
        
        # Field conditions branch
        self.field_branch = nn.Sequential(
            nn.Linear(field_feat_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(128, 64)
        )
        
        # Storage conditions branch
        self.storage_branch = nn.Sequential(
            nn.Linear(storage_feat_dim, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, 32)
        )
        
        # Ensemble fusion
        self.fusion = nn.Sequential(
            nn.Linear(64 + 64 + 32, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_dim // 2, 1)  # ARS output (0-100)
        )
        
    def forward(self, hyperspectral, field_features, storage_features):
        # Encode each branch
        h_feat = self.hyperspectral_branch(hyperspectral.unsqueeze(1))  # [B, 64]
        f_feat = self.field_branch(field_features)  # [B, 64]
        s_feat = self.storage_branch(storage_features)  # [B, 32]
        
        # Concatenate and fuse
        combined = torch.cat([h_feat, f_feat, s_feat], dim=1)  # [B, 160]
        ars = self.fusion(combined)  # [B, 1]
        ars = torch.sigmoid(ars) * 100  # Scale to 0-100
        
        return ars.squeeze(1)


def train_seed_models(shi_model, ars_model, train_loader, val_loader, epochs=100, device='cpu'):
    """Train SHI and ARS models."""
    shi_criterion = nn.MSELoss()
    ars_criterion = nn.MSELoss()
    
    shi_optimizer = torch.optim.Adam(shi_model.parameters(), lr=1e-3, weight_decay=1e-5)
    ars_optimizer = torch.optim.Adam(ars_model.parameters(), lr=1e-3, weight_decay=1e-5)
    
    shi_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(shi_optimizer, mode='min', factor=0.5, patience=10)
    ars_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(ars_optimizer, mode='min', factor=0.5, patience=10)
    
    best_shi_r2 = 0.0
    best_ars_r2 = 0.0
    
    for epoch in range(epochs):
        # Training
        shi_model.train()
        ars_model.train()
        
        shi_train_loss = 0.0
        ars_train_loss = 0.0
        
        for batch in train_loader:
            # SHI training
            h_spec, uav_feat, env_feat, shi_target = batch['hyperspectral'], batch['uav'], batch['env'], batch['shi']
            h_spec = h_spec.to(device)
            uav_feat = uav_feat.to(device)
            env_feat = env_feat.to(device)
            shi_target = shi_target.to(device)
            
            shi_optimizer.zero_grad()
            shi_pred = shi_model(h_spec, uav_feat, env_feat)
            shi_loss = shi_criterion(shi_pred, shi_target)
            shi_loss.backward()
            shi_optimizer.step()
            shi_train_loss += shi_loss.item()
            
            # ARS training
            field_feat = batch['field'].to(device)
            storage_feat = batch['storage'].to(device)
            ars_target = batch['ars'].to(device)
            
            ars_optimizer.zero_grad()
            ars_pred = ars_model(h_spec, field_feat, storage_feat)
            ars_loss = ars_criterion(ars_pred, ars_target)
            ars_loss.backward()
            ars_optimizer.step()
            ars_train_loss += ars_loss.item()
        
        shi_train_loss /= len(train_loader)
        ars_train_loss /= len(train_loader)
        
        # Validation
        shi_model.eval()
        ars_model.eval()
        
        shi_val_preds = []
        shi_val_targets = []
        ars_val_preds = []
        ars_val_targets = []
        
        with torch.no_grad():
            for batch in val_loader:
                h_spec = batch['hyperspectral'].to(device)
                uav_feat = batch['uav'].to(device)
                env_feat = batch['env'].to(device)
                field_feat = batch['field'].to(device)
                storage_feat = batch['storage'].to(device)
                
                shi_pred = shi_model(h_spec, uav_feat, env_feat)
                ars_pred = ars_model(h_spec, field_feat, storage_feat)
                
                shi_val_preds.append(shi_pred.cpu())
                shi_val_targets.append(batch['shi'])
                ars_val_preds.append(ars_pred.cpu())
                ars_val_targets.append(batch['ars'])
        
        # Calculate R²
        from sklearn.metrics import r2_score
        
        shi_pred_all = torch.cat(shi_val_preds).numpy()
        shi_target_all = torch.cat(shi_val_targets).numpy()
        shi_r2 = r2_score(shi_target_all, shi_pred_all)
        
        ars_pred_all = torch.cat(ars_val_preds).numpy()
        ars_target_all = torch.cat(ars_val_targets).numpy()
        ars_r2 = r2_score(ars_target_all, ars_pred_all)
        
        shi_scheduler.step(shi_train_loss)
        ars_scheduler.step(ars_train_loss)
        
        if shi_r2 > best_shi_r2:
            best_shi_r2 = shi_r2
            torch.save(shi_model.state_dict(), 'best_shi_model.pth')
        
        if ars_r2 > best_ars_r2:
            best_ars_r2 = ars_r2
            torch.save(ars_model.state_dict(), 'best_ars_model.pth')
        
        if (epoch + 1) % 20 == 0:
            print(f'Epoch {epoch+1}/{epochs}')
            print(f'  SHI - Train Loss: {shi_train_loss:.4f}, Val R²: {shi_r2:.4f}')
            print(f'  ARS - Train Loss: {ars_train_loss:.4f}, Val R²: {ars_r2:.4f}')
    
    return best_shi_r2, best_ars_r2
