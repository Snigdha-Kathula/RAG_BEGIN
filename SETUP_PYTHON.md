# Switch Python version for this project

Your default `python3` is 3.14; this project needs **Python 3.12** (or 3.11) for ChromaDB/LangChain.

## Option A: Recreate the venv with Python 3.12 (recommended)

Run these in your project folder:

```bash
# 1. Go to project
cd /Users/snigdhaa/Desktop/RAG/RAG_FOR_BEGINNERS

# 2. Deactivate current venv if active (type "deactivate" or close the terminal)

# 3. Remove old venv (backup first if you want)
rm -rf venv

# 4. Create new venv with Python 3.12
/opt/homebrew/bin/python3.12 -m venv venv

# 5. Activate it
source venv/bin/activate

# 6. Confirm version
python --version
# Should show: Python 3.12.12

# 7. Install dependencies
pip install -r requirements-gemini.txt

# 8. Run the pipeline
python ing_pipeline_gemini.py
```

## Option B: Keep both venvs (use a new folder)

If you want to keep the old venv and also have a 3.12 one:

```bash
cd /Users/snigdhaa/Desktop/RAG/RAG_FOR_BEGINNERS

# Create venv with a different name
/opt/homebrew/bin/python3.12 -m venv venv312

# Use this one from now on
source venv312/bin/activate
pip install -r requirements-gemini.txt
python ing_pipeline_gemini.py
```

## Make Python 3.12 the default for this project (optional)

In Cursor/VS Code:

1. **Select interpreter**: `Cmd+Shift+P` → “Python: Select Interpreter”
2. Choose the one that shows **Python 3.12** and path `.../venv/bin/python` (or `.../venv312/bin/python`).

Your terminal will still use whatever venv you `source`; the interpreter picker only affects the editor (running/debugging, linting).

## Quick reference

| Command | Purpose |
|--------|--------|
| `which python` | See which Python is used (after activating venv) |
| `python --version` | Check version |
| `deactivate` | Leave the current venv |
| `source venv/bin/activate` | Enter the project venv (3.12) |
