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

### Editing workflow

To edit the documentation sources:
* Use git as normal: clone/update/pull the repo to your machine,
* Edit the .tex files in `docs/source`, you can compile the latex sources into a pdf using the main.tex `in docs/latex`, figures need to be place in `doc/figures`. 
* PAY ATTENTION TO RULES ABOVE otherwise the conversion to rst will not work.
* run pandoc to convert the .tex the .rst (see command above).
* then commit/push as normal.

To update the Read-the-Doc:
* on the build page, select build the latest
* check that the webpage was updated correlcty (some times, changes can take a few minutes to take effect)

### Previewing documentation in VS Code

The [Esbonio](https://marketplace.visualstudio.com/items?itemName=swyddfa.esbonio)
VS Code extension provides a live Sphinx preview for the ``.rst`` files in this
repository. It builds the entire documentation project, so cross-references,
citation roles, themes, and images render as they do in the published docs.

1. Install Python 3.11 or later. Python can be downloaded from
   [python.org](https://www.python.org/downloads/). On macOS with Homebrew, run
   ``brew install python@3.11``.
2. Clone this repository and open its root folder in VS Code.
3. Create and activate a virtual environment, then install the documentation
   dependencies:

   ```sh
   python3.11 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   python -m pip install -r docs/requirements.txt
   ```

   On Windows PowerShell, activate the environment with:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

4. In VS Code, install the **Esbonio** extension from the Extensions view.
   Esbonio is installed as a VS Code extension; no separate ``pip install
   esbonio`` is required.
5. Select ``.venv`` with **Python: Select Interpreter**, then run **Esbonio:
   Restart Language Server** and **Esbonio: Restart Sphinx Process** from the
   Command Palette.
6. Open an ``.rst`` file, save it, and launch **Esbonio: Preview Documentation
   in Split Window** (or press ``Ctrl+K V``). The preview may take a few seconds
   to appear after the first Sphinx build.

This repository's ``pyproject.toml`` configures Esbonio to use ``.venv``, build
from ``docs/source``, and write HTML output to ``docs/build``. If previewing
does not start, confirm that VS Code was opened at the repository root rather
than at ``docs`` or ``docs/source``.

Note:
* When releasing a new version of QES, the relase number needs to be updated. The release is 'definitive' ie documentation of the relase number (ex v2.1.0) will not changes anymore. This need to be synced with public release of QES. 

