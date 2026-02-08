# LaTeX Best Practices Applied to AIRS-GSeed Paper

## Summary
The manuscript has been updated to follow comprehensive LaTeX and IEEE best practices for high-quality scientific publication.

---

## 1. Package Management Best Practices ✅

### Package Loading Order
```latex
% Core packages first
\usepackage{cite}
\usepackage{amsmath,amssymb,amsfonts}
...
% Hyperref MUST be loaded LAST
\usepackage[options]{hyperref}
```

**✅ Applied**: 
- Moved `hyperref` to the end of package list
- Added proper hyperref configuration for print-friendly output
- Added metadata (pdftitle, pdfauthor, etc.)

### New Packages Added
1. **siunitx** - Proper SI unit formatting
2. **mhchem** - Chemical formulas (\ce{CO2})

---

## 2. Mathematical Notation Best Practices ✅

### Operators in Roman (Not Italic)
**Bad**: `$\text{Softmax}$`
**Good**: `$\mathrm{Softmax}$` or `\DeclareMathOperator`

**✅ Applied**:
```latex
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator*{\argmin}{arg\,min}
\DeclareMathOperator{\softmax}{softmax}
\DeclareMathOperator{\sigmoid}{sigmoid}
```

### Subscripts for Text
**Bad**: `$\mathbf{I}_{RGB}$` (italic subscript)
**Good**: `$\mathbf{I}_{\text{RGB}}$` (roman subscript for labels)

**✅ Applied**: All text subscripts now use `\text{}`

### Equation Formatting
**Best Practices**:
1. Add labels to all equations: `\label{eq:name}`
2. Add punctuation (comma/period) at end of equations
3. Add `%` after equations to prevent extra spacing
4. Define all variables after first use

**✅ Applied**:
```latex
\begin{equation}
P(y|\mathbf{I}) = \mathrm{Softmax}(...),
\label{eq:cnn_vit}
\end{equation}
%
where $\mathbf{I} = ...$ is the input.
```

### R² Notation
**Bad**: `R²` or `R2`
**Good**: `$R^2$`

**✅ Applied**: All instances now use proper superscript

---

## 3. Units and Numbers Best Practices ✅

### Using siunitx Package

**Bad**:
- `6.2% VWC`
- `730 nm`
- `-40°C to 85°C`
- `5-10 cm`

**Good**:
- `\SI{6.2}{\percent} VWC`
- `\SI{730}{\nano\meter}`
- `\SIrange{-40}{85}{\celsius}`
- `\SIrange{5}{10}{\centi\meter}`

**✅ Applied Throughout**:
```latex
% Single values
\SI{89.2}{\percent}
\SI{730}{\nano\meter}

% Ranges
\SIrange{400}{2500}{\nano\meter}
\SIrange{1}{3}{\centi\meter}

% In tables (unit in header)
\begin{tabular}{lc}
\toprule
\textbf{Metric} & \textbf{Value} \\
 & (\si{\percent}) \\
\midrule
Accuracy & 89.2 \\
\end{tabular}
```

### Benefits:
- Consistent spacing between number and unit
- Automatic line-break prevention
- Easy unit conversion if needed
- Professional appearance

---

## 4. Table Formatting Best Practices ✅

### IEEE Table Guidelines

**✅ Applied**:
1. **Caption above table** (IEEE standard)
2. **Use booktabs** (`\toprule`, `\midrule`, `\bottomrule`)
3. **No vertical lines**
4. **Units in column headers** (not in each cell)
5. **Consistent decimal places**
6. **Bold for best results**

**Example**:
```latex
\begin{table}[!t]
\renewcommand{\arraystretch}{1.3}
\caption{Performance Metrics}
\label{tab:performance}
\centering
\begin{tabular}{lcc}
\toprule
\textbf{Method} & \textbf{Accuracy} & \textbf{RMSE} \\
 & (\si{\percent}) & (points) \\
\midrule
Proposed & \textbf{89.2} & \textbf{9.8} \\
Baseline & 80.7 & 12.5 \\
\bottomrule
\end{tabular}
\end{table}
```

---

## 5. Figure Best Practices ✅

### Current Implementation

**✅ Applied**:
```latex
\begin{figure}[!t]  % [!t] = top of page preferred
\centering
\includegraphics[width=0.48\textwidth]{filename}
\caption{Caption goes here.}  % Caption BELOW figure
\label{fig:name}  % Label AFTER caption
\end{figure}
```

### Best Practices:
1. **Caption below figures** (IEEE standard)
2. **Use vector graphics** (PDF/EPS) when possible
3. **0.48\textwidth** for single-column figures
4. **\textwidth** for two-column spanning figures
5. **Reference before appearance**: Mention Fig.~\ref{...} before figure appears

---

## 6. Custom Commands for Consistency ✅

### Defined Commands

