# untitledProject
Template project for python data science projects

### Set up virtual environments in `venv` folder
```
virtualenv --python=/usr/bin/python3.6 untitledProject
```

### Add virtual env activate to alias into `.bash_rc` file
```
alias untitledProject='source /path/to/project/venv/untitledProject/bin/activate'
```

### Install package with pip in dev mode
```
pip install -e ./
```

### Set up `__init__.py` files
[whats init for me?](https://towardsdatascience.com/whats-init-for-me-d70a312da583)


### intialise git repository
```
git init
```

### Edit `.gitignore` file
```
data/*
venv/
*projectName.egg-info
*.vscode
scripts/notebook/rough/*
*__pycache__
```

### VSCode
- Select interpreter
- Run unit tests (create launch.json)

---
## File structure:
```
./
├── data
│   ├── db
│   ├── model
│   ├── processed
│   └── raw
├── projectName
│   ├── __init__.py
│   ├── module1.py
│   ├── subpackage_1
│   │   ├── __init__.py
│   │   ├── moduleA.py
│   │   ├── moduleB.py
│   │   ├── moduleC.py
│   │   └── test
│   │       ├── __init__.py
│   │       ├── test_moduleA.py
│   │       └── test_moduleB.py
│   ├── subpackage_2
│   │   ├── __init__.py
│   │   ├── moduleC.py
│   │   └── test
│   │       ├── __init__.py
│   │       └── test_moduleC.py
│   └── test
│       ├── __init__.py
│       └── test_class1.py
├── projectName.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── README.md
├── requirements.txt
├── scripts
│   ├── get_requirements.sh
│   ├── notebook
│   │   ├── eda
│   │   └── rough
│   │       └── rough_working.py
│   ├── prep
│   │   └── example_scipt.py
│   └── processing
├── setup.py
├── TODO.md
└── venv
    └── untitledProject
        ├── bin
        ├── include
        └── lib
```
---

## Other tips:

### Working imports
Remember to always run code from top folder

### Package wide unit testing
if you include `__init__.py` files in all test folders, all unit tests in the package can be found recursively run using:
```
python -m unittest discover -p test_*
```


### Avoid deep nesting
Two levels is almost always enough
```
Yes: "pyranha"
Yes: "pythonsport.climbing"
Yes: "pythonsport.forestmap"
No: "pythonsport.maps.forest"
```

### Use brackets for multiline imports
`import *` is not an option!
```
from Tkinter import (Tk, Frame, Button, Entry, Canvas, Text,
    LEFT, DISABLED, NORMAL, RIDGE, END)

```

