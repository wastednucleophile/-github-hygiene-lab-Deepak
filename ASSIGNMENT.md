# Assignment — Clean Up and Ship It

**Submit:** one Pull Request URL, posted in the session chat.
**Pace:** yours. Everything you need is in this file and `CHEATSHEET.md`.

Stuck for more than 10 minutes? Post the exact error in the chat and move to the next task.

---

## The brief

`src/expense_tracker/messy_tracker.py` works. It also breaks most of the fifteen rules from the session.

Your job: **make it clean without changing what it does.**

```
The tests are the contract. pytest must be green at every commit.
```

Run this before you start, and after every change:
```bash
python -m pytest -q      # expected: 5 passed
```

---

## Step 0 — Branch off

```bash
git switch main
git pull origin main
git switch -c refactor/code-hygiene-<yourname>
```

Never work on `main`.

---

## The 5 tasks — one commit each

**Five separate commits, not one at the end.** Your commit history is part of the grade.

---

### Task 1 — Get the secrets out · `chore:`

1. Copy `.env.example` to `.env`, put the two values in it
2. Delete `API_KEY` and `DB_PASSWORD` from `messy_tracker.py`
3. Load them properly instead:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   API_KEY = os.getenv("API_KEY")
   ```
4. Confirm `git status` does **not** offer to commit `.env`

```bash
git commit -am "chore: move credentials out of source into environment variables"
```

**Answer in your PR description:** if that key had been real, why is deleting it in a later commit not enough?

---

### Task 2 — Make the names say what they mean · `refactor:`

| Current | Problem | Fix to something like |
|---|---|---|
| `L()` | single capital letter | `load_expenses()` |
| `calc()` | calculate *what*? | `calculate_total_with_tax()` |
| `calc2()` | never number a name | `calculate_self_paid_total()` |
| `addExpense()` | camelCase is Java | `add_expense()` |
| `l1`, `t`, `r`, `e`, `f`, `c`, `n`, `x` | unreadable | real words |
| dict keys `"d"`, `"c"`, `"a"`, `"p"` | unreadable | `"date"`, `"category"`, `"amount"`, `"paid_by"` |
| `data` (global) | meaningless + global state | delete it entirely |

If you rename `main_report`, update the import in `tests/test_behaviour.py` too. That is allowed and expected.

```bash
python -m pytest -q
git commit -am "refactor: rename functions and variables to intent-revealing names"
```

---

### Task 3 — Kill the magic numbers · `refactor:`

Pull `1.18`, `1.12`, `1.05`, `5000` into named constants at the top:

```python
GST_RATE_HIGH_VALUE = 1.18
GST_RATE_TRAVEL_STANDARD = 1.05
GST_RATE_DEFAULT = 1.12
HIGH_VALUE_THRESHOLD_INR = 5000
```

```bash
git commit -am "refactor: replace magic numbers with named constants"
```

---

### Task 4 — Delete the duplication · `refactor:`

`calc()` and `calc2()` contain the same tax logic, copy-pasted.

1. Extract the per-row tax calculation into one function, e.g. `tax_for(row) -> float`
2. Have both totals call it — the only real difference between them is a filter on `paid_by`
3. Flatten the nesting while you're there: use `continue` guard clauses instead of four levels of `if`

Target: neither function longer than ~8 lines.

```bash
python -m pytest -q
git commit -am "refactor: extract shared tax calculation and remove duplicate logic"
```

---

### Task 5 — Fix the traps and tidy up · `fix:`

1. **Mutable default** — `def addExpense(e, store=[])` → `store: list | None = None`, create it inside
2. **Bare `except:`** → `except (ValueError, TypeError, KeyError):`
3. **`!= None` / `== True`** → `is not None`, and just `if value:`
4. **File never closed** → `with open(path, newline="", encoding="utf-8") as fh:`
5. **Delete dead code** — the commented-out `old_report` block and the `# TODO`
6. **Delete unused imports** — `sys`, `json`, `math`, `datetime`, and the `from datetime import *` wildcard

Then let the tools finish it:
```bash
ruff check --fix src/
black src/
python -m pytest -q
git commit -am "fix: remove traps, dead code and unused imports"
```

---

## Step 6 — Ship the Pull Request

```bash
python -m pytest -q
ruff check src/
git push -u origin refactor/code-hygiene-<yourname>
```

On GitHub → **Compare & pull request**
- Base `main` ← Compare your branch
- Title: `refactor: code hygiene pass on expense tracker`
- Fill in the template completely
- **Read your own diff, file by file, before you click Create**

Post the PR URL in the chat.

---

## Step 7 — Review one peer's PR

Pick the PR posted just before yours. Leave **two** comments:
- one on a specific line, from the **Files changed** tab
- one overall: what they did well, and one thing you'd change

Comment on the code, never on the person.

---

## Stretch goals (only if you finish early)

- **S1** — add type hints and a one-line docstring to every function
- **S2** — split `messy_tracker.py` into `loader.py`, `calculator.py`, `report.py`. Keep tests green.
- **S3** — add a test for a row with a negative amount and one with a blank category. Does it handle them? If it crashes, that's a real finding — write it up in your PR.

---

## How this is graded

| Weight | What |
|---|---|
| 30% | Tests green, program still runs |
| 25% | Five meaningful commits with correct `type:` prefixes |
| 25% | Naming and structure readable by someone who has never seen the file |
| 10% | No secrets in the diff, `.env` correctly ignored |
| 10% | PR description filled in + one peer review left |

---

## If you get stuck

```bash
git status                 # 90% of Git confusion ends here
git restore <file>         # throw away uncommitted changes
git stash                  # park your mess, come back to it
git log --oneline          # where am I in history
```

Broke it completely? Your commits are safe. Post the error in chat and start the next task.
