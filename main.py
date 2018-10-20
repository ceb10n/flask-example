from flask import Flask
from flask_cors import CORS
from do_blueprint import bp


app = Flask(__name__)
CORS(app)

app.config[
    "SECRET_KEY"
] = "\x18\xb9\xcb\xf5\xaa0\x9aL5\xc0\xcc\x8f#\xc8D\xa6F\x86\x18\x9d\xfc\r@p"


app.register_blueprint(bp)


if __name__ == "__main__":
    app.run()
