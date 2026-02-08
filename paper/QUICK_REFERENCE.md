# LaTeX Quick Reference for AIRS-GSeed Paper

## Quick Patterns

### Units and Numbers
```latex
% Single values
\SI{89.2}{\percent}
\SI{730}{\nano\meter}
\SI{25}{\celsius}
\SI{5}{\minute}

% Ranges
\SIrange{400}{2500}{\nano\meter}
\SIrange{5}{10}{\centi\meter}
\SIrange{-40}{85}{\celsius}

% In text
The accuracy is \SI{89.2}{\percent}.
Wavelength range: \SIrange{400}{2500}{\nano\meter}.
```

### Mathematical Notation
```latex
% Operators (roman, not italic)
\mathrm{Softmax}(...)
\mathrm{CNN}(...)
\mathrm{LSTM}(...)

% Subscripts (text labels)
\mathbf{I}_{\text{RGB}}
\mathbf{f}_{\text{CNN}}
\theta_{\text{soil}}

% Equations with labels
\begin{equation}
y = mx + b,
\label{eq:line}
\end{equation}
%
where $m$ is slope...
```

### References
```latex
% Figures
Fig.~\ref{fig:arch}
Figure~\ref{fig:arch}  % At sentence start

% Tables
Table~\ref{tab:results}

% Equations
Equation~\eqref{eq:loss} or~\eqref{eq:loss}

% Sections
Section~\ref{sec:intro}

% Citations
as shown in~\cite{paper1,paper2}
```

### Tables
```latex
\begin{table}[!t]
\renewcommand{\arraystretch}{1.3}
\caption{Caption Above Table}
\label{tab:name}
\centering
\begin{tabular}{lcc}
\toprule
\textbf{Method} & \textbf{Metric 1} & \textbf{Metric 2} \\
 & (\si{\percent}) & (units) \\
\midrule
Proposed & \textbf{89.2} & \textbf{9.8} \\
Baseline & 80.7 & 12.5 \\
\bottomrule
\end{tabular}
\end{table}
```

### Figures
```latex
\begin{figure}[!t]
\centering
\includegraphics[width=0.48\textwidth]{filename}
\caption{Caption below figure.}
\label{fig:name}
\end{figure}
```

### Chemical Formulas
```latex
\ce{CO2}
\ce{H2O}
\ce{CH4}
```

### Custom Commands
```latex
\airsgseed  % AIRS-GSeed
\shi        % SHI
\ars        % ARS
```

### Common Symbols
```latex
% Multiplication
$640 \times 512$

% Range/dash
0--100 scale

% R-squared
$R^2$

% Approximately
$\approx$

% Less/greater than
$<$, $>$, $\leq$, $\geq$
```

## Common Mistakes to Avoid

❌ `5-10 cm` → ✅ `\SIrange{5}{10}{\centi\meter}`
❌ `89.2%` → ✅ `\SI{89.2}{\percent}`
❌ `R2` → ✅ `$R^2$`
❌ `$\text{Softmax}$` → ✅ `$\mathrm{Softmax}$`
❌ `$I_{RGB}$` → ✅ `$I_{\text{RGB}}$`
❌ `Fig. \ref{...}` → ✅ `Fig.~\ref{...}`

## Compilation

```bash
# Full build
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex

# Or with latexmk
latexmk -pdf paper.tex

# Clean
latexmk -c
```
