# Lab 3 — Branching and Merging (12 minutes)

**Goal:** never commit directly to `main` again.

---

## Why branches exist

`main` is what ships. A branch is a **safe sandbox** with its own history that you can throw away if it goes wrong. In every real team, you touch `main` only through a reviewed Pull Request.

Naming convention (use this all week):
```
feature/<short-description>     feature/add-currency-column
fix/<short-description>         fix/negative-amount-crash
chore/<short-description>       chore/update-readme
```
Lowercase, hyphens, no spaces, no `final`, no `final2`, no your-name-only branches.

---

## Steps

### 1. Create and switch
```bash
git switch -c feature/add-file-header
git branch
```
The `*` shows your current branch. `git switch -c` = create + switch in one step.
(You will also see the older syntax `git checkout -b` — same thing.)

### 2. Do work on the branch
In `src/expense_tracker/messy_tracker.py`, replace the top-of-file comment with a proper module docstring:

```python
"""Expense tracker: loads expense rows from CSV and produces a tax-inclusive report."""
```

Verify nothing broke, then commit:
```bash
python -m pytest -q
git add -A
git commit -m "docs: add module docstring to tracker"
```

### 3. Prove the branch is isolated
```bash
git switch main
```
Now open the file in VS Code. **Your docstring is gone.** That is correct — it lives on the branch.
```bash
git switch feature/add-file-header
```
It's back.

### 4. Merge into main
```bash
git switch main
git merge feature/add-file-header
git log --oneline --graph --all
```

Read the merge message. Because `main` had no new commits, Git did a **fast-forward** — it just moved the pointer. No merge commit was needed.

### 5. Clean up and push
```bash
git branch -d feature/add-file-header
git branch
git push origin main
```

Delete branches after merging. A repo with 40 stale branches is a repo nobody trusts.

### 6. Bonus — see history as a graph
```bash
git log --oneline --graph --all --decorate
```
In VS Code, open the **GitLens** panel and look at the same graph visually.

---

## Checkpoint — you are done when

- [ ] `git branch` shows only `main`
- [ ] `git log --oneline` shows your docstring commit
- [ ] GitHub shows the docstring in the file
- [ ] You can explain what "fast-forward" meant in step 4

---

## Commands you just used

`git switch -c` · `git switch` · `git branch` · `git merge` · `git branch -d` · `git log --graph`
