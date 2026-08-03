# GitHub & Code Hygiene Lab

A deliberately messy Python project used to learn Git, GitHub, and code hygiene by fixing real problems.

**You will:** run the code, break it, branch it, conflict it, clean it, and ship it via a Pull Request.

---

## 1. Setup (10 minutes, do this first)

### Check what you already have
```bash
git --version
python --version
code --version
```
All three must print a version. If `git` fails, install from https://git-scm.com/downloads

### One-time Git identity
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
git config --list
```

### Get the code
```bash
git clone <REPO_URL_SHARED_IN_CHAT>
cd github-code-hygiene-lab
code .
```

### Python environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Verify everything works
```bash
python -m pytest -q
```
Expected: `5 passed`

If you see 5 passing tests, you are ready.

### VS Code extensions (install from the Extensions panel)
- **Python** (Microsoft)
- **GitLens**
- **Ruff** (Astral Software)

---

## 2. What's in here

```
github-code-hygiene-lab/
├── src/expense_tracker/
│   └── messy_tracker.py      <- the code you will clean up
├── tests/
│   └── test_behaviour.py     <- your safety net. Must stay green.
├── data/
│   └── expenses_sample.csv   <- input data
├── config/
│   └── settings.py           <- used for the merge conflict lab
├── exercises/                <- Labs 1, 2, 3 (during the session)
├── ASSIGNMENT.md             <- your take-home work
├── CHEATSHEET.md             <- every command from today
├── .gitignore                <- what Git must never track
└── .env.example              <- how secrets are supposed to be handled
```

Run the program:
```bash
python src/expense_tracker/messy_tracker.py
```

---

## 3. Session flow

| Time | What |
|---|---|
| 2:30 – 4:00 | Learning + Labs 1, 2, 3 |
| 4:00 – 4:15 | Break |
| 4:15 – 5:00 | Live demos: merge conflicts, hygiene pass, PR review |
| 5:00 – 7:00 | `ASSIGNMENT.md` — self-paced, submit a PR |

---

## 4. The golden rule of this repo

> **The tests define the behaviour. You may change every line of code, but `pytest` must stay green.**

That is what refactoring means: changing how code looks and reads, without changing what it does.
