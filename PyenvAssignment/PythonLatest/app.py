import sys
from flask import Flask
from importlib.metadata import version

if sys.version_info[:3] != (3, 14, 5):
    raise RuntimeError("PythonLatest requires Python 3.14.5")

if version("Flask") != "3.1.3":
    raise RuntimeError("PythonLatest requires Flask 3.1.3")

app = Flask(__name__)

app.config["SECRET_KEY"] = "new-secret-key"
app.config["SECRET_KEY_FALLBACKS"] = ["old-secret-key"]

@app.route("/")
def home():
    return "PythonLatest: Python 3.14.5 + Flask 3.1.3"

if __name__ == "__main__":
    app.run()