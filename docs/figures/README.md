Command to compile and crop figures:
```
pdflatex figures.tex; for i in $(seq 1 $(qpdf --show-npages figures.pdf)); do qpdf figures.pdf --pages figures.pdf $i -- out$i.pdf; pdfcrop out$i.pdf; rm out$i.pdf; done
```
