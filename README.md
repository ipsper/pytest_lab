# pytest_lab
base to be able to compare pytest with other test frameworks

## setup in vent
```
cd $HOME/repo/pytest_lab
python3 -m venv pytest_lab_venv
source pytest_lab_venv/bin/activate
python -m pip install -r requirements.txt
```
## To exit
```
deactivate
```
## To delete vent
```
rm -rf $HOME/repo/pytest_lab/pytest_lab_venv
```
[For test information](tests/README.md#tests)

## Run tests 
```
python -m pytest -sx tests/test_of_localhost.py
```


