"""Smoke test for the project.

WHY: Verify that Python can find the project package
     and that its source files compile successfully.
"""

import importlib.util
from pathlib import Path


def test_project_runs() -> None:
    """Verify the NLP package exists and its Python files compile."""
    spec = importlib.util.find_spec("nlp")
    assert spec is not None
    assert spec.submodule_search_locations is not None

    package_dir = Path(next(iter(spec.submodule_search_locations)))
    source_files = list(package_dir.rglob("*.py"))

    assert source_files, "No Python source files found."

    for path in source_files:
        compile(path.read_bytes(), str(path), "exec")
