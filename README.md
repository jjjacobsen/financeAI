# financeAI #
Using AI to calculate a budget and give financial advice based on my current financial state, primarily written in Go

- The main benefit is for when I calculate my net worth every month and I sort my transactions into categories like gas, groceries, drinks, etc
    - Use AI to do the sorting
- Can access my transaction history through apis, and make sure not to let any kind of passwords end up on the public repo
- Can also access my loan information and other assets through apis
- Have code put everything into the Google Sheet so I can see it easily
    - maybe eventually I move data to a database and make a fancy UI. For now, Google Sheets is good enough
- Once I collect all the data, use AI to calculate a budget and give financial advice


### Setup ###

1. Install pyenv and pyenv-virtualenv ([brew](https://brew.sh/))
   ```sh
   brew update
   brew upgrade
   brew install pyenv
   brew install pyenv-virtualenv
   ```
2. Install python and create the venv
   ```sh
   pyenv install <python version>
   pyenv virtualenv <python version> <venv name>
   ```
    - for automatic sourcing of the venv
        ```sh
        pyenv local <venv name>
        ```
    - Current version is 3.12.6
3. Install pdm
    ```sh
    pip install pdm
    ```
    - Current version is 2.19.1
4. Install the rest of the packages
    ```sh
    pdm install --dev
    ```
5. Setup pre-commit
    ```sh
    pre-commit install
    ```


### To setup manual.py ###

Needed to do a few things
- create new google cloud project
    - enable services
        - sheets.googleapis.com
        - drive.googleapis.com
    - create service account and download json key
- from the sheet ui, share it with the service account email
- for restricted files that need a symbolic link:
    - `ln -s ~/path/to/file restricted/file`


### To run ###

- login to bank and expand the transactions history to get needed transactions, then download the html
    - right click -> save page as -> Format: Web Page, Complete -> ledger.html
        - this also downloads some directory with extra files, but ledger.html is the only one needed
    - ledger.html needs to be under restricted/
- `python main.py`
