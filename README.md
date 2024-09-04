# financeAI #
Using AI to calculate a budget and give financial advice based on my current financial state, primarily written in Go

- The main benefit is for when I calculate my net worth every month and I sort my transactions into categories like gas, groceries, drinks, etc
    - Use AI to do the sorting
- Can access my transaction history through apis, and make sure not to let any kind of passwords end up on the public repo
- Can also access my loan information and other assets through apis
- Have this code put everything into the Google Sheet so I can see it easily
- Once I have all this data, use AI to calculate a budget and give financial advice


### Notes ###
- Seems like Gorgonia is the AI library for Go
    - https://gorgonia.org/
- I really would like this to do three things (these are the exported functions)
    - pull transactions via api or web scraping
    - group the transactions
    - put the sum of the groups into my net worth Google doc
        - if it does this then calculating the net worth stuff becomes very easy
- These are bonus things that would be nice to have
    - get all other financial data via api
        - loans
        - investments
    - given the data above, to give financial advice based on those numbers
- Build an executable and put it in my PATH so that I can use this code easily from the cli
    - given the project structure below, use this command
    - `go build -o /usr/local/bin/yourapp ./cmd/financeAI`
    - not sure if this does the permissions correctly, we will have to see
- After investigation I decided to use a Random Forest ML model
    - after conversing with the AI this seems to be my best choice
    - was originally going to use the Gorgonia library, however that doesn't support random forest so I'm using GoLearn instead
        - https://github.com/sjwhitworth/golearn
- When I asked the AI for how I should organize the repo, it gave me this. I like it
```
/
├── cmd
│   └── yourapp
│       └── main.go  # Contains the main function and CLI setup.
├── pkg
│   ├── processor
│   │   └── processor.go  # Business logic for processing data.
│   ├── loader
│   │   └── loader.go  # Logic for loading/saving data.
│   └── model
│       └── model.go  # Definitions of data models and possibly machine learning models.
├── data
│   └── ...           # Data files, possibly ignored in .gitignore for large datasets.
├── scripts
│   └── setup.sh      # Scripts for setting up or configuring the environment.
├── go.mod
├── go.sum
└── README.md
```
- there is an example file under cmd for how to build a random forest model using GoLearn. Take that and build all these pkg's out
- I can save the output of a trained model using encoding/gob, just ask the AI how to do it
- to build these training datasets I might need to make a custom tool that I can click in a gui to speed sort all the transactions
    - like I collect all the transactions then display them one at a time in the gui, tinder style, and select which group it belongs
    - as I go through and manually sort, it builds the training dataset on each click
- since I have a limited number of factors, trying different parameters for the model is how I will find the highest accuracy
    - like building 150 trees instead of 100, etc
- I want to make sure that wherever I run this binary from, the data and models are always stored in the data directory in this repo
    - might need to create and use scripts/setup.sh for that

### Python Packages ###

For now I'm still using requirements.txt. I want to learn something new like pdm or poetry and do this in a better way. Here are the high level packages I installed so I can remember before I learn the new stuff

- python-dotenv
- gspread
- google-auth

### To setup manual.py ###

Needed to do a few things
- create new google cloud project
- enable services
    - sheets.googleapis.com
    - drive.googleapis.com
- create service account and download json key
- from the sheet, share it with the service account email
