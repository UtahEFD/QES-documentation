Template for the Read the Docs tutorial
=======================================

This GitHub template includes fictional Python library
with some basic Sphinx docs.

Read the tutorial here:

https://docs.readthedocs.io/en/stable/tutorial/


Require pandoc:

```
for f in *.tex;
do pandoc $f -f latex -t rst --lua-filter latex-cite.lua -o ${f/tex/rst}
done
```