**✅ Applied**:
```latex
% Model names
\newcommand{\airsgseed}{AIRS-GSeed}
\newcommand{\shi}{SHI}
\newcommand{\ars}{ARS}

% Abbreviations
\newcommand{\ie}{i.e.\@\xspace}
\newcommand{\eg}{e.g.\@\xspace}
\newcommand{\etal}{et~al.\@\xspace}

% Vector notation
\renewcommand{\vec}[1]{\mathbf{#1}}
```

### Benefits:
- **Consistency**: All instances identical
- **Easy updates**: Change once, affects everywhere
- **Proper spacing**: `\@` prevents extra space after periods

---

## 7. Citation Best Practices ✅

### IEEE Citation Style

**✅ Current**:
```latex
\usepackage{cite}
\bibliographystyle{IEEEtran}
\bibliography{references}
```

**Best Practices**:
1. **Multiple citations**: `\cite{ref1,ref2,ref3}`
2. **Non-breaking space**: `as shown in~\cite{ref1}`
3. **Sort citations**: cite package does this automatically
4. **Compress ranges**: [1]-[3] becomes [1--3]

**Example**:
```latex
% Good
Recent work~\cite{paper1,paper2,paper3} shows...

% Bad
Recent work \cite{paper1}, \cite{paper2}, \cite{paper3} shows...
```

---

## 8. Typography Best Practices ✅

### Spacing

**✅ Applied**:
1. **Non-breaking space** `~` before citations and references
2. **En-dash** `--` for ranges (0--100)
3. **Em-dash** `---` for interruption
4. **Proper spacing** after periods in abbreviations

```latex
% Figures
Fig.~\ref{fig:arch}  % Non-breaking space

% Ranges  
0--100 scale  % En-dash, no spaces

% Abbreviations
i.e.\@ properly  % Correct spacing after period
```

### Special Characters

**✅ Applied**:
```latex
% Degree symbol (with siunitx)
\SI{25}{\celsius}

% Multiplication
$640 \times 512$  % Use \times not ×

% Chemical formulas (with mhchem)
\ce{CO2}
```

---

## 9. Algorithm Formatting Best Practices ✅

### Current Implementation

**✅ Applied**:
```latex
\begin{algorithm}[!t]
\caption{Algorithm Name}
\label{alg:name}
\begin{algorithmic}[1]  % Line numbers
\REQUIRE Input requirements
\ENSURE Output guarantees
\STATE Step 1
\IF{condition}
    \STATE Step 2
\ENDIF
\RETURN result
\end{algorithmic}
\end{algorithm}
```

**Best Practices**:
1. Use `\REQUIRE` and `\ENSURE` (not Input/Output)
2. Number lines with `[1]` parameter
3. Use proper capitalization: `\STATE`, `\IF`, `\FOR`
4. Mathematical notation in `$...$`

---

## 10. Acronyms and Abbreviations ✅

### First Use Definition

**Best Practice**: Define on first use
```latex
unmanned aerial vehicle (UAV)  % First use
...
UAV flights...  % Subsequent uses
```

**✅ Applied**: All acronyms defined on first appearance

### Common Abbreviations

**Defined**:
- UAV: Unmanned Aerial Vehicle
- CNN: Convolutional Neural Network
- ViT: Vision Transformer
- PINN: Physics-Informed Neural Network
- SHI: Seed Health Index
- ARS: Aflatoxin Risk Score
- LSTM: Long Short-Term Memory
- MLP: Multi-Layer Perceptron

---

## 11. Reference Formatting Best Practices ✅

### Cross-References

**Best Practices**:
```latex
% Figures
Fig.~\ref{fig:arch}  % Abbreviated with capital F
Figure~\ref{fig:arch}  % Full word (sentence start)

% Tables
Table~\ref{tab:results}  % Always capitalize

% Equations
Equation~\eqref{eq:loss} or simply~\eqref{eq:loss}

% Sections
Section~\ref{sec:intro}

% Algorithms
Algorithm~\ref{alg:main}
```

**✅ Applied**: All cross-references use non-breaking space `~`

---

## 12. Hyphenation Control ✅

### Custom Hyphenation

**✅ Applied**:
```latex
\hyphenation{op-tical net-works semi-conduc-tor 
             ground-nut aflatoxin hyper-spectral multi-modal}
```

Prevents awkward line breaks in technical terms.

---

## 13. Hyperref Configuration ✅

### Print-Friendly Settings

**✅ Applied**:
```latex
\hypersetup{
    colorlinks=true,
    linkcolor=black,  % Black for printing
    citecolor=black,
    filecolor=black,
    urlcolor=black
}
```

### Metadata

**✅ Applied**:
```latex
\usepackage[pdftitle={...},
            pdfauthor={...},
            pdfkeywords={...}]{hyperref}
```

Benefits:
- Searchable PDF metadata
- Better accessibility
- Professional appearance

---

## 14. Spacing Best Practices ✅

### After Equations

**✅ Applied**:
```latex
\begin{equation}
y = mx + b,
\label{eq:line}
\end{equation}
%  <-- Percent sign prevents extra space
where $m$ is...
```

