# Git Workflow Cheat Sheet for ASVS Panjabi Translation
# ASVS ਪੰਜਾਬੀ ਅਨੁਵਾਦ ਲਈ Git ਵਰਕਫਲੋ ਚੀਟ ਸ਼ੀਟ

## Daily Workflow (5 commands)

### 1. Start of session — pull latest changes
```bash
cd "path/to/ASVS"
git checkout panjabi-translation-v5
git pull origin panjabi-translation-v5
```

### 2. Make your changes
Edit files in `5.0/pa-IN/` using any text editor.

### 3. Check what changed
```bash
git status
git diff
```

### 4. Stage and commit
```bash
git add 5.0/pa-IN/
git commit -m "trans(pa-IN): translate 0x02-Preface.md"
```

### 5. Push to GitHub
```bash
git push origin panjabi-translation-v5
```

PR #3254 updates automatically when you push.

---

## Commit Message Format
```
trans(pa-IN): <what you did>
```

Examples:
- `trans(pa-IN): translate 0x02-Preface.md`
- `trans(pa-IN): expand glossary to 100 terms`
- `trans(pa-IN): fix Gurmukhi spelling in Authentication chapter`

## Useful Commands

| What | Command |
|------|---------|
| See PR status | `gh pr view 3254` |
| See what's changed | `git status` |
| Undo last unstaged change | `git checkout -- <file>` |
| See commit history | `git log --oneline -10` |
| Sync with upstream OWASP | `git fetch upstream && git merge upstream/master` |

## Branch Structure
```
master (OWASP/ASVS upstream)
  └── panjabi-translation-v5 (your PR branch)
        └── 5.0/pa-IN/ (translation files)
```
