"""Launcher for the Streamlit dashboard notebook.

Streamlit only runs raw ``.py`` files, so this module executes the code cells
of ``Streamlit working - Commented.ipynb`` inside Streamlit's script context.

Edit the notebook; run:

    uv run streamlit run app.py

Two caveats worth knowing:

* The notebook is not runnable in Jupyter on its own — the ``st.*`` calls need
  Streamlit's server runtime.
* Streamlit watches ``app.py``, not the notebook, so editing the notebook needs
  a manual **Rerun** (or a restart) to show up.
"""

from __future__ import annotations

import json
from pathlib import Path

NOTEBOOK = Path(__file__).with_name("Streamlit working - Commented.ipynb")


def run_notebook(path: Path) -> None:
    """Execute every code cell of ``path`` in this module's namespace."""
    notebook = json.loads(path.read_text(encoding="utf-8"))

    for cell in notebook["cells"]:
        if cell["cell_type"] != "code":
            continue
        source = "".join(cell["source"])
        exec(compile(source, str(path), "exec"), globals())


if __name__ == "__main__":
    run_notebook(NOTEBOOK)
