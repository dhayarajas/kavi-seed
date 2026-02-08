# AIRS-GSeed: An AI-Driven Framework for Groundnut Seed Health Assessment and Aflatoxin Risk Prediction

## Abstract

This document presents AIRS-GSeed (AI-driven Remote Sensing for Groundnut Seed Health), a novel multi-modal AI framework that addresses critical gaps in groundnut crop monitoring by integrating UAV-based remote sensing, spectral analysis, and IoT sensor data to infer underground pod-zone stress, detect pre-symptomatic seed health degradation, and predict aflatoxin contamination risk. The framework bridges field monitoring, harvest timing, and storage management through explainable AI models, enabling actionable interventions for farmers, seed producers, and food safety regulators.

---

## 1. Scope of the Proposed System

### 1.1 Problem Boundaries

AIRS-GSeed addresses the following problem domain:

**Included:**
- Pre-harvest field monitoring (vegetative to maturity stages)
- Underground pod-zone stress inference from above-ground proxies
- Early disease detection (leaf spot, rust, Aspergillus infection)
- Seed health assessment at harvest
- Post-harvest storage monitoring and risk prediction
- Aflatoxin contamination risk modeling
- Multi-scale deployment (smallholder to commercial farms)

**Excluded:**
- Real-time in-field pod excavation and direct pod imaging
- Post-processing quality control (shelling, grading automation)
- Market price prediction or supply chain optimization
- Genetic modification or breeding recommendations
- Pesticide application scheduling (though stress detection informs timing)

### 1.2 Target Users

**Primary Users:**
1. **Smallholder Farmers (0.5–5 hectares)**
   - Need: Cost-effective early warning, harvest timing guidance
   - Access: Mobile app with simplified alerts, SMS notifications

2. **Commercial Farmers & FPOs (5–100+ hectares)**
   - Need: Field-scale stress mapping, batch seed quality assessment
   - Access: Web dashboard, API integration, bulk analysis

3. **Seed Producers & Processors**
   - Need: Seed health certification, aflatoxin compliance monitoring
   - Access: Laboratory-grade spectral analysis, batch reporting

4. **Food Safety Regulators & Certification Bodies**
   - Need: Traceability, risk assessment, compliance verification
   - Access: Audit logs, explainability reports, risk dashboards

**Secondary Users:**
- Agricultural extension services
- Research institutions
- Insurance providers (risk assessment)

### 1.3 Operational Stages

**Stage 1: Field Monitoring (30–120 DAS)**
- Weekly/bi-weekly UAV flights
- Continuous soil sensor data collection
- Weather data integration
- Canopy stress detection and pod-zone inference

**Stage 2: Pre-Harvest Assessment (90–120 DAS)**
- Intensive spectral sampling of flagged areas
- Seed Health Index (SHI) prediction
- Aflatoxin Risk Score (ARS) generation
- Harvest window recommendation

**Stage 3: Harvest & Immediate Post-Harvest (120–150 DAS)**
- Seed sample collection and hyperspectral analysis
- Validation of pre-harvest predictions
- Initial seed grading recommendations

**Stage 4: Storage Monitoring (Post-harvest)**
- Continuous IoT sensor monitoring (temperature, RH, CO₂, VOC)
- Storage risk alerts
- Intervention recommendations
- Periodic seed re-assessment

### 1.4 Assumptions and Constraints

**Assumptions:**
1. Groundnut cultivars are primarily Spanish or Virginia types with known pod depth ranges (5–15 cm)
2. Field access permits UAV operations (regulatory compliance assumed)
3. Storage facilities have basic IoT sensor deployment capability
4. Weather data (IMD/NASA POWER) is accessible with reasonable accuracy
5. Laboratory facilities exist for ground truth aflatoxin measurement (B1, B2, G1, G2)
6. Farmers can provide basic agronomic metadata (cultivar, planting date, irrigation)

**Constraints:**
1. **Technical:**
   - UAV flight restrictions (weather, regulatory)
   - Hyperspectral data collection is time-intensive (targeted sampling required)
   - Limited real-time processing capability in field conditions
   - Sensor calibration drift over time

2. **Economic:**
   - Cost per hectare must remain <$50 for smallholder adoption
   - Hyperspectral equipment cost limits widespread deployment
   - Storage IoT sensors must be low-cost (<$100 per unit)

3. **Data:**
   - Ground truth aflatoxin measurement is expensive and time-delayed
   - Historical multi-season data may be limited
   - Label noise in field disease scoring

4. **Biological:**
   - Aflatoxin production is stochastic (environmental triggers)
   - Disease progression varies by cultivar and microclimate
   - Pod-zone conditions are heterogeneous within fields

### 1.5 Deployment Scenarios

**Scenario A: Smallholder Farm (0.5–2 ha)**
- Deployment: Community UAV service, shared IoT sensors
- Frequency: Bi-weekly flights, weekly soil sensor readings
- Output: SMS alerts, mobile app dashboard
- Cost model: Pay-per-service or subscription ($20–30/season)

**Scenario B: Medium-Scale Farm (5–20 ha)**
- Deployment: Owned UAV, field IoT network, targeted hyperspectral sampling
- Frequency: Weekly flights, continuous soil monitoring
- Output: Field maps, harvest timing recommendations, storage alerts
- Cost model: Equipment lease + service ($200–500/season)

**Scenario C: Large Commercial Farm / FPO (50–200+ ha)**
- Deployment: Fleet UAV operations, comprehensive sensor network, laboratory-grade spectral analysis
- Frequency: Multi-flight per week, real-time monitoring
- Output: Precision agriculture dashboard, batch seed certification, API integration
- Cost model: Enterprise license + equipment ($2000–5000/season)

---

## 2. System Architecture

### 2.1 Overview

AIRS-GSeed employs a four-layer architecture:

1. **Sensing Layer**: Multi-modal data acquisition
2. **Data Processing & Fusion Layer**: Preprocessing, feature extraction, multi-modal fusion
3. **AI & Intelligence Layer**: Deep learning models for inference and prediction
4. **Explainability & Decision Layer**: Interpretability, uncertainty quantification, actionable outputs

