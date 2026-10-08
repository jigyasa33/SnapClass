import py_compile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_all_python_files_compile():
    """Koi bhi .py file me syntax error ho to test fail ho jayega."""
    files = [
        f for f in ROOT.rglob("*.py")
        if "venv" not in f.parts and ".git" not in f.parts
    ]
    assert files, "Koi python file nahi mili"
    for f in files:
        py_compile.compile(str(f), doraise=True)


def test_requirements_file_exists():
    assert (ROOT / "requirements.txt").exists()


def test_app_entry_exists():
    assert (ROOT / "app.py").exists()