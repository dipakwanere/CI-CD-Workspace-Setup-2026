How to setup a project with Python venv and scaffold files for production ready code.

## Creating a venv for a project 
python -m venv .venv
Windows use `.venv\Scripts\activate`
Linux/Mac use `source .venv/bin/activate`


##  Fixing the venv gone in new terminal
If you open a new terminal and your venv is gone, you can reactivate it by running the activate command again: BUT ---- Here is the fix 

* Step 1: Open the terminal in VS Code.
* Step 2: vim ~/.bashrc  (or ~/.zshrc if you use zsh)
* Step 3: Press "Shift+G" to go to bottom of the file. and Add the following line at the end of the file:
    # Souce VirtualENV
    Windows use `.venv\Scripts\activate`
    Linux/Mac use `source .venv/bin/activate`

* Quit Vim editor by typing `:wq` and pressing Enter.




## Creating scaffolded projects

- create a makefile with  touch Makefile
- create a requirements.txt with touch requirements.txt
- create a .gitignore with touch .gitignore
- create a main.py with touch main.py
- create a readme.md with touch readme.md
- create a tests folder with mkdir tests
- create a test files with touch tests/test_main.py
- create a src folder with mkdir src


Makefile example:

```Makefile
install:
    pip install --upgrade pip &&\
    pip install -r requirements.txt

test:
    python -m pytest -vv tests/test_main.py

format:
    black *.py

lint:
    pylint --disable=R,C,W *.py or src/*.py or scr/filename.py

all: install lint test

```
install:
    pip install --upgrade pip
    pip install -r requirements.txt

test:
    python -m pytest -vv tests/test_hello.py

format:
    black *.py

lint:
    pylint --disable=R,C src/main.py

all: install lint test



cli.py → contains functions
pyproject.toml OR setup.py → defines CLI commands
pip install -e . → installs package in editable mode
terminal → run CLI commands (install/test/lint/all/format)