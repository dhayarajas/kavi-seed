# Compilation and Verification Guide

## Step-by-Step Compilation

### 1. Navigate to Paper Directory
```bash
cd /Users/dhaya/Kavitha-Agri/paper
```

### 2. Clean Previous Builds (Optional)
```bash
rm -f paper.aux paper.bbl paper.blg paper.log paper.out paper.pdf
```

### 3. Compile the Paper
```bash
# Step 1: First LaTeX pass
pdflatex paper.tex

# Step 2: Generate bibliography
bibtex paper

# Step 3: Second LaTeX pass (resolve citations)
pdflatex paper.tex

# Step 4: Third LaTeX pass (resolve references)
pdflatex paper.tex
```

### Alternative: Use latexmk (Recommended)
```bash
# Automatic compilation with dependency tracking
latexmk -pdf paper.tex

# Clean auxiliary files
latexmk -c

# Clean everything including PDF
latexmk -C
```

---

## Verification Checklist

### ✅ Compilation Success
- [ ] No errors during compilation
- [ ] PDF generated successfully
- [ ] All passes completed without fatal errors

### ✅ Warnings Check
```bash
# Check for warnings
pdflatex paper.tex 2>&1 | grep -i "warning"

# Check for common issues
pdflatex paper.tex 2>&1 | grep -E "Overfull|Underfull|undefined"
```

**Common Warnings to Fix**:
- Overfull hbox: Line too wide (adjust text)
- Underfull hbox: Line too narrow (usually OK)
- Undefined references: Run pdflatex again
- Citation undefined: Run bibtex then pdflatex twice

### ✅ Visual Verification

Open the PDF and check:

#### Title Page
- [ ] Title appears correctly
- [ ] Author line shows "Anonymous Authors for Review"
- [ ] Running header shows journal name
- [ ] Abstract is present and formatted
- [ ] Keywords are listed

#### Sections
- [ ] All section numbers appear
- [ ] Subsection numbering is correct
- [ ] No orphaned headings at bottom of pages

#### Figures
- [ ] All figures appear
- [ ] Figure numbers are sequential
- [ ] Captions are below figures
- [ ] Images are clear (not pixelated)
- [ ] All figures referenced in text

#### Tables
- [ ] All tables appear
- [ ] Table numbers are sequential
- [ ] Captions are above tables
- [ ] All tables referenced in text
- [ ] No vertical lines (booktabs style)

#### Equations
- [ ] All equations display correctly
- [ ] Equation numbers appear
- [ ] No equations overflow margins
- [ ] All math symbols render properly

#### References
- [ ] All citations appear as [1], [2], etc.
- [ ] No question marks (??) in citations
- [ ] Bibliography appears at end
- [ ] All references formatted correctly

#### Cross-References
- [ ] All Fig.~X references work (no ??)
- [ ] All Table~X references work
- [ ] All Equation references work
- [ ] All Section references work

---

## Common Issues and Solutions

### Issue: "Undefined references"
**Solution**: Run pdflatex one more time
```bash
pdflatex paper.tex
```

### Issue: "Citation undefined"
**Solution**: Run bibtex, then pdflatex twice
```bash
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

### Issue: "Package X not found"
**Solution**: Install missing package
```bash
# For Ubuntu/Debian
sudo apt-get install texlive-science  # for siunitx
sudo apt-get install texlive-latex-extra  # for IEEEtran

# For macOS with MacTeX
# Packages should be included, try updating:
sudo tlmgr update --self
sudo tlmgr update --all
```

### Issue: "File not found" for figures
**Solution**: Check graphicspath and file names
```latex
% In preamble
\graphicspath{{figures/}{results/}{images/}}
```

### Issue: Overfull hbox warnings
**Solution**: 
1. Adjust text to fit within margins
2. Use `\linebreak` to suggest line breaks
3. Add words to hyphenation list
4. Rephrase sentences

---

## Quality Checks

### Check 1: All Units Use siunitx
```bash
# Search for bare percentages
grep -n "\\d\\+%" paper.tex

# Should use: \SI{X}{\percent}
```

### Check 2: Math Operators in Roman
```bash
# Check for \text{} in operators
grep -n "\\text{Softmax\|CNN\|LSTM" paper.tex