```
┌─────────────────────────────────────────────────────────────┐
│         Explainability & Decision Layer                      │
│  (SHAP, Attention Maps, Uncertainty, Decision Rules)        │
└─────────────────────────────────────────────────────────────┘
                            ↑
┌─────────────────────────────────────────────────────────────┐
│              AI & Intelligence Layer                         │
│  (CNN/ViT, Physics-Informed ML, Transformers, SHI/ARS)      │
└─────────────────────────────────────────────────────────────┘
                            ↑
┌─────────────────────────────────────────────────────────────┐
│         Data Processing & Fusion Layer                       │
│  (Normalization, Feature Extraction, Multi-modal Fusion)     │
└─────────────────────────────────────────────────────────────┘
                            ↑
┌─────────────────────────────────────────────────────────────┐
│                  Sensing Layer                               │
│  (UAV RGB/MS/Thermal, Soil Sensors, Hyperspectral, IoT)     │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Sensing Layer

#### 2.2.1 UAV RGB Imaging

**Specifications:**
- **Resolution**: 4K (3840×2160) minimum, 20 MP preferred
- **Spatial Resolution**: 1–3 cm GSD (Ground Sample Distance) at 50–100 m altitude
- **Temporal Resolution**: Weekly during critical stages (60–120 DAS), bi-weekly otherwise
- **Coverage**: Full field coverage with 70–80% overlap for orthomosaic generation
- **Acquisition**: Automated flight planning, triggered by growth stage calendar or stress alerts

**Data Type**: Geotagged RGB images, orthomosaics, point clouds (optional)

**Use Cases**: Canopy structure, leaf area estimation, visual disease symptoms, growth stage classification

#### 2.2.2 UAV Multispectral Imaging

**Specifications:**
- **Bands**: RGB, Red-edge (730 nm), NIR (850 nm), optional additional bands (550 nm, 670 nm)
- **Spatial Resolution**: 5–10 cm GSD
- **Temporal Resolution**: Weekly during critical stages
- **Sensor**: Commercial multispectral cameras (e.g., MicaSense RedEdge-MX, Parrot Sequoia+)

**Data Type**: Geotagged multispectral images, calibrated reflectance

**Use Cases**: Vegetation indices (NDVI, NDRE, GNDVI), chlorophyll content, early stress detection

#### 2.2.3 UAV Thermal Imaging

**Specifications:**
- **Resolution**: 640×512 or higher
- **Spatial Resolution**: 10–20 cm GSD
- **Temporal Resolution**: Bi-weekly, more frequent during drought stress periods
- **Temperature Range**: -10°C to 150°C, accuracy ±2°C
- **Sensor**: FLIR thermal cameras (e.g., FLIR Vue Pro)

**Data Type**: Geotagged thermal images, temperature maps

**Use Cases**: Canopy temperature stress, water stress detection, disease hotspots

#### 2.2.4 Soil & Pod-Zone Proxy Sensors

**Specifications:**
- **Soil Moisture**: Capacitive sensors, 0–100% VWC, accuracy ±3%
- **Soil Temperature**: -40°C to 85°C, accuracy ±0.5°C
- **Soil EC (Electrical Conductivity)**: 0–23 dS/m
- **Deployment**: 5–10 cm depth (pod zone), 1–2 sensors per hectare
- **Temporal Resolution**: Continuous logging (15-minute intervals)
- **Communication**: LoRaWAN or cellular IoT

**Data Type**: Time series of soil parameters, geotagged sensor locations

**Use Cases**: Pod-zone stress inference, irrigation scheduling, disease risk modeling

#### 2.2.5 Hyperspectral / NIR Spectroscopy

**Specifications:**
- **Spectral Range**: 400–2500 nm (VNIR-SWIR)
- **Spectral Resolution**: 3–10 nm
- **Spatial Resolution**: Point measurements (seed samples) or imaging (pod samples)
- **Temporal Resolution**: Triggered by UAV stress alerts or harvest sampling
- **Equipment**: Portable hyperspectral spectrometers (e.g., ASD FieldSpec, Ocean Insight)

**Data Type**: Reflectance spectra (seed, pod, leaf samples)

**Use Cases**: Seed health classification, fungal detection, aflatoxin prediction, quality grading

#### 2.2.6 Storage IoT Sensors

**Specifications:**
- **Temperature**: -20°C to 60°C, accuracy ±0.5°C
- **Relative Humidity (RH)**: 0–100%, accuracy ±2%
- **CO₂**: 0–5000 ppm, accuracy ±50 ppm
- **VOC (Volatile Organic Compounds)**: Qualitative detection (fungal activity indicator)
- **Deployment**: 1 sensor per storage unit (silo, warehouse section)
- **Temporal Resolution**: Continuous (5-minute intervals)
- **Communication**: LoRaWAN, Wi-Fi, or cellular

**Data Type**: Time series of environmental parameters

**Use Cases**: Storage risk assessment, spoilage prediction, intervention alerts

#### 2.2.7 Weather & Climate Data

**Specifications:**
- **Sources**: India Meteorological Department (IMD), NASA POWER, local weather stations
- **Parameters**: Temperature, precipitation, humidity, solar radiation, wind speed
- **Spatial Resolution**: Grid-based (0.25°–1°), interpolated to field coordinates
- **Temporal Resolution**: Daily aggregates, hourly when available

**Data Type**: Time series of weather variables

**Use Cases**: Disease risk modeling, aflatoxin prediction, irrigation needs

### 2.3 Data Processing & Fusion Layer

#### 2.3.1 Image Normalization

**Illumination Correction:**
- Empirical Line Method (ELM) using calibration targets
- Histogram matching across flight dates
- Shadow detection and masking

**Geometric Correction:**
- Structure-from-Motion (SfM) for orthomosaic generation
- Ground control points (GCPs) for georeferencing
- DEM generation for terrain correction

#### 2.3.2 Spectral Preprocessing

**Baseline Correction:**
- Savitzky-Golay smoothing
- Multiplicative Scatter Correction (MSC)
- Standard Normal Variate (SNV) transformation

**Dimensionality Reduction:**
- Principal Component Analysis (PCA) for hyperspectral data
- Band selection algorithms (e.g., Sequential Forward Selection)
- Vegetation index computation (NDVI, NDRE, PRI, etc.)

#### 2.3.3 Feature Extraction

**Vegetation Indices:**
- NDVI, NDRE, GNDVI, EVI, PRI, CWSI (Crop Water Stress Index)
- Red-edge position, chlorophyll indices

**Texture Features:**
- Gray-Level Co-occurrence Matrix (GLCM) features
- Local Binary Patterns (LBP)
- Gabor filters

**Spectral Biomarkers:**
- Absorption features (chlorophyll, carotenoids, water)
- Derivative spectra (first, second derivatives)
- Continuum removal for specific absorption features

**Temporal Features:**
- Time-series statistics (mean, variance, trend)
- Phenological metrics (green-up, peak, senescence)
- Change detection metrics

#### 2.3.4 Multi-Modal Data Fusion Strategy

**Early Fusion:**
- Concatenation of features from different modalities
- Used for: Canopy stress detection (RGB + multispectral + thermal)

**Late Fusion:**
- Separate model predictions combined at decision level
- Used for: SHI prediction (UAV features + soil features + weather)

**Attention-Based Fusion:**
- Cross-modal attention mechanisms
- Used for: Pod-zone stress inference (canopy features attend to soil features)

**Hierarchical Fusion:**
- Field-level → plot-level → pixel-level aggregation
- Used for: Field-scale risk assessment

### 2.4 AI & Intelligence Layer

#### 2.4.1 Canopy Stress Detection Model

**Architecture:**
- **Hybrid CNN-ViT (Vision Transformer)**
  - CNN backbone (ResNet-50 or EfficientNet) for local feature extraction
  - ViT encoder for global context and long-range dependencies
  - Multi-scale feature pyramid for disease lesion detection

**Input:**
- RGB + multispectral + thermal orthomosaics (patches: 256×256 or 512×512)
- Temporal stack (current + previous 2–3 flights)

**Output:**
- Stress probability map (0–1)
- Disease class probabilities (healthy, leaf spot, rust, unknown stress)
- Confidence scores

**Training:**
- Supervised learning with field-annotated disease maps
- Data augmentation (rotation, flip, color jitter, mixup)
- Transfer learning from ImageNet and agricultural datasets

#### 2.4.2 Pod-Zone Stress Inference Model

**Architecture:**
- **Physics-Informed Neural Network (PINN)**
  - Incorporates soil physics constraints (water movement, heat transfer)
  - Multi-input network: canopy features + soil sensor data + weather

**Input:**
- Canopy stress features (from CNN-ViT)
- Soil moisture, temperature, EC time series
- Weather history (temperature, precipitation)
- Agronomic metadata (cultivar, pod depth estimate)

**Output:**
- Pod-zone stress index (0–1)
- Estimated pod moisture content
- Pod temperature proxy

**Physics Constraints:**
- Soil moisture diffusion equations
- Heat transfer relationships
- Pod depth-dependent attenuation factors

**Training:**
- Semi-supervised learning (limited pod excavation ground truth)
- Physics loss terms in objective function
- Transfer learning from soil physics simulations

#### 2.4.3 Temporal Disease Progression Model

**Architecture:**
- **Transformer + LSTM Hybrid**
  - Transformer encoder for spatial-temporal attention
  - LSTM decoder for sequential prediction
  - Multi-head attention across time steps

**Input:**
- Time series of canopy stress maps
- Weather time series
- Soil sensor time series

**Output:**
- Future stress probability (1–4 weeks ahead)
- Disease progression trajectory
- Risk escalation alerts

**Training:**
- Sequence-to-sequence learning
- Teacher forcing during training
- Curriculum learning (short-term → long-term prediction)

#### 2.4.4 Seed Health Index (SHI) Prediction Model

**Architecture:**
- **Multi-Modal Deep Learning Network**
  - Branch 1: Hyperspectral encoder (1D CNN or Transformer)
  - Branch 2: UAV feature encoder (from canopy stress model)
  - Branch 3: Soil/weather feature encoder (MLP)
  - Fusion layer with attention mechanism

**Input:**
- Seed hyperspectral spectrum (400–2500 nm, 2151 bands)
- UAV-derived features (canopy stress, vegetation indices)
- Soil/weather features (pre-harvest conditions)
- Agronomic metadata

**Output:**
- Seed Health Index (SHI): 0–100
  - 80–100: Excellent (high germination, low infection risk)
  - 60–79: Good (acceptable quality)
  - 40–59: Moderate (reduced germination, elevated risk)
  - 0–39: Poor (low germination, high infection risk)

**Training:**
- Supervised learning with ground truth:
  - Germination rate (%)
  - Fungal presence (binary)
  - Visual quality score
- Multi-task learning (germination + infection + quality)

#### 2.4.5 Aflatoxin Risk Score (ARS) Prediction Model

**Architecture:**
- **Ensemble Model**
  - Model 1: Hyperspectral regression (1D CNN → MLP)
  - Model 2: Multi-modal fusion (UAV + soil + weather)
  - Model 3: Temporal risk model (storage conditions)
  - Weighted ensemble with uncertainty-aware weighting

**Input:**
- Seed hyperspectral spectrum (if available)
- Pre-harvest field conditions (UAV stress, soil, weather)
- Post-harvest storage conditions (temperature, RH, CO₂, VOC)
- Time since harvest

**Output:**
- Aflatoxin Risk Score (ARS): 0–100
  - 0–20: Low risk (<10 ppb expected)
  - 21–40: Moderate risk (10–20 ppb)
  - 41–60: High risk (20–50 ppb)
  - 61–80: Very high risk (50–100 ppb)
  - 81–100: Critical risk (>100 ppb, regulatory limit)

**Training:**
- Supervised learning with laboratory-measured aflatoxin (B1, B2, G1, G2)
- Imbalanced dataset handling (SMOTE, focal loss)
- Transfer learning from related crop datasets

#### 2.4.6 Uncertainty Handling

**Methods:**
- **Monte Carlo Dropout**: Bayesian approximation for uncertainty
- **Ensemble Methods**: Multiple model predictions for variance estimation
- **Conformal Prediction**: Prediction intervals with coverage guarantees

**Output:**
- Prediction confidence intervals
- Epistemic uncertainty (model uncertainty)
- Aleatoric uncertainty (data noise)

#### 2.4.7 Cost Optimization Mechanisms

**Adaptive Sampling:**
- UAV flights triggered by risk thresholds
- Hyperspectral sampling only for high-risk areas
- Sensor data downsampling during low-risk periods

**Model Compression:**
- Knowledge distillation (teacher → student models)
- Quantization (FP32 → INT8)
- Pruning for edge deployment

**Federated Learning (Optional):**
- Distributed training across farms
- Privacy-preserving model updates
- Reduced data transfer costs

### 2.5 Explainability & Decision Layer

#### 2.5.1 Explainable AI Methods

**SHAP (SHapley Additive exPlanations):**
- Feature importance for SHI and ARS predictions
- Local explanations for individual seed samples
- Global feature importance across dataset

**Attention Maps:**
- Visual attention from ViT models
- Spatial attention for disease localization
- Temporal attention for progression analysis

**Spectral Attribution:**
- Wavelength importance for hyperspectral predictions
- Identification of spectral biomarkers
- Interpretation of absorption features

**Gradient-Based Methods:**
- Grad-CAM for CNN visualizations
- Integrated gradients for feature attribution

#### 2.5.2 Confidence & Uncertainty Estimation

**Outputs:**
- Prediction confidence scores (0–1)
- Uncertainty intervals (e.g., 95% confidence)
- Risk flags when uncertainty exceeds thresholds

**Visualization:**
- Uncertainty heatmaps overlaid on field maps
- Confidence bands in time-series predictions
- Risk stratification (high confidence vs. uncertain predictions)

#### 2.5.3 Decision Rules

**Harvest Timing:**
```
IF ARS < 30 AND SHI > 70 AND days_since_flowering > 90:
    RECOMMEND: Harvest within 7 days
