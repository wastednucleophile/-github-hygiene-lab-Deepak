# Lab 1 — The Local Git Loop (12 minutes)

**Goal:** you should be able to explain what `add` and `commit` actually do, without hand-waving.

---

## The mental model

Git has three places your file can live:

```
  Working Directory  →  Staging Area  →  Repository
   (you edit here)      (git add)        (git commit)
    "my desk"           "the outbox"     "the filing cabinet"
```

`git add` = "include this in the next snapshot"
`git commit` = "take the snapshot, permanently"

---

## Steps

### 1. Where am I?
```bash
git status
git log --oneline
```
`git status` is the single most useful command in Git. Run it after **every** step below.

### 2. Make a change
Open `src/expense_tracker/messy_tracker.py` in VS Code.
At the very top of the file, add a comment with your own name:

```python
# Cleaned up by: <Your Name>
```

### 3. See exactly what changed
```bash
git status
git diff
```
Read the diff. `-` is the old line, `+` is the new line.

### 4. Stage it
```bash
git add src/expense_tracker/messy_tracker.py
git status
```
Notice the file moved from *"Changes not staged"* to *"Changes to be committed"*.

### 5. See the difference between the two diffs
```bash
git diff              # working dir vs staging  -> now empty
git diff --staged     # staging vs last commit  -> shows your change
```

### 6. Commit
```bash
git commit -m "chore: add author comment to tracker module"
git log --oneline
```

### 7. Practise the .gitignore rule
```bash
echo "API_KEY=sk-real-secret-value" > .env
git status
```
**Expected:** Git does *not* offer to track `.env`. Why? Look at `.gitignore` line for `.env`.

Now try to force it and see what protection you have:
```bash
git add .env          # nothing happens
git add -f .env       # DO NOT RUN THIS in real work - shown only so you know it exists
git status
git restore --staged .env
```

### 8. Undo practice
Make a bad change (delete a random line in the file), then:
```bash
git diff
git restore src/expense_tracker/messy_tracker.py   # throw away uncommitted changes
git status
```

---

## Checkpoint — you are done when

- [ ] `git log --oneline` shows your commit at the top
- [ ] `git status` shows a clean tree (except the ignored `.env`)
- [ ] You can say out loud what the difference is between `git diff` and `git diff --staged`

---

## Commands you just used

`git status` · `git log --oneline` · `git diff` · `git diff --staged` · `git add` · `git commit -m` · `git restore` · `git restore --staged`
