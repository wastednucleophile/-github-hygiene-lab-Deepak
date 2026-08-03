# Lab 2 — GitHub: Remote, Push, Clone (15 minutes)

**Goal:** get your own copy of this project onto GitHub under your account, and prove you can pull it back down.

---

## Part A — Create your own repository (5 min)

1. Go to https://github.com → **New repository**
2. Name: `github-hygiene-lab-<yourname>`
3. Visibility: **Public** (so your trainer and peers can review your PR)
4. **Do NOT** tick "Add a README", "Add .gitignore", or "Choose a license"
   → we already have those locally, and pre-filling causes an unrelated-histories conflict
5. **Create repository**

Copy the HTTPS URL GitHub shows you. It looks like:
`https://github.com/<you>/github-hygiene-lab-<yourname>.git`

---

## Part B — Connect your local folder to it (5 min)

```bash
git remote -v                # currently points at the trainer's repo
git remote rename origin upstream
git remote add origin https://github.com/<you>/github-hygiene-lab-<yourname>.git
git remote -v
```

You now have two remotes:
- `upstream` → the trainer's original repo (read from it)
- `origin` → your own repo (write to it)

Push:
```bash
git branch                   # confirm you are on main
git push -u origin main
```

**Authentication:** GitHub will not accept your account password.
When prompted for a password, paste a **Personal Access Token**:

> GitHub → your avatar → Settings → Developer settings → Personal access tokens →
> Tokens (classic) → Generate new token → scope: **repo** → Generate → **copy it now**, it is shown once.

Paste the token as the password. Username is your GitHub username.

`-u` sets the upstream tracking branch, so future pushes are just `git push`.

Refresh your GitHub page. Your code is there.

---

## Part C — Prove a clone works (5 min)

Go **outside** your project folder and clone your own repo fresh:

```bash
cd ..
git clone https://github.com/<you>/github-hygiene-lab-<yourname>.git verify-copy
cd verify-copy
ls -a
```

Answer these two questions:

1. Is `.env` present in the clone? **Why / why not?**
2. Is `.git` present? What does that folder contain?

Then delete the verify copy and go back to your working folder:
```bash
cd ..
rm -rf verify-copy      # Windows PowerShell: Remove-Item -Recurse -Force verify-copy
cd github-code-hygiene-lab
```

---

## Part D — The pull habit

```bash
git pull origin main
```
Nothing to pull yet — but build the habit now: **pull before you start work, push when you finish.**
90% of merge pain comes from skipping the pull.

---

## Checkpoint — you are done when

- [ ] Your GitHub repo page shows `src/`, `tests/`, `README.md`
- [ ] `.env` is **not** visible on GitHub
- [ ] `git remote -v` shows both `origin` (yours) and `upstream` (trainer's)
- [ ] You can explain what `-u` did in `git push -u origin main`

---

## Commands you just used

`git remote -v` · `git remote add` · `git remote rename` · `git push -u origin main` · `git clone` · `git pull`
