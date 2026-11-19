# marquisatoll-9l-kit

Summarize numeric CSV columns (n / min / max / mean).

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m marquisatoll_9l_kit.cli --help
```

```python
from marquisatoll_9l_kit.core import Marquisatoll9lTool

tool = Marquisatoll9lTool()
print(tool)
```

## Layout

```
marquisatoll_9l_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 marquisatoll-9l
