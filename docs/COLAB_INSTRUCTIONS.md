# Google Colab Execution Instructions

## Quick Start

1. **Upload the notebook to Google Colab:**
   - Go to [Google Colab](https://colab.research.google.com/)
   - Click "File" → "Upload notebook"
   - Select `AIRS-GSeed_Results_Generation.ipynb`

2. **Run all cells:**
   - Click "Runtime" → "Run all"
   - Or run each cell sequentially using Shift+Enter

3. **Download results:**
   - After execution, download the `results/` folder
   - Right-click on the folder in Colab's file browser
   - Select "Download"

## What the Notebook Does

The notebook generates:
- ✅ Architecture diagram (PDF + PNG)
- ✅ Canopy stress detection performance figures
- ✅ Seed Health Index (SHI) prediction results
- ✅ Aflatoxin Risk Score (ARS) prediction results
- ✅ Temporal ARS prediction visualizations
- ✅ Ablation study results
- ✅ All performance CSV files

## Output Files

After running, you'll have:
```
results/
├── architecture.pdf / .png
├── canopy_performance.pdf / .png / .csv
├── seed_health_results.pdf / .png
├── shi_performance.csv
├── ars_performance.csv
├── ars_temporal.pdf / .png
├── ablation_study.pdf / .png / .csv
└── pod_zone_performance.csv
```

## Notes

- The notebook is self-contained and doesn't require external data
- All figures are generated with publication-quality settings (300 DPI)
- CSV files contain all performance metrics for paper tables
- You can modify the code in any cell to customize outputs

## Troubleshooting

If you encounter issues:
1. Make sure you run the first cell (setup) before others
2. Check that all packages installed correctly
3. Restart runtime if needed: "Runtime" → "Restart runtime"
