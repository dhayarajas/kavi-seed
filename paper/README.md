# AIRS-GSeed Research Paper

This folder contains all files related to the AIRS-GSeed research manuscript.

---

## 📄 Main Files

| File | Description |
|------|-------------|
| `paper.tex` | Main LaTeX manuscript source |
| `references.bib` | Bibliography in BibTeX format |
| `paper.pdf` | Compiled manuscript (PDF) |

---

## 🖼️ Figures

### `figures/` folder
- `architecture.png` - System architecture diagram

### `images/` folder
Contains 8 visualization figures for the manuscript:

1. `architecture.png` - AIRS-GSeed framework architecture
2. `ablation_study.png` - Component contribution analysis
3. `ars_temporal.png` - Temporal ARS prediction
4. `canopy_performance.png` - Canopy stress detection results
5. `comparative_analysis_heatmap.png` - Comparative performance heatmap
6. `gaps_addressed.png` - Research gaps visualization
7. `seed_health_results.png` - SHI prediction results
8. `581408db-5691-4e23-b2bd-e88ba5148cbf.png` - Additional figure

### Root level
- `novel_contributions.png` - Novel contributions diagram

---

## 🔨 Compilation

To compile the LaTeX manuscript:

```bash
cd paper
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

---

## 📊 Auxiliary Files

The following files are auto-generated during LaTeX compilation:

- `paper.aux` - Auxiliary file for cross-references
- `paper.log` - Compilation log
- `paper.out` - PDF outline/bookmarks

These files are not tracked in git (see `.gitignore`).

---

## 📝 Manuscript Details

**Title:** AIRS-GSeed: AI-Driven Framework for Groundnut Seed Quality Assessment and Aflatoxin Risk Prediction Using Multi-Modal Remote Sensing

**Format:** IEEE Conference/Journal format

**Sections:**
- Abstract
- Introduction
- Related Work
- Methodology
- Results and Discussion
- Conclusion
- References

---

## 🎨 Figure Guidelines

All figures follow IEEE manuscript standards:
- **Resolution:** 300 DPI minimum
- **Format:** PNG (for compatibility)
- **Size:** Optimized for publication
- **Captions:** Included in LaTeX source

---

## 📚 References

The bibliography (`references.bib`) includes:
- Peer-reviewed journal articles
- Conference papers
- Technical reports
- Limited web sources and preprints (following reviewer guidelines)

All references formatted according to IEEE citation style.

---

## 🔄 Version Control

This folder is tracked in the git repository at:
https://github.com/dhayarajas/kavi-seed

**Structure:**
```
paper/
├── paper.tex                  # Main LaTeX source
├── references.bib             # Bibliography
├── paper.pdf                  # Compiled PDF
├── figures/                   # Architecture diagrams
│   └── architecture.png
├── images/                    # Result visualizations
│   ├── ablation_study.png
│   ├── ars_temporal.png
│   ├── canopy_performance.png
│   ├── comparative_analysis_heatmap.png
│   ├── gaps_addressed.png
│   ├── seed_health_results.png
│   ├── architecture.png
│   └── 581408db-5691-4e23-b2bd-e88ba5148cbf.png
├── novel_contributions.png    # Contributions diagram
├── paper.aux                  # LaTeX auxiliary (not tracked)
├── paper.log                  # Compilation log (not tracked)
└── paper.out                  # PDF bookmarks (not tracked)
```

---

## 📖 Related Documentation

For framework implementation and analysis:
- See `../docs/` for comprehensive documentation
- See `../Codebase/AIRS-GSeet/` for source code
- See `../Custom-Dataset/` for real data used in validation

---

## ✏️ Editing Guidelines

When modifying the manuscript:

1. **Edit** `paper.tex` for content changes
2. **Update** `references.bib` for citation additions
3. **Recompile** using the commands above
4. **Verify** all figures are properly referenced
5. **Commit** changes with descriptive message

---

## 🎯 Submission Checklist

Before submitting to a journal/conference:

- [ ] All sections complete and proofread
- [ ] All figures referenced in text
- [ ] All citations numbered sequentially
- [ ] References follow IEEE format
- [ ] Abstract within word limit (typically 200-250 words)
- [ ] PDF compiles without errors
- [ ] Figures are high resolution (300+ DPI)
- [ ] Author information complete
- [ ] Keywords included
- [ ] Acknowledgments (if applicable)

---

## 📧 Contact

For questions about the manuscript, please refer to the main repository README.

---

**Last Updated:** February 8, 2026
