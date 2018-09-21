from flask import Flask, jsonify
from digitalocean import DigitalOcean
import os

app = Flask(__name__)
do_token = os.environ.get('DO_TOKEN', '')

@app.route("/account")
def home():
    digital_ocean = DigitalOcean(do_token)
    account = digital_ocean.account()
    print(account)
    return jsonify(account.__dict__)

if __name__ == "__main__":
    app.run()
