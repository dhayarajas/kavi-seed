# AIRS-GSeed: AI-Driven Seed Quality Analysis Framework

[![License](https://img.shields.io/badge/License-Research-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Colab](https://img.shields.io/badge/Google-Colab-orange.svg)](https://colab.research.google.com/)

**AI-driven Remote Sensing for Groundnut Seed Quality Assessment and Aflatoxin Risk Prediction**

---

## 🎯 Overview

AIRS-GSeed is a comprehensive AI framework for groundnut seed health assessment using multi-modal remote sensing and machine learning. The system analyzes seed quality over time and predicts aflatoxin contamination risk.

### Key Features

- 🔬 **Seed Health Index (SHI)**: Composite quality metric (0-100 scale)
- ⚠️ **Aflatoxin Risk Score (ARS)**: Risk assessment metric (0-100 scale)
- 📊 **Temporal Analysis**: Track quality changes over months
- 🎨 **Professional Visualizations**: Publication-ready charts
- 📓 **Google Colab Ready**: No installation required
- 📈 **Real Data Analysis**: Custom 3-month groundnut seed dataset

---

## 🚀 Quick Start

### Option 1: Google Colab (Recommended - No Setup Required)

1. Open the notebook in Google Colab:
   - Go to [Google Colab](https://colab.research.google.com/)
   - Upload: `Codebase/AIRS-GSeet/AIRS_GSeed_Custom_Dataset_Analysis.ipynb`

2. Run the analysis:
   - Click **Runtime → Run all**
   - Wait 1-2 minutes

3. Download results:
   - 3 professional charts (PNG)
   - 2 data files (CSV)

📖 **Detailed Guide:** [HOW_TO_RUN_IN_COLAB.md](docs/HOW_TO_RUN_IN_COLAB.md)

### Option 2: Local Python

```bash
# Navigate to project directory
cd Codebase/AIRS-GSeet

# Run analysis
python generate_custom_results.py
```

**Requirements:** Python 3.8+, pandas, numpy, matplotlib, seaborn, openpyxl

---

## 📊 Dataset

**Three-Month Seed Quality Study**
- **Time Period:** September 2025 - November 2025
- **Parameters:** Germination, vigour, moisture, pathogen levels, electrical conductivity
- **Location:** `Custom-Dataset/Three_Month_Seed_Quality_Data.xlsx`

---

## 📈 Key Results

### Seed Quality Degradation (3 Months)

| Metric | Initial | Month 2 | Change |
|--------|---------|---------|--------|
| **Germination (%)** | 91.0 | 81.0 | **-11% ⚠️** |
| **Vigour Index** | 3,130 | 2,362 | **-24.5% ⚠️** |
| **SHI Score** | 82.18 | 65.08 | **-20.8% ⚠️** |
| **Quality Status** | Excellent | Fair | **Degraded** |

### Aflatoxin Risk Escalation

| Metric | Initial | Month 2 | Change |
|--------|---------|---------|--------|
| **ARS Score** | 0.00 | 23.31 | **+23.31 ⚠️** |
| **Pathogen (%)** | 0.00 | 6.66 | **+6.66% ⚠️** |
| **Risk Level** | Low | Medium | **Escalated** |

📖 **Full Analysis:** [CUSTOM_DATASET_RESULTS.md](docs/CUSTOM_DATASET_RESULTS.md)

---

## 📁 Repository Structure

```
├── Codebase/AIRS-GSeet/
│   ├── AIRS_GSeed_Custom_Dataset_Analysis.ipynb  ⭐ Main Jupyter Notebook
│   ├── generate_custom_results.py                 Python analysis script
│   ├── read_custom_dataset.py                     Dataset reader
│   ├── results/                                   Generated charts & CSVs
│   └── src/                                       Framework source code
│
├── Custom-Dataset/
│   └── Three_Month_Seed_Quality_Data.xlsx        ⭐ Your seed quality data
│
├── paper/                                         ⭐ Research manuscript
│   ├── paper.tex                                   LaTeX source
│   ├── references.bib                              Bibliography
│   ├── paper.pdf                                   Compiled manuscript
│   ├── figures/                                    Architecture diagrams
│   └── images/                                     Result visualizations
│
├── docs/                                          📚 Documentation
│   ├── HOW_TO_RUN_IN_COLAB.md                     Colab instructions
│   ├── CUSTOM_DATASET_RESULTS.md                  Analysis findings
│   ├── CUSTOM_DATASET_USAGE.md                    Usage guide
│   └── ... (15 documentation files)
│
├── Images/                                        Generated visualizations
└── Ref-Papers/                                    Reference literature
```

---

## 🔬 Methodology

### Seed Health Index (SHI)

```
SHI = (Germination × 0.4) + (Vigour × 0.3) + 
      (Moisture Quality × 0.15) + (Pathogen-free × 0.15)
```

**Interpretation:**
- **80-100:** Excellent quality ✅
- **70-80:** Good quality 🟢
- **60-70:** Fair quality 🟡
- **<60:** Poor quality 🔴

### Aflatoxin Risk Score (ARS)

```
ARS = (Moisture Risk × 0.5) + (Pathogen Risk × 0.35) + 
      (EC Risk × 0.15)
```

**Interpretation:**
- **0-20:** Low risk ✅
- **20-40:** Medium risk 🟡
- **40-60:** High risk 🔴
- **>60:** Critical risk ⛔

---

## 📊 Generated Outputs

### Visualizations (PNG, 300 DPI)

1. **temporal_analysis.png** - Time series of all quality metrics
2. **quality_parameters.png** - Comprehensive parameter analysis
3. **model_performance.png** - Prediction accuracy charts

### Data Files (CSV)

1. **airs_gseed_summary.csv** - Summary statistics
2. **airs_gseed_full_analysis.csv** - Complete dataset with SHI/ARS

---

## 💡 Use Cases

- 🔬 **Research:** Seed quality assessment studies
- 🌾 **Agriculture:** Storage condition monitoring
- 📊 **Quality Control:** Seed batch evaluation
- 🎓 **Education:** Data science teaching tool
- 💼 **Consulting:** Client seed quality reports

---

## 📖 Documentation

Comprehensive documentation available in the [`docs/`](docs/) folder:

- **[HOW_TO_RUN_IN_COLAB.md](docs/HOW_TO_RUN_IN_COLAB.md)** - Google Colab setup (3 steps)
- **[CUSTOM_DATASET_RESULTS.md](docs/CUSTOM_DATASET_RESULTS.md)** - Detailed findings & insights
- **[CUSTOM_DATASET_USAGE.md](docs/CUSTOM_DATASET_USAGE.md)** - Python script usage
- **[JUPYTER_NOTEBOOK_CREATED.md](docs/JUPYTER_NOTEBOOK_CREATED.md)** - Notebook features
- **[QUICK_START_CUSTOM_DATASET.txt](QUICK_START_CUSTOM_DATASET.txt)** - Quick reference
- **[COMPLETE_PACKAGE_SUMMARY.txt](COMPLETE_PACKAGE_SUMMARY.txt)** - Full overview

---

## 🎓 Citation

If you use this framework, please cite:

```bibtex
@software{airsgseed2026,
  title={AIRS-GSeed: AI-Driven Framework for Groundnut Seed Quality Assessment},
  author={AIRS-GSeed Team},
  year={2026},
  url={https://github.com/dhayarajas/kavi-seed}
}
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

---

## 📄 License

This project is available for research and educational purposes.

---

## 📞 Contact

For questions or collaborations:
- **Repository:** [github.com/dhayarajas/kavi-seed](https://github.com/dhayarajas/kavi-seed)
- **Issues:** [github.com/dhayarajas/kavi-seed/issues](https://github.com/dhayarajas/kavi-seed/issues)

---

## 🌟 Highlights

✅ **Self-Contained Notebook** - No external file uploads needed  
✅ **One-Click Execution** - Works in free Google Colab  
✅ **Real Data Analysis** - Custom 3-month groundnut seed dataset  
✅ **Professional Outputs** - Publication-ready charts and tables  
✅ **Comprehensive Docs** - 7 detailed documentation files  
✅ **Proven Results** - Detected 20.8% quality decline and medium aflatoxin risk  

---

## 📅 Version History

- **v1.0** (February 2026) - Initial release
  - Self-contained Jupyter notebook
  - Custom dataset integration
  - Complete documentation
  - Google Colab support

---

**Ready to analyze your seed quality data? Get started with the Jupyter notebook!** 🚀

[Open in Colab](https://colab.research.google.com/) | [Read Documentation](docs/HOW_TO_RUN_IN_COLAB.md) | [View Results](docs/CUSTOM_DATASET_RESULTS.md)
