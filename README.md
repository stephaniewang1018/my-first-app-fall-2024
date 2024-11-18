# my-first-app-fall-2024

## Setup

Create a virtual environment (first time only):

```sh
conda create -n reports-env-2024 python=3.12.7
```

Activate the environment (whenever you come back to this project):

```sh
conda activate reports-env-2024
```

Install packages:

```sh
pip install -r requirements.txt
```

[Obtain an API Key] (https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Signing up for the email sending platform (e.g. Sendgrid). Obtain sendgrid API Key, and set the key and your sender address as env vars.

Create a ".env" file and add contents like the following (using your own AlphaVantage API Key):

```sh
# this is the ".env" file:
ALPHAVANTAGE_API_KEY="..."

# optionally:
SENDGRID_API_KEY = "_______"
SENDGRID_SENDER_ADDRESS = "________"
```

## Usage

Run the example script:

```sh
python app/example.py
```

Run the unemployment report:

```sh
#ALPHAVANTAGE_API_KEY="JYN0QT6BO4ZPV807" python app/unemployment_report.py

#python app/unemployment_report.py
python -m app.unemployment_report
```

Run the stocks report:

```sh
#python app/stocks_report.py 
python -m app.stocks_report
```

Run the example email sending file:

```sh
python app/email_service.py
```

### Web App 

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run tests:

```sh
pytest
```
