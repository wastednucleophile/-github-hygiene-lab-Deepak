## What changed
<!-- One or two lines. What did you actually do? -->

## Why
<!-- What problem does this fix? Reference the hygiene rule number if applicable. -->

## How to verify
```bash
python -m pytest -q
ruff check src/
black --check src/
```

## Checklist
- [ ] All tests pass locally
- [ ] `ruff check` is clean
- [ ] `black --check` is clean
- [ ] No secrets, keys, or passwords in the diff
- [ ] Commit messages follow `type: short description`
- [ ] I reviewed my own diff before opening this PR
