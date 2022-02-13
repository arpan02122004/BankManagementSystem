# COMMANDS TO GET STARTED
## change your mysql sql server psswd in password.json in front of databsepsswd only
## don't change the other value 

```python
pip install -r requirements.txt
```
### You can setup required sql tables by setup.py in : 

#### NOTE : You can also import the the databse of sql in databse folder ...
```shell
cd "$(pwd)\setup_environment"
```
### You can run you in virtual_env by : 
```shell
".\$(pwd)\venv\Scripts\activate.ps1"
```
## After all this run your virtual bank by 
```python
python "$(pwd)\menu.py"
```