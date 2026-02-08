# Bibliography Compilation Guide

## Overview

The paper now uses BibTeX for bibliography management. The bibliography file `references.bib` contains all citations referenced in the paper.

## Bibliography Contents

### 10 Comparative Papers
1. **paper1_adaptive_clustering**: Adaptive Clustering for UAV Hyperspectral Data
2. **paper2_apple_disease**: Low-Cost UAV Pipeline for Apple Disease
3. **paper3_intelligent_agri**: Intelligent Agriculture Review
4. **paper4_recent_advances**: Recent Advances in Plant Disease Detection
5. **paper5_evolution_dl**: Evolution of DL in UAV Agriculture
6. **paper6_rice_disease**: Rice Leaf Disease Detection
7. **paper7_pest_mapping**: Pest Infestation Mapping
8. **paper8_ai_assisted**: AI-Assisted Early Detection
9. **paper9_dl_cv_review**: DL & CV Review
10. **paper10_hyperspectral**: Hyperspectral Advances

### Additional References
- **ref_uav_disease**: UAV-based crop disease detection
- **ref_multispectral_agri**: Multispectral imaging for agriculture
- **ref_hyperspectral_seed**: Hyperspectral seed analysis
- **ref_aflatoxin_prediction**: Aflatoxin prediction models
- **ref_multimodal_fusion**: Multi-modal data fusion
- **ref_physics_informed**: Physics-informed neural networks
- **ref_vision_transformer**: Vision Transformer paper
- **ref_shap**: SHAP explainability
- **ref_groundnut_aflatoxin**: Groundnut aflatoxin review
- **ref_precision_agri**: Precision agriculture review

## Compilation Instructions

### Standard LaTeX + BibTeX Compilation

To compile the paper with bibliography, run these commands in sequence:

```bash
# Step 1: Compile LaTeX (first pass)
pdflatex paper.tex

# Step 2: Run BibTeX to process bibliography
bibtex paper

# Step 3: Compile LaTeX again (second pass - includes citations)
pdflatex paper.tex

# Step 4: Compile LaTeX again (third pass - resolves all references)
pdflatex paper.tex
```

### Using LaTeX Compilation Tools

#### Overleaf
1. Upload both `paper.tex` and `references.bib` to Overleaf
2. Click "Recompile" - Overleaf handles BibTeX automatically

#### TeXstudio / TeXmaker
1. Open `paper.tex`
2. Use "Build & View" - the IDE handles BibTeX automatically

#### Command Line (Linux/Mac)
```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

#### Command Line (Windows)
```cmd
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

## Citation Keys Used in Paper

The following citation keys are used throughout the paper:

### In Introduction Section:
- `ref_groundnut_aflatoxin`
- `paper1_adaptive_clustering`, `paper2_apple_disease`, `paper6_rice_disease`
- `paper4_recent_advances`, `paper9_dl_cv_review`
- `ref_hyperspectral_seed`, `paper10_hyperspectral`
- `ref_aflatoxin_prediction`
- `ref_uav_disease`, `paper3_intelligent_agri`, `paper5_evolution_dl`
- `paper7_pest_mapping`

### In Related Work Section:
- `ref_uav_disease`, `paper3_intelligent_agri`, `paper6_rice_disease`
- `paper1_adaptive_clustering`, `paper2_apple_disease`
- `ref_hyperspectral_seed`, `paper10_hyperspectral`, `paper8_ai_assisted`
- `ref_aflatoxin_prediction`, `ref_groundnut_aflatoxin`
- `ref_multimodal_fusion`, `paper5_evolution_dl`

### In Methodology Section:
- `ref_vision_transformer`
- `ref_physics_informed`
- `ref_shap`

## Troubleshooting

### Issue: Citations show as [?]
**Solution**: Run BibTeX and then compile LaTeX twice more:
```bash
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

### Issue: Bibliography not appearing
**Solution**: Check that `references.bib` is in the same directory as `paper.tex`

### Issue: Undefined citation warnings
**Solution**: Verify the citation key exists in `references.bib` and matches exactly (case-sensitive)

### Issue: Bibliography formatting issues
**Solution**: The paper uses `IEEEtran` bibliography style. Ensure you have the IEEEtran class files.

## Updating References

To add new references:

1. Add entry to `references.bib` with a unique key
2. Use `\cite{key}` in `paper.tex` where needed
3. Recompile using the 4-step process above

## Bibliography Style

The paper uses `IEEEtran` bibliography style, which is standard for IEEE journals. This is specified in the paper with:
```latex
\bibliographystyle{IEEEtran}
\bibliography{references}
```

## Notes

- All 10 comparative papers are included in the bibliography
- Additional supporting references are included for completeness
- Citation keys follow a consistent naming convention
- URLs and DOIs are included where available
- The bibliography is formatted for IEEE journal standards
