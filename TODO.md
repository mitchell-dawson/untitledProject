- [ ] setup virtual environment in venv folder
```
virtualenv --python=/usr/bin/python3.6 untitledProject
```
- [ ] Add virtual env activate to alias into .bash_rc file
```
alias ml='source /path/to/project/venv/untitledProject/bin/activate'
```
- [ ] Select python interpreter in vscode
- [ ] Install package with pip in dev mode
```
pip install -e ./
```
- [ ] Create launch.json file (run in debug mode)