# Should use: \mathrm{} instead
```

### Check 3: Subscripts for Labels
```bash
# Check for italic subscripts
grep -n "_[A-Z]" paper.tex | grep -v "\\text{"

# Labels should use: _{\text{LABEL}}
```

### Check 4: Non-breaking Spaces
```bash
# Check for missing non-breaking spaces
grep -n "Fig\\. \\\\ref\|Table \\\\ref" paper.tex

# Should use: Fig.~\ref or Table~\ref
```

---

## File Size Check

### Check PDF Size
```bash
ls -lh paper.pdf
```

**Typical Sizes**:
- Small (< 1 MB): Mostly text, few images
- Medium (1-5 MB): Normal paper with several figures
- Large (> 5 MB): Many high-res images

**If too large**:
- Compress images
- Convert to vector graphics (PDF/EPS)
- Reduce image resolution

---

## Metadata Verification

### Check PDF Properties
```bash
# On macOS
mdls paper.pdf | grep -i "title\|author\|subject"

# On Linux
pdfinfo paper.pdf
```

Should show:
- Title: AIRS-GSeed: AI-Driven Groundnut Seed Health Assessment
- Author: Anonymous Authors
- Subject: Remote Sensing, Machine Learning, Agriculture

---

## Pre-Submission Final Checks

### Content Verification
- [ ] Abstract is 150-250 words
- [ ] All acronyms defined on first use
- [ ] All figures have clear captions
- [ ] All tables have clear captions
- [ ] All equations have punctuation
- [ ] All equations are numbered
- [ ] All references are cited
- [ ] Acknowledgments updated (if final version)

### Formatting Verification
- [ ] Two-column layout (IEEE standard)
- [ ] Correct page margins
- [ ] Font size appropriate
- [ ] Line spacing correct
- [ ] No pages exceed limit

### Technical Verification
- [ ] All math renders correctly
- [ ] All symbols display properly
- [ ] All units formatted with siunitx
- [ ] All chemical formulas use mhchem
- [ ] Hyperlinks work (internal)

---

## Automated Checking Script

### Create Check Script
```bash
#!/bin/bash
# save as check_paper.sh

echo "=== Compiling Paper ==="
pdflatex paper.tex > /dev/null
bibtex paper > /dev/null
pdflatex paper.tex > /dev/null
pdflatex paper.tex

echo ""
echo "=== Checking for Issues ==="
echo "Errors:"
grep -i "error" paper.log | head -5

echo ""
echo "Critical Warnings:"
grep -E "Overfull.*hbox|undefined.*reference|citation.*undefined" paper.log

echo ""
echo "=== PDF Generated ==="
ls -lh paper.pdf

echo ""
echo "=== Page Count ==="
pdfinfo paper.pdf | grep Pages
```

### Run Check Script
```bash
chmod +x check_paper.sh
./check_paper.sh
```

---

## Success Criteria

Your paper is ready when:
- ✅ Compiles without errors
- ✅ PDF generates successfully
- ✅ All figures appear
- ✅ All tables appear
- ✅ All citations work
- ✅ All cross-references work
- ✅ No undefined references
- ✅ Minimal warnings
- ✅ Meets page limits
- ✅ Follows IEEE format

---

## Quick Compile Command

```bash
# One-liner for quick compilation
cd /Users/dhaya/Kavitha-Agri/paper && \
pdflatex paper.tex && \
bibtex paper && \
pdflatex paper.tex && \
pdflatex paper.tex && \
open paper.pdf  # Opens PDF on macOS
```

---

## Final Steps

1. **Compile**: Run full compilation sequence
2. **Check**: Verify all checklist items
3. **Review**: Read through entire PDF
4. **Share**: Send to co-authors for review
5. **Revise**: Make any necessary changes
6. **Recompile**: After changes
7. **Submit**: Upload to journal system

---

## Support

If you encounter issues:
1. Check this guide first
2. Review LATEX_BEST_PRACTICES.md
3. Check LaTeX error messages carefully
4. Search for specific error online
5. Check package documentation

**Common Help Resources**:
- TeX StackExchange: https://tex.stackexchange.com/
- IEEEtran documentation
- siunitx manual
- LaTeX WikiBook

---

## Status: Ready to Compile! ✅

Your paper follows all best practices and should compile successfully.
