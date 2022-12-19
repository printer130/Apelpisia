# Apelpisia

Apelpisia is an API connected with twilio and openai for whatsapp chating

## Requirements
These four env variables found in openai and twilio console.
```
OPENAI_KEY=
OPENAI_ORG=

TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
```
Install [ngrok](https://ngrok.com/) from webpage.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage

```python
ngrok http 8080 # This URL goes messages in twilio (web hook)

python3 index.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
