# QES documentation

Link to the documentation: https://qes-documentation.readthedocs.io/en/latest/

### Repository layout

```
QES-documentation/
├── docs/
│   ├── source/             # Editable RST pages, Sphinx configuration, bibliography, and published images
│   ├── figures/            # Figure source images and figure-preparation material
│   ├── Makefile            # Local Sphinx build commands (macOS/Linux)
│   ├── make.bat            # Local Sphinx build commands (Windows)
│   └── requirements.txt    # Python dependencies for the documentation build
├── .readthedocs.yaml       # Read the Docs build configuration
├── pyproject.toml          # Project metadata
└── README.md               # Repository overview and contributor workflow
```

Edit documentation pages directly in `docs/source`. Generated files in
`docs/build` are local build output and are not committed.

### Template for the Read the Docs tutorial

This GitHub template includes fictional Python library with some basic 
Sphinx docs.

Read the tutorial here: https://docs.readthedocs.io/en/stable/tutorial/

The main documentation: https://docs.readthedocs.io/en/stable/index.html

### Documentation

The documentation is written directly in reStructuredText (RST). The sources
are in `docs/source`; edit the `.rst` files there directly. Do not use Pandoc
or maintain a parallel LaTeX source.

* Update `docs/source/index.rst` when adding, removing, or reordering pages.
* Add bibliography entries to `docs/source/refs.bib` and cite them with, for
  example, <code>:cite:`key`</code>.
* Store documentation images in `docs/source/Images` and reference them from
  the relevant RST page.
* Build the documentation before committing to catch broken links, citations,
  and image paths.

### Building locally

From the repository root, create a virtual environment and install the
documentation dependencies:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r docs/requirements.txt
```

Build the HTML documentation with:

```sh
make -C docs html
```

Open `docs/build/html/index.html` in a browser to inspect the result. Read the
Docs builds the published HTML documentation and downloadable PDF from these
same RST sources.

To update the Read-the-Doc:
* on the build page, select build the latest
* check that the webpage was updated correlcty (some times, changes can take a few minutes to take effect)

Build the PDG documentation with:

```sh
make -C docs latexpdf
```

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

If previewing does not start, confirm that VS Code was opened at the repository
root and that the selected interpreter is ``.venv/bin/python``.

Note:
* When releasing a new version of QES, the relase number needs to be updated. The release is 'definitive' ie documentation of the relase number (ex v2.1.0) will not changes anymore. This need to be synced with public release of QES. 

