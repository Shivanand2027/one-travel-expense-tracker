# Git Tips and Common Mistakes

## Understanding Git Command Placeholders

When reading Git documentation or tutorials, you'll often see commands written with placeholders in angle brackets like:

```bash
git diff <commit1> <commit2>
```

**Important:** The angle brackets `< >` are placeholders that indicate you should replace them with actual values. **Do not type the angle brackets literally!**

### ❌ Wrong (causes syntax error):

```bash
$ git diff <commit1> <commit2>
bash: syntax error near unexpected token `<'
```

This fails because the shell interprets `<` and `>` as redirection operators, not as part of the git command.

### ✅ Correct usage:

Replace the placeholders with actual commit hashes or references:

```bash
# Using commit hashes (from git log)
$ git diff 6293eec 4960765

# Using HEAD and previous commit
$ git diff HEAD~1 HEAD

# Using branch names
$ git diff main feature-branch

# Compare working directory with a specific commit
$ git diff 6293eec
```

## Common Git Diff Examples

### View changes between two commits
```bash
# First, find the commit hashes
$ git log --oneline
4960765 (HEAD -> master) Added a new line in demo.txt
6293eec Initial commit with demo.txt

# Then compare them
$ git diff 6293eec 4960765
```

### View changes in the working directory
```bash
# Show all uncommitted changes
$ git diff

# Show changes in a specific file
$ git diff demo.txt
```

### View changes that are staged
```bash
$ git diff --staged
```

### View changes between branches
```bash
$ git diff main..feature-branch
```

## Understanding Placeholder Notation

In documentation, you'll commonly see:
- `<commit>` - Replace with a commit hash (e.g., `6293eec`) or reference (e.g., `HEAD`)
- `<branch>` - Replace with a branch name (e.g., `main`, `feature-branch`)
- `<file>` - Replace with a file path (e.g., `demo.txt`, `src/app.py`)
- `<remote>` - Replace with a remote name (e.g., `origin`)

**Always replace the entire placeholder including the angle brackets with your actual value.**

## Quick Reference

| Command | Description |
|---------|-------------|
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git diff HEAD` | Show all changes since last commit |
| `git diff <commit1> <commit2>` | Compare two commits |
| `git diff <branch1>..<branch2>` | Compare two branches |
| `git diff HEAD~1 HEAD` | Compare with previous commit |

## Pro Tips

1. Use `git log --oneline` to see commit hashes before using `git diff`
2. Use `HEAD` to refer to the current commit
3. Use `HEAD~1` for the previous commit, `HEAD~2` for two commits back, etc.
4. Tab completion can help you avoid typos with commit hashes and branch names
5. Add `--name-only` flag to see only the names of changed files: `git diff --name-only <commit1> <commit2>`

## Getting Help

For more information on git diff options:
```bash
$ git diff --help
```