ELSE IF ARS < 50 AND SHI > 60:
    RECOMMEND: Harvest within 14 days (monitor closely)
ELSE:
    RECOMMEND: Delay harvest, apply interventions, re-assess
```

**Seed Grading:**
```
IF SHI >= 80 AND ARS < 20:
    GRADE: Premium (certified seed quality)
ELSE IF SHI >= 60 AND ARS < 40:
    GRADE: Standard (commercial use)
ELSE IF SHI >= 40:
    GRADE: Feed grade (not for human consumption)
ELSE:
    GRADE: Reject (disposal recommended)
```

**Storage Intervention:**
```
IF storage_temperature > 25°C AND RH > 70% AND ARS > 40:
    ALERT: Critical risk - immediate aeration/cooling required
ELSE IF CO₂ > 1000 ppm OR VOC_detected:
    ALERT: Fungal activity detected - inspect and treat
ELSE IF ARS_trend_increasing:
    ALERT: Risk escalating - schedule re-assessment
```

---

## 3. Dataset Description

### 3.1 Dataset Concept

AIRS-GSeed employs a composite, multi-modal, groundnut-specific dataset that spans field monitoring, harvest assessment, and storage phases. **No single public dataset exists that comprehensively addresses groundnut pod-zone stress, seed health, and aflatoxin risk prediction.** Therefore, this dataset is purpose-built by combining:

1. **Newly collected groundnut field data** (primary dataset)
2. **Public agricultural datasets** for representation learning and transfer learning
3. **Synthetic data augmentation** using physics-informed simulations

The dataset is designed to support:
- Pre-symptomatic disease detection
- Pod-zone stress inference
- Seed health classification
- Aflatoxin risk prediction
- Temporal disease progression modeling

### 3.2 Field UAV Dataset

#### 3.2.1 Data Collection

**Acquisition Parameters:**
- **Locations**: 3–5 groundnut-growing regions in semi-arid India (Gujarat, Andhra Pradesh, Tamil Nadu)
- **Seasons**: ≥2 cropping seasons (Kharif and Rabi)
- **Fields**: 20–30 fields per season, varying sizes (0.5–20 ha)
- **Flight Frequency**: Weekly during critical stages (60–120 DAS), bi-weekly otherwise
- **Total Flights**: 200–300 flights across seasons

**Sensors:**
- RGB: 4K/20 MP cameras
- Multispectral: 5-band (RGB, Red-edge, NIR)
- Thermal: FLIR or equivalent

**Spatial Coverage:**
- Full field orthomosaics
- Overlap: 70–80% for SfM processing
- GSD: 1–3 cm (RGB), 5–10 cm (multispectral), 10–20 cm (thermal)

#### 3.2.2 Labels

**Canopy Stress Levels:**
- 0: Healthy (no visible stress)
- 1: Mild stress (slight discoloration, <10% affected area)
- 2: Moderate stress (visible symptoms, 10–30% affected)
- 3: Severe stress (>30% affected, advanced disease)

**Disease Presence:**
- Binary labels: Leaf spot (Cercospora), Rust (Puccinia), Unknown stress
- Annotated polygons for disease lesions
- Growth stage labels (vegetative, flowering, pod development, maturity)

**Soil Moisture Class:**
- Derived from soil sensors or field measurements
- Classes: Very dry (<30% VWC), Dry (30–50%), Optimal (50–70%), Wet (>70%)

**Dataset Scale:**
- **RGB Images**: 10,000–15,000 images
- **Multispectral Images**: 8,000–12,000 images
- **Thermal Images**: 5,000–8,000 images
- **Annotated Patches**: 50,000–100,000 (256×256 or 512×512 patches)

### 3.3 Soil & Pod-Zone Proxy Dataset

#### 3.3.1 Data Collection

**Sensor Deployment:**
- 1–2 sensors per hectare
- Depth: 5–10 cm (pod zone)
- Parameters: Soil moisture (VWC), soil temperature, EC
- Logging: 15-minute intervals, continuous

**Weather Integration:**
- Daily aggregates from IMD/NASA POWER
- Parameters: Temperature, precipitation, humidity, solar radiation

**Agronomic Metadata:**
- Cultivar (Spanish/Virginia, specific varieties)
- Planting date
- Irrigation schedule
- Fertilizer application
- Estimated pod depth (cultivar-dependent)

#### 3.3.2 Labels

**Pod Stress Indicators:**
- Derived from limited pod excavation (10–20% of plots)
- Visual pod quality (healthy, discolored, shriveled)
- Pod moisture content (laboratory measurement)

**Yield Loss Proxy:**
- Harvest yield measurements (kg/ha)
- Pod count per plant
- Pod fill percentage

**Dataset Scale:**
- **Sensor Time Series**: 5,000+ sensor-days
- **Weather Records**: 2,000+ field-days
- **Pod Excavation Samples**: 200–500 plots
- **Yield Measurements**: 50–100 fields

### 3.4 Seed & Pod Spectral Dataset

#### 3.4.1 Data Collection

**Sampling Strategy:**
- **Triggered Sampling**: Hyperspectral analysis of seeds from UAV-flagged stress areas
- **Random Sampling**: Baseline healthy samples
- **Harvest Sampling**: Representative samples from each field

**Equipment:**
- Portable hyperspectral spectrometer (400–2500 nm)
- Laboratory-grade NIR spectrometer for validation
- Sample preparation: Dried seeds, uniform lighting

**Spectral Acquisition:**
- 3–5 spectra per seed sample (averaged)
- Background correction
- Calibration with white reference

#### 3.4.2 Labels

**Laboratory-Confirmed Labels:**

1. **Healthy vs. Infected:**
   - Visual inspection
   - Fungal culture (Aspergillus, other pathogens)
   - Binary classification

2. **Germination Rate:**
   - Standard germination test (ISTA protocol)
   - Percentage germination after 7–10 days
   - Continuous label (0–100%)

3. **Fungal Presence:**
   - Microscopic examination
   - Culture-based identification
   - Multi-class: None, Aspergillus flavus, A. parasiticus, Other

4. **Aflatoxin Level:**
   - HPLC or ELISA measurement
   - Total aflatoxin (B1+B2+G1+G2) in ppb
   - Regulatory threshold: 20 ppb (India), 10–20 ppb (international)

**Dataset Scale:**
- **Hyperspectral Seed Samples**: 1,000–3,000 samples
- **Spectral Bands**: 2151 (400–2500 nm, 3 nm resolution)
- **Labeled Samples**: 100% (all samples have ground truth)
- **Aflatoxin Measurements**: 500–1,000 samples (expensive, subset)

### 3.5 Storage Environment Dataset

#### 3.5.1 Data Collection

**Storage Units:**
- 10–20 storage facilities (silos, warehouses, bags)
- Varied conditions (controlled vs. ambient)
- Duration: 3–6 months post-harvest

**IoT Sensors:**
- Temperature, RH, CO₂, VOC
- Continuous logging (5-minute intervals)
- Alerts for threshold breaches

**Spoilage Events:**
- Visual inspection records
- Fungal growth onset (timestamped)
- Seed quality degradation tracking

#### 3.5.2 Labels

**Spoilage Events:**
- Binary: Spoilage detected (yes/no)
- Timestamp of onset
- Severity level (mild, moderate, severe)

**Fungal Growth Onset:**
- Timestamp when fungal activity first detected
- Type of fungal growth (if identified)

**Dataset Scale:**
- **Sensor Hours**: 5,000+ hours
- **Storage Units**: 10–20 units
- **Spoilage Events**: 20–50 events
- **Time Series Records**: 100,000+ data points

### 3.6 Dataset Structure

```
AIRS-GSeed_Dataset/
├── Field_UAV/
│   ├── RGB/
│   │   ├── Season1/
│   │   │   ├── Field01/
│   │   │   │   ├── Flight01/
│   │   │   │   │   ├── images/
│   │   │   │   │   ├── orthomosaic.tif
│   │   │   │   │   └── metadata.json
│   │   │   │   └── ...
│   │   │   └── ...
│   │   └── Season2/
│   ├── Multispectral/
│   │   └── (similar structure)
│   ├── Thermal/
│   │   └── (similar structure)
│   └── Annotations/
│       ├── disease_polygons.geojson
│       ├── stress_maps.tif
│       └── labels.csv
├── Soil_Sensors/
│   ├── Field01_Sensor01.csv
│   ├── Field01_Sensor02.csv
│   └── ...
├── Weather/
│   ├── IMD_Field01.csv
│   └── NASA_POWER_Field01.csv
├── Hyperspectral_Seeds/
│   ├── spectra/
│   │   ├── sample_001.asd
│   │   └── ...
│   ├── labels.csv
│   └── metadata.csv
├── Storage_IoT/
│   ├── StorageUnit01/
│   │   ├── sensor_data.csv
│   │   └── spoilage_events.csv
│   └── ...
└── Metadata/
    ├── field_info.csv
    ├── agronomic_data.csv
    └── ground_truth_summary.csv