### Around Floats

**IEEE Standard**:
```latex
\begin{figure}[!t]  % Prefer top of page
\begin{table}[!t]   % Prefer top of page
```

---

## 15. Code Organization Best Practices ✅

### File Structure

**✅ Current Organization**:
```
paper/
├── paper.tex                    # Main document
├── references.bib               # Bibliography
├── figures/                     # Vector graphics
│   └── architecture.png
├── images/                      # Raster images
│   ├── canopy_performance.png
│   └── ...
├── IEEE_COMPLIANCE_NOTES.md     # IEEE standards
├── SUBMISSION_CHECKLIST.md      # Submission guide
└── LATEX_BEST_PRACTICES.md      # This file
```

### Section Organization

**✅ Applied**: Clear comments delineating sections
```latex
% *** INTRODUCTION ***
\section{Introduction}
...

% *** METHODOLOGY ***
\section{Methodology}
...
```

---

## 16. Chemical Formulas Best Practices ✅

### Using mhchem Package

**✅ Applied**:
```latex
\usepackage[version=4]{mhchem}

% Usage
\ce{CO2}     % Carbon dioxide
\ce{H2O}     % Water
\ce{^{14}C}  % Isotopes
```

---

## 17. Common Mistakes AVOIDED ✅

### ❌ What NOT to Do

1. **Don't**: `$RGB$` for labels
   **Do**: `RGB` or `\text{RGB}` in math mode

2. **Don't**: `5-10 cm` (hyphen for range)
   **Do**: `\SIrange{5}{10}{\centi\meter}` or `5--10~cm`

3. **Don't**: Multiple spaces for alignment
   **Do**: Use proper LaTeX environments

4. **Don't**: `\\` for line breaks in paragraphs
   **Do**: Blank line for new paragraph

5. **Don't**: Inconsistent capitalization in headings
   **Do**: Follow IEEE style (Title Case for sections)

6. **Don't**: Hardcode values that appear multiple times
   **Do**: Define commands for consistency

---

## 18. IEEE-Specific Best Practices ✅

### Document Class Options

**✅ Applied**:
```latex
\documentclass[journal]{IEEEtran}
\IEEEoverridecommandlockouts  % For review
```

### Title and Authors

**✅ Applied**:
```latex
\title{Full Title Here}
\author{Anonymous Authors for Review}
\markboth{Journal Name}{Authors: Short Title}
\IEEEpeerreviewmaketitle  % Not \maketitle
```

### Abstract and Keywords

**✅ Applied**:
```latex
\begin{abstract}
150-250 words...
\end{abstract}

\begin{IEEEkeywords}
keyword1, keyword2, ...
\end{IEEEkeywords}
```

---

## 19. Accessibility Best Practices ✅

### Alt Text and Descriptions

**✅ Applied**: Descriptive captions
```latex
\caption{Canopy stress detection results: 
         (a) RGB image, (b) Ground truth, 
         (c) Prediction, (d) Attention map.}
```

### Hyperref for Navigation

**✅ Applied**: Internal links work for PDF navigation

---

## 20. Quality Checklist ✅

### Pre-Submission Verification

- [x] All equations numbered and labeled
- [x] All figures and tables referenced in text
- [x] Units formatted with siunitx
- [x] R² notation correct ($R^2$)
- [x] Proper subscripts (\text{} for labels)
- [x] Operators in roman (\mathrm{})
- [x] Non-breaking spaces before refs
- [x] Hyperref loaded last
- [x] Chemical formulas with mhchem
- [x] Consistent acronym usage
- [x] Proper hyphenation defined
- [x] Tables use booktabs
- [x] Citations properly formatted
- [x] Bibliography style: IEEEtran
- [x] No compilation warnings

---

## Compilation Instructions

### Recommended Sequence
```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

### Check for Warnings
```bash
pdflatex paper.tex 2>&1 | grep -i "warning\|error"
```

### Clean Build
```bash
latexmk -C          # Clean
latexmk -pdf paper  # Build
```

---

## Benefits of Applied Best Practices

1. **Professional Appearance**: Publication-ready formatting
2. **Consistency**: Uniform notation throughout
3. **Maintainability**: Easy to update and modify
4. **IEEE Compliance**: Meets all journal standards
5. **Accessibility**: Better PDF navigation and metadata
6. **Print-Friendly**: Black hyperlinks, proper spacing
7. **Reproducibility**: Clear organization and documentation

---

## Additional Resources

1. **LaTeX Best Practices**
   - https://mirrors.ctan.org/info/l2tabu/english/l2tabuen.pdf

2. **siunitx Package**
   - https://www.ctan.org/pkg/siunitx

3. **IEEE Author Tools**
   - https://template-selector.ieee.org/

4. **Mathematical Writing**
   - Knuth et al., "Mathematical Writing"

---

## Status: ✅ ALL BEST PRACTICES APPLIED

Your manuscript now follows comprehensive LaTeX and IEEE best practices for high-quality scientific publication.
