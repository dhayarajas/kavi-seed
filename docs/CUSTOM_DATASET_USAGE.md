# Custom Dataset Usage Guide

This guide explains how to use your custom seed quality dataset with the AIRS-GSeed framework.

## Quick Start

### 1. Ensure Dependencies are Installed

The system requires pandas, numpy, matplotlib, seaborn, and openpyxl:

```bash
# Using conda (recommended)
conda install -y pandas openpyxl numpy matplotlib seaborn scipy

# Or using pip (with virtual environment)
python3 -m venv venv
source venv/bin/activate
pip install pandas openpyxl numpy matplotlib seaborn scipy
```

### 2. Run Analysis

```bash
# Navigate to the project directory
cd /Users/dhaya/Kavitha-Agri/Codebase/AIRS-GSeet

# Option 1: Read and explore dataset only
/opt/anaconda3/bin/python read_custom_dataset.py

# Option 2: Generate complete analysis (recommended)
/opt/anaconda3/bin/python generate_custom_results.py
```

## Dataset Requirements

Your dataset should be an Excel file (`.xlsx`) with the following structure:

### Required Columns

- **Month** or **Date**: Temporal identifier
- **Germination (%)**: Germination percentage (0-100)
- **Vigour Index**: Seed vigour metric
- **Moisture content (%)**: Moisture percentage
- **Pathogen infestation (%)**: Pathogen levels (optional for initial measurements)

### Optional but Recommended Columns

- Root length (cm)
- Shoot length (cm)
- 100 Pod weight (g)
- 100 Seed weight (g)
- Electrical conductivity (dS/m)

### Example Format

```
| Month          | Germination (%) | Root length (cm) | ... |
|----------------|----------------|------------------|-----|
| September-2025 | 91             | 16.1            | ... |
| October-2025   | 85             | 16.0            | ... |
| November-2025  | 81             | 11.8            | ... |
```

## Generated Outputs

### Figures (PDF format)

Located in `results/` directory:

1. **`custom_temporal_analysis.pdf`**
   - Germination trends
   - Vigour index changes
   - Seed Health Index (SHI) over time
   - Aflatoxin Risk Score (ARS) progression

2. **`custom_quality_parameters.pdf`**
   - Root & shoot growth
   - Pod & seed weight
   - Moisture content
   - Electrical conductivity
   - Pathogen infestation
   - Multi-parameter heatmap

3. **`custom_airs_gseed_performance.pdf`**
   - SHI prediction accuracy
   - ARS prediction accuracy

### Data Files (CSV format)

Located in `results/` directory:

1. **`custom_dataset_summary.csv`**
   - Raw data with basic processing

2. **`custom_dataset_airs_gseed_analysis.csv`**
   - Full analysis with SHI and ARS
   - Quality status classifications
   - Risk level assessments

3. **`custom_dataset_summary_statistics.csv`**
   - Summary statistics
   - Percentage changes over time

## Understanding the Results

### Seed Health Index (SHI)

A composite metric (0-100) that combines multiple quality parameters:

- **80-100**: Excellent quality
- **70-80**: Good quality
- **60-70**: Fair quality
- **Below 60**: Poor quality (intervention needed)

**Formula:**
```
SHI = (Germination × 0.4) + (Vigour × 0.3) + 
      (Moisture Quality × 0.15) + (Pathogen-free × 0.15)
```

### Aflatoxin Risk Score (ARS)

A risk metric (0-100) indicating aflatoxin contamination likelihood:

- **0-20**: Low risk
- **20-40**: Medium risk (monitoring recommended)
- **40-60**: High risk (intervention required)
- **Above 60**: Critical risk (immediate action needed)

**Formula:**
```
ARS = (Moisture Risk × 0.5) + (Pathogen Risk × 0.35) + 
      (EC Risk × 0.15)
```

## Customization

### Changing Dataset Path

Edit the path in `generate_custom_results.py`:

```python
CUSTOM_DATASET_PATH = '../../Custom-Dataset/Your_Dataset.xlsx'
```

### Adjusting SHI/ARS Calculations

Modify the weight factors in `generate_custom_results.py`:

```python
def calculate_seed_health_index(df):
    # Adjust these weights based on your priorities
    shi = (germ_score * 0.4 +      # Germination weight
           vigour_score * 0.3 +    # Vigour weight
           moisture_score * 0.15 + # Moisture weight
           pathogen_score * 0.15)  # Pathogen weight
    return shi
```

