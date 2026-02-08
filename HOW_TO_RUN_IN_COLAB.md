# How to Run AIRS-GSeed Analysis in Google Colab

This guide shows you how to run the AIRS-GSeed seed quality analysis in Google Colab without needing any external files.

---

## 🚀 Quick Start (3 Steps)

### Step 1: Upload Notebook to Google Colab

**Option A: Direct Upload**
1. Go to [Google Colab](https://colab.research.google.com/)
2. Click **File → Upload notebook**
3. Select: `AIRS_GSeed_Custom_Dataset_Analysis.ipynb`
4. Wait for upload to complete

**Option B: From Google Drive**
1. Upload the notebook to your Google Drive
2. Right-click the file
3. Select **Open with → Google Colaboratory**

**Option C: From GitHub** *(if you have the notebook in a GitHub repository)*
1. Go to [Google Colab](https://colab.research.google.com/)
2. Click **File → Open notebook**
3. Select **GitHub** tab
4. Enter repository URL
5. Select the notebook

---

### Step 2: Run All Cells

Once the notebook is open in Colab:

1. Click **Runtime → Run all** in the menu
   - OR use keyboard shortcut: `Ctrl+F9` (Windows/Linux) or `Cmd+F9` (Mac)

2. The notebook will:
   - ✅ Install required packages automatically
   - ✅ Load the embedded dataset (no file upload needed!)
   - ✅ Calculate SHI and ARS metrics
   - ✅ Generate all visualizations
   - ✅ Create summary statistics
   - ✅ Prepare downloadable files

3. Wait for all cells to complete (approximately 1-2 minutes)

---

### Step 3: Download Results

After all cells have run:

1. Scroll to the last cell (Step 9)
2. Click the download prompts that appear
3. Save the following files to your computer:
   - `airs_gseed_summary.csv` - Summary statistics
   - `airs_gseed_full_analysis.csv` - Complete dataset with SHI/ARS
   - `temporal_analysis.png` - Time series charts
   - `quality_parameters.png` - Detailed parameter analysis
   - `model_performance.png` - Prediction accuracy charts

**Alternative Download Method:**
- Click the folder icon 📁 in the left sidebar
- Right-click any file
- Select "Download"

---

## 📊 What You'll Get

### Visualizations (PNG Images)

1. **temporal_analysis.png**
   - Germination trends over 3 months
   - Vigour index changes
   - Seed Health Index (SHI) trajectory
   - Aflatoxin Risk Score (ARS) progression

2. **quality_parameters.png**
   - Root & shoot growth comparison
   - Pod & seed weight analysis
   - Moisture content monitoring
   - Electrical conductivity trends
   - Pathogen infestation levels
   - Multi-parameter heatmap

3. **model_performance.png**
   - SHI prediction accuracy (R² score)
   - ARS prediction accuracy (R² score)
   - Comparison with actual values

### Data Files (CSV)

1. **airs_gseed_summary.csv**
   - Key metrics comparison (Initial vs Month 2)
   - Percentage changes
   - Quick reference table

2. **airs_gseed_full_analysis.csv**
   - Complete dataset
   - All calculated metrics (SHI, ARS)
   - Quality status and risk levels
   - All measurement parameters

---

## 🎯 Understanding Your Results

### Seed Health Index (SHI)

Your notebook will show SHI values for each time point:

```
SHI = (Germination × 0.4) + (Vigour × 0.3) + 
      (Moisture × 0.15) + (Pathogen-free × 0.15)
```

**Interpretation:**
- **80-100:** ✅ Excellent - No action needed
- **70-80:** 🟢 Good - Monitor regularly
- **60-70:** 🟡 Fair - Consider intervention
- **<60:** 🔴 Poor - Immediate action required

### Aflatoxin Risk Score (ARS)

```
ARS = (Moisture Risk × 0.5) + (Pathogen Risk × 0.35) + 
      (EC Risk × 0.15)
```

**Interpretation:**
- **0-20:** ✅ Low risk - Continue monitoring
- **20-40:** 🟡 Medium risk - Take preventive measures
- **40-60:** 🔴 High risk - Intervention needed
- **>60:** ⛔ Critical - Urgent action required

---

## 💡 Tips for Using in Colab

### Running Individual Cells

Instead of running all cells at once, you can run them one by one:
- Click on a cell
- Press `Shift + Enter` to run and move to next cell
- OR click the ▶️ play button on the left side of the cell

### Viewing Larger Images

If charts are too small:
1. Right-click on any image
2. Select "Open image in new tab"
3. View full-resolution chart

### Modifying the Data

To analyze different seed quality data:

1. Find **Step 2** in the notebook
2. Modify the data dictionary with your own measurements:

```python
data = {
    'Month': ['Your-Month-1', 'Your-Month-2', 'Your-Month-3'],
    'Germination (%)': [YOUR_VALUE_1, YOUR_VALUE_2, YOUR_VALUE_3],
    'Vigour index': [YOUR_VALUE_1, YOUR_VALUE_2, YOUR_VALUE_3],
    # ... update all parameters
}
```

3. Re-run all cells to see updated analysis

### Saving Your Work

To save your Colab notebook with results:
1. Click **File → Save a copy in Drive**
2. Your notebook will be saved to Google Drive
3. You can access it anytime from Drive

---

## 🔧 Troubleshooting

### "Module not found" Error

**Solution:** The notebook automatically installs packages. If you see this error:
1. Manually run the first code cell (Step 1)
2. Wait for installation to complete
3. Then run remaining cells

### Charts Not Displaying

**Solution:**
1. Make sure you're running cells in order (top to bottom)
2. Check that Step 1 (package installation) completed successfully
3. Try **Runtime → Restart and run all**

### Download Not Working

**Solution:**
1. Check your browser's download settings
2. Allow pop-ups for colab.research.google.com
3. Alternative: Use the folder icon 📁 to manually download files

### Slow Performance

**Solution:**
1. Go to **Runtime → Change runtime type**
2. Select "GPU" or "TPU" (though not necessary for this notebook)
3. Or simply wait - the notebook typically completes in 1-2 minutes

---

## 📱 Using on Mobile/Tablet

While Google Colab works on mobile browsers, it's recommended to use a desktop/laptop for:
- Better visualization viewing
- Easier file downloads
- More comfortable code editing

If using mobile:
1. Use landscape orientation
2. Zoom in on charts for better viewing
3. Downloads will go to your device's download folder

---

## 🆘 Need Help?

### Common Questions

**Q: Do I need to upload my Excel file?**  
A: No! The dataset is embedded in the notebook. No external files needed.

**Q: Can I use my own data?**  
A: Yes! Edit the data dictionary in Step 2 with your measurements.

**Q: Will my analysis be saved?**  
A: Charts and CSVs are generated each time you run the notebook. Download them to keep permanently.

**Q: Can I share my results?**  
A: Yes! Download the files and share the CSVs/images, or share your saved Colab notebook.

**Q: Do I need to pay for Colab?**  
A: No! The free tier is sufficient for this notebook.

---

## ✅ Checklist for Success

Before running:
- [ ] Notebook uploaded to Google Colab
- [ ] Connected to a runtime (automatic when you open the notebook)

While running:
- [ ] All cells executed in order
- [ ] No error messages in output
- [ ] All charts displayed successfully

After running:
- [ ] Downloaded all 5 files (3 PNGs + 2 CSVs)
- [ ] Reviewed visualizations for trends
- [ ] Checked summary statistics
- [ ] Noted any warnings or recommendations

---

## 🔄 Updating with New Measurements

When you collect new seed quality data:

1. Open your saved Colab notebook
2. Go to Step 2
3. Add new data points to the dictionary:

```python
data = {
    'Month': ['Sep-2025', 'Oct-2025', 'Nov-2025', 'Dec-2025'],  # Added Dec
    'Germination (%)': [91, 85, 81, 78],  # Added new value
    # ... add values for all other parameters
}
```

4. Run all cells again
5. Download updated results

---

## 📞 Support Resources

**Documentation:**
- Full analysis interpretation: See notebook's "How to Interpret Results" section
- AIRS-GSeed framework: Read the embedded markdown cells

**Files in This Package:**
- `AIRS_GSeed_Custom_Dataset_Analysis.ipynb` - Main notebook
- `CUSTOM_DATASET_RESULTS.md` - Detailed findings explanation
- `CUSTOM_DATASET_USAGE.md` - Advanced usage guide
- `README.md` - Project overview

---

## 🎓 Learning Resources

To learn more about Jupyter notebooks and Google Colab:
- [Google Colab Guide](https://colab.research.google.com/notebooks/intro.ipynb)
- [Jupyter Notebook Basics](https://jupyter.org/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

---

## 🌟 Features of This Notebook

✅ **Self-Contained** - No external files needed  
✅ **One-Click Run** - Execute all analysis automatically  
✅ **Professional Visualizations** - Publication-ready charts  
✅ **Downloadable Results** - Take your analysis with you  
✅ **Fully Documented** - Every step explained  
✅ **Customizable** - Easy to modify for your data  
✅ **Free to Use** - No software purchase required  

---

**Ready to analyze your seed quality data? Upload the notebook to Colab and click "Run all"!**

---

**Created:** February 2026  
**Compatible with:** Google Colab (Free & Pro)  
**Runtime:** Python 3  
**Average Execution Time:** 1-2 minutes
