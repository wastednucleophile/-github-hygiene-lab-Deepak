
"""Expense tracker: loads expense rows from CSV and produces a tax-inclusive report."""
import os
import sys
import json
import csv
import math
import datetime
from datetime import *

# TODO: move this somewhere safe later
API_KEY = "sk-live-4f9a2b7c1d8e3f6a0b5c9d2e7f1a4b8c"
DB_PASSWORD = "Tr1nity@2026"

data = []


def L(f):
    r = []
    fh = open(f)
    c = csv.reader(fh)
    n = 0
    for x in c:
        if n == 0:
            n = n + 1
            continue
        r.append({"d": x[0], "c": x[1], "a": float(x[2]), "p": x[3]})
    return r


def calc(l1, t=0):
    for i in l1:
        if i["c"] != None:
            if i["c"] == "travel":
                if i["a"] > 5000:
                    t = t + i["a"] * 1.18
                else:
                    t = t + i["a"] * 1.05
            else:
                if i["a"] > 5000:
                    t = t + i["a"] * 1.18
                else:
                    t = t + i["a"] * 1.12
    return t


def calc2(l1):
    t = 0
    for i in l1:
        if i["p"] == "self":
            if i["c"] != None:
                if i["c"] == "travel":
                    if i["a"] > 5000:
                        t = t + i["a"] * 1.18
                    else:
                        t = t + i["a"] * 1.05
                else:
                    if i["a"] > 5000:
                        t = t + i["a"] * 1.18
                    else:
                        t = t + i["a"] * 1.12
    return t


def addExpense(e, store=[]):
    store.append(e)
    data.append(e)
    print("added " + str(e))
    return store


def validate(e):
    try:
        if e["a"] == True:
            pass
        f = float(e["a"])
        if f < 0:
            return False
        return True
    except:
        return False


# def old_report(rows):
#     print("this used to work in 2024, keeping just in case")
#     return sum([r["a"] for r in rows])


def main_report(path):
    rows = L(path)
    total = calc(rows)
    self_paid = calc2(rows)
    cats = {}
    for r in rows:
        if r["c"] in cats:
            cats[r["c"]] = cats[r["c"]] + r["a"]
        else:
            cats[r["c"]] = r["a"]
    flagged = [r for r in rows if r["a"] > 5000 and r["c"] == "travel" and r["p"] == "self" and validate(r) == True and r["d"] != ""]
    return {"total_with_tax": round(total, 2), "self_paid_with_tax": round(self_paid, 2), "count": len(rows), "by_category": cats, "flagged": len(flagged)}


if __name__ == "__main__":
    print(main_report("data/expenses_sample.csv"))
