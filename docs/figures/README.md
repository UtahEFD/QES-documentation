Command to compile and crop figures:
```
pdflatex figures.tex; for i in $(seq 1 $(qpdf --show-npages figures.pdf)); do qpdf figures.pdf --pages figures.pdf $i -- output/out$i.pdf; pdfcrop output/out$i.pdf; rm out$i.pdf; done
```
Once the figuures are renamed and moved to final, they can be converted to png with folloging command:
```
for f in *.pdf; do pdftocairo -png -r 300 -singlefile $f "${f%.*}"; done
```