```

### 3.7 Data Splits

**Training Set**: 70%
- Stratified by field, season, disease presence
- Ensures representation across conditions

**Validation Set**: 15%
- Used for hyperparameter tuning
- Model selection

**Test Set**: 15%
- Held-out fields/seasons
- Final performance evaluation
- No data leakage from training

### 3.8 Data Augmentation

**Image Augmentation:**
- Rotation, flip, scale
- Color jitter (illumination variation)
- Mixup, CutMix
- Synthetic disease lesion generation (GAN-based)

**Spectral Augmentation:**
- Noise injection
- Baseline drift simulation
- Wavelength shift (calibration variation)

**Temporal Augmentation:**
- Time warping
- Subsequence sampling

---

## 4. Inputs & Outputs

### 4.1 Formal Input Specifications

#### 4.1.1 Sensor Inputs

**UAV RGB Images:**
- **Format**: GeoTIFF, JPEG (with EXIF geotags)
- **Dimensions**: Variable (orthomosaics: 5000×5000 to 20000×20000 pixels)
- **Coordinate System**: WGS84 UTM
- **Metadata**: Flight altitude, timestamp, camera parameters, GSD

**UAV Multispectral Images:**
- **Format**: GeoTIFF (5 bands: R, G, B, Red-edge, NIR)
- **Calibration**: Reflectance values (0–1) or DN with calibration coefficients
- **Dimensions**: Similar to RGB
- **Metadata**: Band center wavelengths, FWHM, calibration date

**UAV Thermal Images:**
- **Format**: GeoTIFF (temperature in °C)
- **Dimensions**: Lower resolution than RGB
- **Metadata**: Emissivity, ambient temperature, calibration parameters

**Soil Sensor Data:**
- **Format**: CSV time series
- **Columns**: Timestamp, Soil_Moisture_VWC (%), Soil_Temperature (°C), EC (dS/m), Sensor_ID, Field_ID
- **Frequency**: 15-minute intervals
- **Metadata**: Sensor location (lat/lon), depth, calibration date

**Hyperspectral Seed Spectra:**
- **Format**: CSV or binary (ASD format)
- **Dimensions**: 2151 wavelengths (400–2500 nm, 3 nm resolution)
- **Values**: Reflectance (0–1) or absorbance
- **Metadata**: Sample_ID, Field_ID, Harvest_Date, Cultivar

**Storage IoT Data:**
- **Format**: CSV time series
- **Columns**: Timestamp, Temperature (°C), RH (%), CO₂ (ppm), VOC (binary/qualitative), Storage_Unit_ID
- **Frequency**: 5-minute intervals
- **Metadata**: Storage unit location, capacity, seed batch ID

#### 4.1.2 Climate & Weather Inputs

**Weather Data:**
- **Format**: CSV time series
- **Columns**: Date, Temperature_Max (°C), Temperature_Min (°C), Precipitation (mm), RH_Mean (%), Solar_Radiation (MJ/m²), Wind_Speed (m/s)
- **Source**: IMD, NASA POWER, or local weather stations
- **Spatial Resolution**: Grid-based, interpolated to field coordinates

#### 4.1.3 Agronomic Metadata

**Field Information:**
- **Format**: JSON or CSV
- **Fields**: Field_ID, Cultivar, Planting_Date, Area (ha), Location (lat/lon), Soil_Type, Irrigation_Type

**Harvest Information:**
- **Format**: JSON or CSV
- **Fields**: Harvest_Date, Yield (kg/ha), Pod_Count, Moisture_Content (%)

### 4.2 Formal Output Specifications

#### 4.2.1 Canopy Stress Maps

**Format**: GeoTIFF raster
- **Bands**: 
  - Stress_Probability (0–1, float32)
  - Disease_Class (0=healthy, 1=leaf_spot, 2=rust, 3=unknown, uint8)
  - Confidence (0–1, float32)
- **Spatial Resolution**: Matches input UAV imagery
- **Coordinate System**: WGS84 UTM
- **Metadata**: Prediction date, model version, uncertainty metrics

#### 4.2.2 Pod-Zone Stress Index

**Format**: GeoTIFF raster or vector (point data)
- **Bands/Attributes**:
  - Pod_Stress_Index (0–1, float32)
  - Estimated_Pod_Moisture (%, float32)
  - Estimated_Pod_Temperature (°C, float32)
  - Confidence (0–1, float32)
- **Spatial Resolution**: Grid-based (10–50 m) or point-based (sensor locations)
- **Metadata**: Inference method, physics constraints used

#### 4.2.3 Seed Health Index (SHI)

**Format**: JSON or CSV
- **Fields**:
  - Sample_ID (string)
  - SHI (0–100, float)
  - SHI_Confidence (0–1, float)
  - SHI_Uncertainty_Interval (lower, upper, float)
  - Predicted_Germination_Rate (0–100%, float)
  - Predicted_Infection_Risk (0–1, float)
  - Contributing_Features (JSON object with feature importance)
- **Metadata**: Model version, prediction timestamp, input data sources

#### 4.2.4 Aflatoxin Risk Score (ARS)

**Format**: JSON or CSV
- **Fields**:
  - Sample_ID or Batch_ID (string)
  - ARS (0–100, float)
  - ARS_Confidence (0–1, float)
  - ARS_Uncertainty_Interval (lower, upper, float)
  - Predicted_Aflatoxin_ppb (float, with confidence interval)
  - Risk_Category (string: Low, Moderate, High, Very High, Critical)
  - Contributing_Factors (JSON object: field_conditions, storage_conditions, temporal_trends)
- **Metadata**: Model version, prediction timestamp, regulatory thresholds

#### 4.2.5 Harvest Window Recommendation

**Format**: JSON
- **Fields**:
  - Field_ID (string)
  - Recommended_Harvest_Start (date)
  - Recommended_Harvest_End (date)
  - Urgency_Level (string: Low, Medium, High, Critical)
  - Rationale (string: explanation)
  - Current_ARS (float)
  - Current_SHI (float)
  - Days_Since_Flowering (integer)
- **Metadata**: Recommendation date, confidence

#### 4.2.6 Storage Risk Alerts

**Format**: JSON (real-time alerts) or CSV (historical)
- **Fields**:
  - Storage_Unit_ID (string)
  - Alert_Type (string: Temperature, RH, CO₂, VOC, ARS_Escalation)
  - Alert_Severity (string: Info, Warning, Critical)
  - Alert_Timestamp (datetime)
  - Current_Value (float)
  - Threshold_Value (float)
  - Recommended_Action (string)
  - Predicted_ARS_7days (float, if applicable)
- **Metadata**: Alert ID, acknowledgment status

#### 4.2.7 Explainability Maps

**Format**: GeoTIFF or PNG (with georeferencing)
- **SHAP Feature Importance Maps**:
  - Per-pixel or per-region feature contributions
  - Bands: Contribution_RGB, Contribution_NDVI, Contribution_Thermal, etc.
- **Attention Maps**:
  - Spatial attention heatmaps from ViT models
  - Temporal attention for disease progression
- **Spectral Attribution**:
  - Wavelength importance plots (PNG/PDF)
  - Absorption feature identification
- **Metadata**: Explanation method, model version, visualization parameters

### 4.3 Output Aggregation Levels

**Pixel-Level**: Individual pixel predictions (stress maps)
**Plot-Level**: Aggregated predictions for field plots (10×10 m to 50×50 m)
**Field-Level**: Field-wide statistics and recommendations
**Batch-Level**: Seed batch quality assessments
**Storage-Level**: Storage unit risk assessments

---

## 5. Validation & Experimental Design

### 5.1 Study Area & Data Collection

#### 5.1.1 Geographic Coverage

**Primary Study Regions:**
1. **Gujarat** (Saurashtra region)
   - Semi-arid climate
   - Major groundnut-growing area
   - 5–8 fields, 2 seasons

2. **Andhra Pradesh** (Anantapur, Kurnool)
   - Arid to semi-arid
   - High aflatoxin risk zone
   - 5–8 fields, 2 seasons

3. **Tamil Nadu** (Vellore, Dharmapuri)
   - Semi-arid
   - Diverse cultivars
   - 4–6 fields, 2 seasons

**Field Selection Criteria:**
- Varied farm sizes (0.5–20 ha)
- Different cultivars (Spanish, Virginia types)
- Varied irrigation (rainfed, irrigated)
- Consent for UAV operations and sensor deployment

#### 5.1.2 Timeline

**Season 1 (Kharif):**
- Planting: June–July
- Monitoring: July–November (120 DAS)
- Harvest: October–November
- Storage: November–February (3 months)

**Season 2 (Rabi/Summer):**
- Planting: January–February
- Monitoring: February–May (120 DAS)
- Harvest: May–June
- Storage: June–September (3 months)

**Total Duration**: 18–24 months (including data processing, model development)

### 5.2 Ground Truth Collection

#### 5.2.1 Visual Disease Scoring

**Protocol:**
- Weekly field visits by trained agronomists
- Disease severity assessment using standard scales:
  - **Leaf Spot**: 0–9 scale (0=no disease, 9=severe)
  - **Rust**: Percentage leaf area affected
- GPS-tagged photographs of disease symptoms
- Annotated polygons on orthomosaics (using QGIS/ArcGIS)

**Quality Control:**
- Inter-rater reliability assessment (Cohen's kappa >0.7)
- Expert validation of ambiguous cases
- Cross-validation with laboratory analysis

#### 5.2.2 Soil Moisture Reference

**Methods:**
- **Gravimetric Method**: Soil samples, oven-drying (gold standard)
- **TDR (Time Domain Reflectometry)**: Portable device validation
- **Calibration**: Sensor readings calibrated against gravimetric measurements

**Frequency:**
- Weekly during critical stages
- Coincident with UAV flights
- 5–10 sampling points per field

#### 5.2.3 Seed Germination Tests

**Protocol:**
- ISTA (International Seed Testing Association) standard
- 4 replicates of 100 seeds per sample
- Conditions: 25°C, 7–10 days
- Germination rate = (germinated seeds / total seeds) × 100

**Samples:**
- 500–1,000 seed samples across fields and stress conditions
- Stratified sampling (healthy, moderate stress, severe stress areas)

#### 5.2.4 Aflatoxin Laboratory Measurements

**Methods:**
- **HPLC (High-Performance Liquid Chromatography)**: Gold standard
  - Detection limit: 0.1 ppb
  - Measures B1, B2, G1, G2 separately
- **ELISA (Enzyme-Linked Immunosorbent Assay)**: Rapid screening
  - Detection limit: 1–5 ppb
  - Used for initial screening, validated with HPLC

**Samples:**
- 500–1,000 samples (subset due to cost)
- Stratified by:
  - Pre-harvest ARS predictions (high-risk vs. low-risk)
  - Storage conditions (high-risk vs. low-risk storage)
  - Random baseline samples

**Quality Assurance:**
- Certified laboratory (NABL accredited)
- Internal standards and spiked samples
- Inter-laboratory validation (10% samples)

#### 5.2.5 Storage Spoilage Observation

**Protocol:**
- Weekly visual inspections
- Fungal growth detection (timestamped)
- Seed quality assessment (discoloration, mold, odor)
- Photographic documentation

**Metrics:**
- Time to spoilage onset
- Spoilage severity (mild, moderate, severe)
- Fungal species identification (when possible)

### 5.3 Evaluation Metrics

#### 5.3.1 Classification Metrics

**Canopy Stress Detection:**
- **Accuracy**: Overall classification accuracy
- **Precision, Recall, F1-Score**: Per disease class
- **Macro F1**: Average F1 across classes
- **Confusion Matrix**: Detailed error analysis
- **AUC-ROC**: For binary stress detection (healthy vs. stressed)

**Seed Health Classification:**
- **Accuracy**: SHI category classification (Excellent/Good/Moderate/Poor)
- **Cohen's Kappa**: Agreement with ground truth categories
- **Per-Class Metrics**: Precision, recall for each category

#### 5.3.2 Regression Metrics

**SHI Prediction:**
- **RMSE (Root Mean Squared Error)**: Overall prediction error
- **MAE (Mean Absolute Error)**: Average absolute error
- **R² (Coefficient of Determination)**: Explained variance
- **Pearson Correlation**: Linear relationship with ground truth

**ARS / Aflatoxin Prediction:**
- **RMSE**: Prediction error in risk score or ppb
- **MAE**: Average absolute error
- **R²**: Model fit
- **Log RMSE**: For log-transformed aflatoxin (handles wide range)
- **Percentage within Regulatory Threshold**: Accuracy of risk categorization

**Pod-Zone Stress Inference:**
- **RMSE**: For pod moisture, temperature estimates
- **Correlation**: With limited excavation ground truth

#### 5.3.3 Early Detection Metrics

**Lead Time:**
- **Days Before Visual Symptoms**: Time between AI detection and human-visible symptoms
- **Days Before Harvest**: Early warning for harvest timing
- **Days Before Storage Spoilage**: Prediction lead time for storage interventions

**Sensitivity at Fixed Specificity:**
- **Early Detection Rate**: Percentage of cases detected X days before symptoms
- **False Positive Rate**: At different lead times

#### 5.3.4 Cost–Benefit Metrics

**Economic Impact:**
- **Cost per Hectare**: Total system cost (UAV, sensors, analysis)
- **Yield Loss Avoided**: Estimated yield saved through early intervention
- **Aflatoxin Contamination Avoided**: Estimated ppb reduction
- **ROI (Return on Investment)**: For different farm scales

**Operational Efficiency:**
- **Processing Time**: Time from data acquisition to actionable output
- **False Alarm Rate**: Unnecessary interventions triggered
- **Intervention Success Rate**: Effectiveness of recommended actions

### 5.4 Baseline Models

#### 5.4.1 RGB-Only CNN Disease Detection

**Architecture:**
- ResNet-50 or EfficientNet-B3
- Trained on RGB images only
- Binary classification (healthy vs. diseased)

**Purpose**: Evaluate contribution of multispectral and thermal data

#### 5.4.2 NDVI Threshold Methods

**Method:**
- Simple NDVI threshold (<0.5 = stress)
- No machine learning
- Standard remote sensing approach

**Purpose**: Compare against simple vegetation index methods

#### 5.4.3 Single-Stage Hyperspectral Models

**Architecture:**
- 1D CNN or PLS (Partial Least Squares) regression
- Hyperspectral data only (no UAV or soil fusion)
- Direct aflatoxin prediction from spectra

**Purpose**: Evaluate multi-modal fusion benefits

#### 5.4.4 Non-Temporal AI Models

**Architecture:**
- Same as AIRS-GSeed but without temporal modeling
- Single time-point predictions only

**Purpose**: Evaluate temporal modeling contribution

#### 5.4.5 Random Forest / XGBoost Baselines

**Method:**
- Traditional ML on handcrafted features
- No deep learning
- Interpretable baseline

**Purpose**: Compare deep learning vs. traditional ML

### 5.5 Ablation & Sensitivity Analysis

#### 5.5.1 Component Ablation

**Ablation 1: Remove Pod-Zone Inference**
- Use only canopy features for SHI/ARS prediction
- **Hypothesis**: Pod-zone inference improves accuracy

**Ablation 2: Remove Hyperspectral Triggering**
- Use only UAV and soil data (no hyperspectral)
- **Hypothesis**: Hyperspectral data is critical for seed health assessment

**Ablation 3: Remove Temporal Modeling**
- Single time-point predictions only
- **Hypothesis**: Temporal context improves early detection

**Ablation 4: Remove Multi-Modal Fusion**
- Use only one modality (RGB, or multispectral, or soil)
- **Hypothesis**: Multi-modal fusion improves robustness

#### 5.5.2 Sensor Dropout Scenarios

**Scenario 1: Missing Thermal Data**
- Evaluate performance with only RGB + multispectral

**Scenario 2: Missing Soil Sensors**
- Evaluate performance without soil data

**Scenario 3: Missing Hyperspectral Data**
- Evaluate performance with UAV data only

**Purpose**: Assess robustness to sensor failures or cost constraints

#### 5.5.3 Sensitivity Analysis

**Parameter Sensitivity:**
- Model hyperparameters (learning rate, batch size, architecture depth)
- Fusion weights (early vs. late fusion)
- Uncertainty thresholds

**Data Sensitivity:**
- Training set size (learning curves)
- Label noise impact
- Temporal resolution impact (weekly vs. bi-weekly flights)

### 5.6 Statistical Analysis

**Significance Testing:**
- Paired t-tests or Wilcoxon signed-rank tests for model comparisons
- Confidence intervals for metrics (bootstrap or cross-validation)
- Multiple comparison correction (Bonferroni or FDR)

**Cross-Validation:**
- 5-fold or 10-fold cross-validation for hyperparameter tuning
- Leave-one-field-out validation for generalization assessment
- Temporal cross-validation (train on Season 1, test on Season 2)

---

## 6. Novelty & Contributions

### 6.1 Scientific Novelty

#### 6.1.1 Underground Pod-Zone Stress Inference

**Novel Contribution:**
- First AI framework to infer underground pod-zone stress non-invasively using above-ground remote sensing proxies
- Physics-informed neural network (PINN) that incorporates soil physics constraints (moisture diffusion, heat transfer) into deep learning
- Integration of canopy stress signals with soil sensor data and weather history to estimate pod conditions without excavation

**Advancement Over Literature:**
- Existing methods focus on above-ground canopy stress only
- No previous work models pod-zone conditions for groundnut using multi-modal remote sensing
- Physics-informed ML for agriculture is emerging but not applied to pod-zone inference

#### 6.1.2 Pre-Symptomatic Seed Health Prediction

**Novel Contribution:**
- Multi-modal fusion of UAV, hyperspectral, and environmental data to predict seed health before harvest
- Integration of field conditions (pre-harvest) with seed spectral signatures for comprehensive health assessment
- Seed Health Index (SHI) as a unified metric combining germination potential, infection risk, and quality indicators

**Advancement Over Literature:**
- Existing seed health assessment is post-harvest only
- No previous framework predicts seed health from pre-harvest field conditions
- Hyperspectral seed analysis exists but not integrated with field monitoring

#### 6.1.3 End-to-End Aflatoxin Risk Prediction

**Novel Contribution:**
- First framework to predict aflatoxin risk from field monitoring through storage, integrating all stages
- Multi-stage risk modeling: pre-harvest field conditions → harvest seed quality → post-harvest storage conditions
- Temporal risk escalation modeling that updates predictions as storage conditions change

**Advancement Over Literature:**
- Existing aflatoxin prediction models are single-stage (field-only or storage-only)
- No previous work integrates UAV remote sensing with storage IoT for aflatoxin risk
- Limited work on pre-harvest aflatoxin risk prediction

#### 6.1.4 Explainable AI for Agricultural Decision-Making

**Novel Contribution:**
- Comprehensive explainability framework combining SHAP, attention maps, and spectral attribution
- Actionable decision rules that translate AI predictions into farmer interventions
- Uncertainty-aware predictions with confidence intervals for risk-based decision-making

**Advancement Over Literature:**
- Most agricultural AI systems are black-box
- Limited explainability for multi-modal agricultural predictions
- Decision rules are often ad-hoc, not systematically derived from model outputs

### 6.2 Engineering Novelty

#### 6.2.1 Multi-Modal Data Fusion Architecture

**Novel Contribution:**
- Hierarchical fusion strategy (pixel → plot → field → batch levels)
- Attention-based cross-modal fusion for pod-zone inference
- Adaptive fusion weights based on data quality and availability

**Advancement Over Literature:**
- Existing fusion methods are simple concatenation or averaging
- No previous work uses attention mechanisms for agricultural multi-modal fusion
- Limited work on handling missing modalities gracefully

#### 6.2.2 Cost-Optimized Adaptive Sampling

**Novel Contribution:**
- Triggered hyperspectral sampling based on UAV stress alerts (reduces cost by 60–80%)
- Adaptive UAV flight scheduling based on risk thresholds
- Sensor data downsampling during low-risk periods

**Advancement Over Literature:**
- Existing systems use fixed sampling schedules
- No previous work optimizes sampling based on AI predictions
- Limited cost optimization in agricultural remote sensing

#### 6.2.3 Scalable Deployment Architecture

**Novel Contribution:**
- Multi-scale deployment (smallholder to commercial) with different sensor configurations
- Edge computing options for real-time processing
- Federated learning framework for privacy-preserving model updates across farms

**Advancement Over Literature:**
- Most systems are designed for single scale
- Limited work on scalable agricultural AI deployment
- Federated learning in agriculture is emerging but not widely deployed

### 6.3 Practical Impact

#### 6.3.1 Food Safety

**Impact:**
- Early aflatoxin risk detection prevents contaminated produce from entering food chain
- Regulatory compliance support (meets India's 20 ppb limit, international standards)
- Traceability from field to storage for food safety audits

**Beneficiaries:**
- Consumers (reduced aflatoxin exposure)
- Food safety regulators (risk-based inspection)
- Export-oriented farmers (meet international standards)

#### 6.3.2 Economic Benefits

**Impact:**
- Early disease detection enables timely interventions (reduces yield loss by 10–20%)
- Optimal harvest timing maximizes seed quality and market value
- Storage risk alerts prevent spoilage (saves 5–15% of stored produce)

**Quantified Benefits (Expected):**
- Yield loss reduction: 10–20% (worth $200–500/ha)
- Aflatoxin contamination reduction: 30–50% (prevents rejection, worth $100–300/ha)
- Storage loss reduction: 5–15% (worth $50–150/ha)
- **Total benefit: $350–950/ha per season**

**Cost:**
- System cost: $50–500/ha (depending on scale)
- **ROI: 7–19x for commercial farms, 2–5x for smallholders**

#### 6.3.3 Sustainability

**Impact:**
- Precision interventions reduce pesticide use (targeted application only)
- Optimal irrigation timing reduces water use
- Prevents food waste (reduces post-harvest losses)

**Environmental Benefits:**
- Reduced chemical inputs (10–20% reduction)
- Water conservation (5–10% reduction through optimal timing)
- Lower carbon footprint (reduced food waste)

### 6.4 Advancement Over Existing Literature

#### 6.4.1 Comparison with Existing Systems

**Existing UAV Disease Detection Systems:**
- **Limitation**: Focus on above-ground symptoms only
- **AIRS-GSeed Advantage**: Infers underground pod stress, predicts seed health

**Existing Hyperspectral Seed Analysis:**
- **Limitation**: Post-harvest only, no field integration
- **AIRS-GSeed Advantage**: Pre-harvest prediction, integrated with field monitoring

**Existing Aflatoxin Prediction Models:**
- **Limitation**: Single-stage (field or storage), limited remote sensing integration
- **AIRS-GSeed Advantage**: End-to-end prediction, multi-modal remote sensing

**Existing Agricultural AI Systems:**
- **Limitation**: Black-box models, limited explainability
- **AIRS-GSeed Advantage**: Comprehensive explainability, actionable decision rules

#### 6.4.2 Publication Readiness

**Target Journals:**
1. **Nature Scientific Reports**: Broad impact, multi-disciplinary
2. **Remote Sensing (MDPI)**: Remote sensing focus, open access
3. **Computers and Electronics in Agriculture**: Agricultural AI focus
4. **IEEE Transactions on Geoscience and Remote Sensing**: Technical depth, remote sensing community

**Contribution Alignment:**
- Novel methodology (pod-zone inference, multi-modal fusion)
- Comprehensive validation (multi-season, multi-location)
- Practical impact (food safety, economic benefits)
- Explainable AI (transparency for adoption)

---

## 7. Expected Results & Discussion

### 7.1 Expected Quantitative Results

#### 7.1.1 Canopy Stress Detection Performance

**Expected Metrics:**
- **Accuracy**: 85–92% (multi-class: healthy, leaf spot, rust, unknown)
- **F1-Score (Macro)**: 0.82–0.90
- **AUC-ROC (Binary)**: 0.90–0.95
- **Early Detection Lead Time**: 7–14 days before visual symptoms

**Comparison with Baselines:**
- **vs. RGB-Only CNN**: +5–10% accuracy improvement (multispectral + thermal contribution)
- **vs. NDVI Threshold**: +15–25% accuracy improvement (deep learning advantage)
- **vs. Non-Temporal Model**: +3–7% accuracy improvement (temporal context)

**Key Insights:**
- Multispectral bands (Red-edge, NIR) are critical for early stress detection
- Thermal data improves water stress detection accuracy
- Temporal modeling enables pre-symptomatic detection

#### 7.1.2 Pod-Zone Stress Inference Performance

**Expected Metrics:**
- **Pod Moisture Estimation RMSE**: 5–8% VWC
- **Correlation with Ground Truth**: 0.70–0.85 (limited excavation data)
- **Pod Temperature Estimation RMSE**: 1–2°C

**Comparison with Baselines:**
- **vs. Canopy-Only Inference**: +10–15% correlation improvement (soil sensor integration)
- **vs. Non-Physics-Informed ML**: +5–10% accuracy improvement (physics constraints)

**Key Insights:**
- Physics-informed constraints improve generalization to unseen conditions
- Soil sensor data is essential for accurate pod-zone inference
- Canopy stress alone is insufficient for pod-zone prediction

#### 7.1.3 Seed Health Index (SHI) Prediction Performance

**Expected Metrics:**
- **RMSE**: 8–12 points (on 0–100 scale)
- **R²**: 0.75–0.85
- **Correlation with Germination Rate**: 0.80–0.90
- **Classification Accuracy (4 categories)**: 80–88%

**Comparison with Baselines:**
- **vs. Hyperspectral-Only**: +5–10% R² improvement (UAV + soil fusion)
- **vs. UAV-Only (No Hyperspectral)**: +15–20% R² improvement (hyperspectral critical)
- **vs. Single Time-Point**: +3–5% R² improvement (temporal features)

**Key Insights:**
- Hyperspectral data is essential for accurate seed health assessment
- Pre-harvest field conditions provide valuable context (10–15% improvement)
- Multi-modal fusion improves robustness to missing data

#### 7.1.4 Aflatoxin Risk Score (ARS) Prediction Performance

**Expected Metrics:**
- **RMSE (Risk Score)**: 10–15 points (on 0–100 scale)
- **RMSE (Aflatoxin ppb, log-transformed)**: 0.3–0.5 log units
- **R²**: 0.70–0.80
- **Accuracy (Risk Category)**: 75–85%
- **Early Warning Lead Time**: 14–21 days before regulatory threshold breach

**Comparison with Baselines:**
- **vs. Field-Only Model**: +10–15% R² improvement (storage integration)
- **vs. Storage-Only Model**: +5–10% R² improvement (pre-harvest field conditions)
- **vs. Hyperspectral-Only**: +8–12% R² improvement (multi-modal fusion)

**Key Insights:**
- Pre-harvest field conditions are predictive of aflatoxin risk (30–40% of variance)
- Storage conditions are critical for post-harvest risk escalation
- Multi-stage modeling (field → harvest → storage) improves accuracy

#### 7.1.5 Ablation Study Results

**Expected Findings:**
- **Pod-Zone Inference Removal**: -8–12% SHI/ARS accuracy
- **Hyperspectral Removal**: -15–20% SHI/ARS accuracy
- **Temporal Modeling Removal**: -5–8% early detection performance
- **Multi-Modal Fusion Removal**: -10–15% overall accuracy

**Interpretation:**
- All components contribute significantly
- Hyperspectral data is most critical for seed health assessment
- Pod-zone inference provides unique value for groundnut (underground pods)

### 7.2 Agronomic Insights

#### 7.2.1 Disease Progression Patterns

**Expected Findings:**
- Leaf spot and rust show distinct spectral signatures 7–14 days before visual symptoms
- Canopy temperature elevation precedes visible stress by 5–10 days
- Disease progression is accelerated under high soil moisture (>70% VWC) and high temperature (>30°C)

**Practical Implications:**
- Early intervention (fungicide application) can be timed 1–2 weeks earlier
- Irrigation management can reduce disease risk (avoid over-irrigation during critical stages)

#### 7.2.2 Pod-Zone Stress Drivers

**Expected Findings:**
- Pod moisture is strongly correlated with soil moisture at 5–10 cm depth (r=0.75–0.85)
- Pod temperature follows soil temperature with 1–2°C lag
- High pod-zone stress (moisture >70% or temperature >35°C) increases aflatoxin risk by 2–3x

**Practical Implications:**
- Soil moisture management is critical for pod health
- Shallow irrigation or mulching can moderate pod-zone temperature
- Harvest timing should avoid periods of high pod-zone stress

#### 7.2.3 Aflatoxin Risk Factors

**Expected Findings:**
- Pre-harvest field stress (disease, drought) increases aflatoxin risk by 1.5–2x
- Storage conditions (temperature >25°C, RH >70%) are primary drivers of post-harvest aflatoxin production
- Combined field + storage stress increases risk by 3–5x compared to optimal conditions

**Practical Implications:**
- Field interventions (disease management, optimal harvest timing) reduce baseline risk
- Storage management (cooling, aeration) is essential even for low-risk harvests
- Integrated field-to-storage monitoring is necessary for comprehensive risk management

### 7.3 Limitations

#### 7.3.1 Data Limitations

**Ground Truth Availability:**
- Limited pod excavation data (expensive, destructive)
- Aflatoxin measurements are costly (subset of samples only)
- Label noise in field disease scoring (subjective)

**Mitigation:**
- Semi-supervised learning for pod-zone inference
- Active learning for targeted aflatoxin sampling
- Inter-rater reliability protocols for disease scoring

#### 7.3.2 Model Limitations

**Generalization:**
- Models trained on specific regions may not generalize to all climates
- Cultivar-specific variations may require fine-tuning
- Limited validation across diverse soil types

**Mitigation:**
- Multi-region, multi-season training data
- Transfer learning and domain adaptation
- Cultivar-specific model variants

#### 7.3.3 Technical Limitations

**Sensor Constraints:**
- Hyperspectral equipment is expensive (limits widespread deployment)
- UAV flight restrictions (weather, regulatory)
- IoT sensor calibration drift over time

**Mitigation:**
- Cost-optimized adaptive sampling (reduces hyperspectral needs)
- Robust models that handle sensor failures
- Automated calibration protocols

#### 7.3.4 Economic Limitations

**Cost Barriers:**
- Initial investment may be prohibitive for smallholders
- Ongoing service costs (UAV flights, data processing)

**Mitigation:**
- Community-based deployment (shared resources)
- Pay-per-service models
- Government subsidies for food safety systems

### 7.4 Sustainability & Ethics

#### 7.4.1 Environmental Sustainability

**Positive Impacts:**
- Reduced pesticide use (precision interventions)
- Water conservation (optimal irrigation timing)
- Reduced food waste (prevented spoilage)

**Potential Concerns:**
- UAV operations have carbon footprint (minimal compared to benefits)
- Electronic waste from IoT sensors (recycling programs needed)

**Mitigation:**
- Optimize flight schedules (reduce unnecessary flights)
- Sensor recycling and reuse programs
- Lifecycle assessment to quantify net environmental benefit

#### 7.4.2 Social & Economic Equity

**Concerns:**
- Technology may favor large farms (economies of scale)
- Digital divide (smallholders may lack access)

**Mitigation:**
- Community-based deployment models
- Subsidized services for smallholders
- Government and NGO partnerships for equitable access

#### 7.4.3 Data Privacy & Ownership

**Concerns:**
- Farm data privacy (location, yield, practices)
- Data ownership and control

**Mitigation:**
- Federated learning (data stays on-farm)
- Transparent data use agreements
- Farmer control over data sharing

#### 7.4.4 Ethical AI

**Concerns:**
- Algorithmic bias (may favor certain cultivars or regions)
- Over-reliance on AI (reduces farmer autonomy)

**Mitigation:**
- Diverse training data (multiple regions, cultivars)
- Explainable AI (farmers understand recommendations)
- Decision support (not replacement) - farmers make final decisions

### 7.5 Future Directions

#### 7.5.1 Research Extensions

**Multi-Crop Generalization:**
- Extend framework to other pod crops (soybean, chickpea)
- Adapt pod-zone inference for different pod depths

**Advanced AI Methods:**
- Foundation models for agricultural remote sensing
- Few-shot learning for new cultivars or regions
- Reinforcement learning for optimal intervention timing

**Integration with Other Technologies:**
- Satellite imagery (Sentinel-2, Landsat) for regional monitoring
- Blockchain for traceability
- Digital twins for predictive modeling

#### 7.5.2 Deployment Scalability

**Technology Transfer:**
- Open-source software components
- Standardized data formats and APIs
- Training programs for extension services

**Commercialization:**
- Startup partnerships for technology deployment
- Licensing agreements with agricultural technology companies
- Government procurement for food safety programs

#### 7.5.3 Policy & Regulation

**Regulatory Integration:**
- Integration with food safety regulatory frameworks
- Certification programs for AI-assisted seed quality assessment
- Standards for explainable AI in agriculture

---

## 8. Conclusion

AIRS-GSeed represents a novel, comprehensive AI framework that addresses critical gaps in groundnut crop monitoring by integrating multi-modal remote sensing, spectral analysis, and IoT data to predict seed health and aflatoxin risk from field to storage. The framework's key innovations include:

1. **Non-invasive pod-zone stress inference** using physics-informed machine learning
2. **Pre-symptomatic seed health prediction** through multi-modal data fusion
3. **End-to-end aflatoxin risk modeling** spanning field monitoring to storage
4. **Explainable AI** with actionable decision rules for farmers and regulators

Expected performance metrics (85–92% disease detection accuracy, 75–85% SHI/ARS prediction R²) demonstrate the framework's potential for practical deployment. Economic analysis suggests 7–19x ROI for commercial farms, with significant food safety and sustainability benefits.

The framework is designed for publication in high-impact journals (Nature Scientific Reports, Remote Sensing, Computers and Electronics in Agriculture, IEEE TGRS) and addresses real-world challenges in groundnut production, food safety, and sustainable agriculture.

**Key Contributions to Science:**
- First AI framework for underground pod-zone stress inference in groundnut
- Novel multi-modal fusion architecture for agricultural remote sensing
- End-to-end aflatoxin risk prediction from field to storage
- Comprehensive explainability framework for agricultural AI

**Key Contributions to Practice:**
- Cost-effective early disease detection (7–14 days lead time)
- Actionable harvest timing and storage intervention recommendations
- Food safety compliance support (regulatory thresholds)
- Scalable deployment from smallholder to commercial farms

AIRS-GSeed sets a new standard for AI-driven precision agriculture in groundnut production and provides a template for extension to other crops with similar challenges (underground development, food safety risks, storage management).

---

## References

*[References section to be populated with relevant literature on:*
- *UAV-based crop disease detection*
- *Hyperspectral seed analysis*
- *Aflatoxin prediction models*
- *Physics-informed machine learning*
- *Multi-modal data fusion*
- *Explainable AI in agriculture*
- *Groundnut agronomy and pathology*
- *Food safety regulations and standards*
*]*

---

## Appendices

### Appendix A: Acronyms and Abbreviations

- **AIRS-GSeed**: AI-driven Remote Sensing for Groundnut Seed Health
- **ARS**: Aflatoxin Risk Score
- **SHI**: Seed Health Index
- **UAV**: Unmanned Aerial Vehicle
- **RGB**: Red, Green, Blue
- **NIR**: Near-Infrared
- **VOC**: Volatile Organic Compounds
- **RH**: Relative Humidity
- **EC**: Electrical Conductivity
- **VWC**: Volumetric Water Content
- **GSD**: Ground Sample Distance
- **DAS**: Days After Sowing
- **IMD**: India Meteorological Department
- **HPLC**: High-Performance Liquid Chromatography
- **ELISA**: Enzyme-Linked Immunosorbent Assay
- **NDVI**: Normalized Difference Vegetation Index
- **NDRE**: Normalized Difference Red-Edge Index
- **CNN**: Convolutional Neural Network
- **ViT**: Vision Transformer
- **PINN**: Physics-Informed Neural Network
- **LSTM**: Long Short-Term Memory
- **SHAP**: SHapley Additive exPlanations
- **FPO**: Farmer Producer Organization
- **ROI**: Return on Investment

### Appendix B: Model Hyperparameters

*[To be populated with final hyperparameters after experimentation]*

### Appendix C: Dataset Statistics

*[To be populated with final dataset statistics after collection]*

### Appendix D: Regulatory Thresholds

**India:**
- Total Aflatoxin: 30 ppb (B1+B2+G1+G2)
- Aflatoxin B1: 20 ppb

**International (EU, USA):**
- Total Aflatoxin: 10–20 ppb (varies by country)
- Aflatoxin B1: 5–10 ppb

**Seed Certification:**
- Germination Rate: ≥75% (certified seed)
- Moisture Content: ≤8% (storage)

---

*Document Version: 1.0*
*Last Updated: [Date]*
*Authors: [To be populated]*
