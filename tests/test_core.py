import tempfile
from pathlib import Path

from marquisatoll_9l_kit.core import Marquisatoll9lTool


def test_summarize_numeric_column():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, "a.csv")
        path.write_text("x,y\n1,2\n3,4\n", encoding="utf-8")
        stats = Marquisatoll9lTool().summarize(path)
        assert stats["x"]["n"] == 2 and stats["x"]["mean"] == 2.0


def test_missing_file_returns_empty():
    assert Marquisatoll9lTool().summarize("/no/such.csv") == {}


def test_skips_non_numeric_rows():
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp, "b.csv")
        path.write_text("x\n1\nnot-a-number\n", encoding="utf-8")
        assert Marquisatoll9lTool().summarize(path)["x"]["n"] == 1
