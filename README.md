# QES documentation

Link to the documentation: https://qes-documentation.readthedocs.io/en/latest/

### Template for the Read the Docs tutorial

This GitHub template includes fictional Python library with some basic 
Sphinx docs.

Read the tutorial here: https://docs.readthedocs.io/en/stable/tutorial/

The main documentation: https://docs.readthedocs.io/en/stable/index.html

### Documentation

Latex can be used to write the QES documentation, but rst (reStructuredText) 
is used by readthedoc. So we will use pandoc (https://pandoc.org, use brew or
other package tool to install) to convert latex sources. 

Here are a few rules to follow when writing latex sources:
* do not change index.rst (main file)
* do not modifed the *.rst directly, changes will be overwritten by pandoc
* add new reference in refs.bib
* no references (figures, equations, or sections)
* no floating element (figure will be placed exactly where they are in the text)
* for inline code use: `\verb|..|`; for code block use: `\begin{verbatim} .. \end{verbatim}`
* no spaces in `\cite{..}` (use `\cite{..}` only)
* if the structure of the document is changed (files), the changes need to be made to index.rst

Run pandoc to convert latex to rst :
```
for f in *.tex;
do pandoc $f -f latex -t rst --lua-filter latex-cite.lua -o ${f/tex/rst}
done
```