### Adding New Parameters

To incorporate additional columns from your dataset:

1. Read the new parameter in `load_custom_dataset()`
2. Add normalization in `calculate_seed_health_index()` or `calculate_aflatoxin_risk_score()`
3. Update the visualization functions to include new plots
4. Adjust the weight factors accordingly

### Example: Adding Temperature Data

```python
def calculate_aflatoxin_risk_score(df):
    # ... existing code ...
    
    # Add temperature risk
    temp = df['Storage Temperature (°C)'].values
    temp_risk = (temp - 20) * 5  # Risk increases above 20°C
    temp_risk = np.clip(temp_risk, 0, 100)
    
    # Adjust ARS calculation
    ars = (moisture_risk * 0.4 +     # Reduced weight
           pathogen_risk * 0.3 +     # Reduced weight
           ec_risk * 0.15 +          # Same
           temp_risk * 0.15)         # New factor
    
    return ars
```

## Troubleshooting

### Issue: "Module not found"

**Solution:**
```bash
# Ensure you're using the correct Python interpreter
which python
/opt/anaconda3/bin/python --version

# Install missing packages
conda install -y <package-name>
```

### Issue: "File not found"

**Solution:**
- Check the dataset path in the script
- Ensure the Excel file is in the correct location
- Verify file permissions

### Issue: "Invalid column names"

**Solution:**
- Check your Excel column headers match expected names
- Update the script to use your actual column names
- Ensure no extra spaces in column headers

### Issue: Missing or NaN values

The scripts handle missing values automatically:
- Pathogen data: NaN values are replaced with 0
- Other parameters: Will generate warnings but continue

To customize missing value handling:

```python
df['Pathogen infestation (%)'].fillna(0, inplace=True)  # Fill with 0
# or
df.dropna(inplace=True)  # Remove rows with missing values
```

## Adding More Time Points

If you have data for more than 3 months:

1. Add rows to your Excel file
2. The scripts will automatically process all rows
3. Visualizations will scale accordingly

No code changes needed!

## Integration with Main Results

To combine custom dataset results with the main AIRS-GSeed paper results:

1. Custom results are saved separately with `custom_` prefix
2. You can reference them in the paper
3. Use both synthetic and real data for validation

## Best Practices

1. **Consistent Units**: Ensure all measurements use consistent units
2. **Regular Updates**: Run analysis after each new data collection
3. **Backup Data**: Keep original Excel file backed up
4. **Version Control**: Track changes to the dataset
5. **Documentation**: Note any data collection methodology changes

## Advanced Usage

### Batch Processing Multiple Datasets

Create a wrapper script:

```python
datasets = [
    'Dataset_Year1.xlsx',
    'Dataset_Year2.xlsx',
    'Dataset_Year3.xlsx'
]

for dataset in datasets:
    CUSTOM_DATASET_PATH = f'../../Custom-Dataset/{dataset}'
    main()  # Run analysis
```

### Comparing Multiple Storage Conditions

Modify the script to process multiple sheets or files and generate comparative plots.

### Export for Further Analysis

Results are saved as CSV for easy import into:
- Statistical software (R, SPSS)
- Spreadsheet programs (Excel, Google Sheets)
- Database systems
- Machine learning frameworks

## Support

For questions or issues:

1. Check this guide first
2. Review `CUSTOM_DATASET_RESULTS.md` for interpretation help
3. Examine the generated CSV files for data verification
4. Consult the main AIRS-GSeed framework documentation

## File Structure

```
Codebase/AIRS-GSeet/
├── read_custom_dataset.py          # Dataset reader and explorer
├── generate_custom_results.py      # Main analysis program
├── CUSTOM_DATASET_USAGE.md         # This file
├── CUSTOM_DATASET_RESULTS.md       # Results summary
├── results/
│   ├── custom_temporal_analysis.pdf
│   ├── custom_quality_parameters.pdf
│   ├── custom_airs_gseed_performance.pdf
│   ├── custom_dataset_airs_gseed_analysis.csv
│   ├── custom_dataset_summary_statistics.csv
│   └── custom_dataset_summary.csv
└── ../../Custom-Dataset/
    └── Three_Month_Seed_Quality_Data.xlsx
```

---

**Last Updated:** February 8, 2026  
**AIRS-GSeed Version:** 1.0 (Custom Dataset Integration)
