# IEEE Submission Checklist - AIRS-GSeed Paper

## Quick Status
✅ **IEEE STANDARDS COMPLIANT** - Ready for review submission

---

## Files Overview

| File | Purpose | Status |
|------|---------|--------|
| `paper.tex` | Main manuscript | ✅ IEEE compliant |
| `references.bib` | Bibliography | ✅ Ready |
| `figures/architecture.png` | System architecture | ✅ Included |
| `images/*.png` | Results figures | ✅ Included |
| `IEEE_COMPLIANCE_NOTES.md` | Compliance documentation | ✅ Created |

---

## Pre-Submission Steps

### 1. Compile the Paper
```bash
cd /Users/dhaya/Kavitha-Agri/paper
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

Or use latexmk:
```bash
latexmk -pdf paper.tex
```

### 2. Check Output
- [ ] Open `paper.pdf`
- [ ] Verify all figures appear correctly
- [ ] Check all equations are properly formatted
- [ ] Ensure all citations resolve correctly
- [ ] Verify page layout is correct

### 3. Final Quality Checks
- [ ] All figures are at least 300 DPI
- [ ] No compilation errors or warnings
- [ ] Abstract is 150-250 words
- [ ] All acronyms defined on first use
- [ ] All symbols defined in equations

---

## For Anonymous Review Submission

### Current Status ✅
- [x] Author information anonymized
- [x] Affiliations removed
- [x] Acknowledgments use placeholders

### Already Configured
```latex
\author{Anonymous Authors for Review}
```

---

## For Final Camera-Ready Submission

### Update Author Information
Replace this:
```latex
\author{Anonymous Authors for Review}
```

With actual authors:
```latex
\author{
    \IEEEauthorblockN{First A. Author\IEEEauthorrefmark{1},
    Second B. Author\IEEEauthorrefmark{2}, and
    Third C. Author\IEEEauthorrefmark{1}}
    \IEEEauthorblockA{\IEEEauthorrefmark{1}Department Name,
    University Name,
    City, Country\\
    Email: author1@email.com}
    \IEEEauthorblockA{\IEEEauthorrefmark{2}Institute Name,
    Organization,
    City, Country\\
    Email: author2@email.com}
}
```

### Add Biographies (End of Paper)
Before `\end{document}`, add:
```latex
\begin{IEEEbiography}[{\includegraphics[width=1in,height=1.25in,clip,keepaspectratio]{photo1}}]{First A. Author}
Biography text here...
\end{IEEEbiography}

\begin{IEEEbiography}[{\includegraphics[width=1in,height=1.25in,clip,keepaspectratio]{photo2}}]{Second B. Author}
Biography text here...
\end{IEEEbiography}
```

### Update Acknowledgments
Replace:
```latex
The authors thank... This work was supported by [Funding Agency] under Grant [Number].
```

With actual funding information:
```latex
The authors thank... This work was supported by [Actual Agency Name] under Grant [Actual Grant Number].
```

### Comment Out Override
```latex
% \IEEEoverridecommandlockouts  % Comment out for final submission
```

---

## IEEE Transactions Specific Requirements

### For IEEE Transactions on Geoscience and Remote Sensing

1. **Page Limit**
   - Regular papers: typically 13-15 pages
   - Check current journal guidelines

2. **Figure Quality**
   - Minimum 300 DPI for photos/raster images
   - Vector graphics (PDF/EPS) preferred
   - Color figures: check if additional fees apply

3. **Supplementary Materials**
   - Code/datasets can be submitted separately
   - Include data availability statement

4. **Copyright Form**
   - Complete IEEE e-Copyright form upon acceptance
   - Submit before final paper deadline

---

## Common Issues to Check

### Before Submission
- [ ] No overfull/underfull hbox warnings
- [ ] All cross-references work (no ?? in PDF)
- [ ] All citations numbered correctly
- [ ] Figure labels are legible
- [ ] Table fonts are readable
- [ ] Equations don't overflow margins
- [ ] Consistent terminology throughout
- [ ] All abbreviations in abstract are defined

### LaTeX Specific
- [ ] No `\\ ` in paragraphs (use blank line instead)
- [ ] Proper `~` for non-breaking spaces
- [ ] Math symbols in `$...$` or equation environments
- [ ] Figures use `[!t]` or `[!b]` placement
- [ ] Large tables/figures use `*` for two-column span

---

## File Preparation for Submission

### Required Files
1. `paper.tex` - Main LaTeX source
2. `references.bib` - Bibliography file
3. `figures/` - All figure files
4. `images/` - All image files
5. `paper.pdf` - Compiled PDF

### Optional Files
- `README.txt` - Compilation instructions
- Source files for complex figures

### Create Submission Package
```bash
cd /Users/dhaya/Kavitha-Agri/paper
zip -r AIRS-GSeed-submission.zip paper.tex references.bib figures/ images/ paper.pdf
```

---

## Submission Platforms

### IEEE Manuscript Central
1. Create account at: https://mc.manuscriptcentral.com/tgrs-ieee
2. Start new submission
3. Upload files:
   - Main document (PDF)
   - Source files (ZIP with .tex, .bib, figures)
4. Enter metadata (title, abstract, keywords, authors)
5. Suggest reviewers (if requested)
6. Submit

### After Submission
- Track status in Manuscript Central
- Respond to reviewer comments if revisions requested
- Submit revised manuscript with point-by-point response

---

## Timeline Expectations

| Stage | Typical Duration |
|-------|-----------------|
| Initial Review | 1-2 weeks |
| Peer Review | 2-4 months |
| Revisions | 4-6 weeks |
| Final Decision | 1-2 weeks |
| Publication | 1-2 months |

**Total**: Approximately 6-9 months from submission to publication

---

## Contact Information

### IEEE Support
- Author support: https://journals.ieeeauthorcenter.ieee.org/
- Technical support: supportcenter@ieee.org

### Journal Specific
- IEEE TGRS: Check journal website for editor contacts
- Manuscript Central help: mc-tgrs-help@ieee.org

---

## Quick Reference: Common LaTeX Commands

### Figures
```latex
\begin{figure}[!t]
\centering
\includegraphics[width=0.48\textwidth]{filename}
\caption{Caption text here.}
\label{fig:label}
\end{figure}
```

### Tables
```latex
\begin{table}[!t]
\caption{Table caption here}
\label{tab:label}
\centering
\begin{tabular}{lcc}
\toprule
Header1 & Header2 & Header3 \\
\midrule
Data & Data & Data \\
\bottomrule
\end{tabular}
\end{table}
```

### Equations
```latex
\begin{equation}
E = mc^2
\label{eq:einstein}
\end{equation}
```

### Citations
```latex
Recent work \cite{ref1,ref2} shows...
As shown in \cite{ref3}...
```

---

## Status: ✅ READY FOR SUBMISSION

Your paper is IEEE compliant and ready for review submission to IEEE Transactions on Geoscience and Remote Sensing.
