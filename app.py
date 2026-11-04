"""Launcher for the Streamlit dashboard notebook.
Streamlit only runs .py files, so we create a combined notebook with each cell and execute that instead

uv run streamlit run app.py

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
