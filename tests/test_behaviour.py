"""Behaviour lock: these numbers must NOT change while you refactor.

This is your safety net. Run `pytest -q` before you start, after every
commit, and before you push. Green tests = your refactor preserved behaviour.

You MAY rename anything inside messy_tracker.py -- if you rename the entry
point, update the import here too. That is a legitimate part of the refactor.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from expense_tracker.messy_tracker import main_report  # noqa: E402

DATA = str(Path(__file__).resolve().parents[1] / "data" / "expenses_sample.csv")


def test_row_count():
    assert main_report(DATA)["count"] == 10


def test_total_with_tax():
    assert main_report(DATA)["total_with_tax"] == 52045.10


def test_self_paid_with_tax():
    assert main_report(DATA)["self_paid_with_tax"] == 29802.04


def test_category_breakdown():
    cats = main_report(DATA)["by_category"]
    assert cats == {
        "travel": 21810.0,
        "food": 2411.25,
        "software": 15200.0,
        "training": 5500.0,
    }


def test_flagged_count():
    assert main_report(DATA)["flagged"] == 2
