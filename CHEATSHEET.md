# Cheatsheet — Everything From Today

## Setup (once per machine)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --list
```

## The daily loop (95% of your Git usage)
```bash
git status                    # where am I, what changed        <- run this constantly
git pull                      # get teammates' work first
# ... edit files ...
git diff                      # what did I change
git add <file>                # stage it
git add -A                    # stage everything
git commit -m "type: message" # snapshot it
git push                      # send it up
```

## Starting a repo
```bash
git init                      # new repo from an existing folder
git clone <url>               # copy an existing repo down
git clone <url> <foldername>  # ...into a named folder
```

## Remotes
```bash
git remote -v
git remote add origin <url>
git remote rename origin upstream
git push -u origin main       # -u sets tracking, so later just `git push`
```

## History
```bash
git log --oneline
git log --oneline --graph --all --decorate
git show <commit-hash>
git diff --staged
git blame <file>
```

## Branching
```bash
git branch                    # list
git switch -c feature/x       # create + switch      (old: git checkout -b)
git switch main               # switch               (old: git checkout)
git merge feature/x           # merge INTO current branch
git branch -d feature/x       # delete after merge
git push origin feature/x
```

## Merge conflict — the 5 steps
```bash
git merge feature/x           # CONFLICT reported
git status                    # lists conflicted files
# 1. open the file
# 2. decide: yours, theirs, or a combination
# 3. delete ALL of <<<<<<<  =======  >>>>>>>  markers
# 4. run the tests
git add <file>
git commit                    # completes the merge
```
Conflict markers look like:
```
<<<<<<< HEAD
your version (the branch you are ON)
=======
their version (the branch you are MERGING IN)
>>>>>>> feature/x
```
Escape hatch: `git merge --abort` puts everything back.

## Undo
```bash
git restore <file>            # discard uncommitted changes to a file
git restore --staged <file>   # unstage, keep changes
git commit --amend            # fix the last commit message
git revert <hash>             # safe undo: new commit that reverses an old one
git reset --hard <hash>       # DANGEROUS: rewrites history. Never on shared branches.
git stash / git stash pop     # park work temporarily
```

---

## Commit message convention
```
type: short imperative description

feat:     new functionality
fix:      a bug fix
refactor: code change, behaviour unchanged
docs:     documentation / comments
style:    formatting only
test:     tests
chore:    tooling, config, dependencies
```
Good: `fix: handle negative expense amounts without crashing`
Bad: `update`, `changes`, `final`, `asdf`, `fixed it`

## Branch naming
```
feature/add-currency-column
fix/negative-amount-crash
refactor/code-hygiene-priya
```
Lowercase, hyphens, purpose-first. Never `final`, `final2`, `test123`.

---

## The 15 code hygiene rules

| # | Rule |
|---|---|
| 1 | Names state intent. If you need a comment to explain a name, rename it. |
| 2 | `snake_case` functions/variables · `PascalCase` classes · `UPPER_SNAKE_CASE` constants |
| 3 | No magic numbers. Name every literal that carries meaning. |
| 4 | No secrets in source. Ever. `.env` + `.gitignore`. |
| 5 | One function, one job. Under ~20 lines. |
| 6 | Separate calculation from I/O. No `print()` inside business logic. |
| 7 | Guard clauses beat nested `if`. Max 2 levels of indentation in logic. |
| 8 | DRY — the same logic must exist in exactly one place. |
| 9 | Never use a mutable default argument (`def f(x=[])`). |
| 10 | Never `except:` bare. Catch what you can actually handle. |
| 11 | Use `with open(...)` — always close what you open. |
| 12 | No wildcard imports, no unused imports. |
| 13 | Delete dead and commented-out code. Git remembers it for you. |
| 14 | Type hints + a one-line docstring on every public function. |
| 15 | `is None`, not `== None`. `if flag:`, not `if flag == True:`. |

## Tooling — don't argue about style, run it
```bash
ruff check src/           # find problems
ruff check --fix src/     # auto-fix what it safely can
black src/                # format
python -m pytest -q       # prove behaviour unchanged
```

## What .gitignore must always contain
```
__pycache__/   .venv/   .env   *.key   *.pem   .vscode/   .DS_Store   *.log
```

---

## Three things that will save you in your first month at work

1. **`git status` before and after everything.** Confusion is almost always fixed by reading it.
2. **Pull before you start. Push before you stop.** Most merge pain is stale-branch pain.
3. **Read your own diff before you open a PR.** You will catch half your reviewer's comments yourself.
