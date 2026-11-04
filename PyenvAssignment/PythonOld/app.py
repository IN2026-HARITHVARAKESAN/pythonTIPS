import sys
from flask import Flask
from importlib.metadata import version

if sys.version_info[:3] != (3, 8, 10):
    raise RuntimeError("PythonOld requires Python 3.8.10")

if version("Flask") != "2.3.3":
    raise RuntimeError("PythonOld requires Flask 2.3.3")

app = Flask(__name__)

@app.route("/")
def home():
    return "PythonOld: Python 3.8.10 + Flask 2.3.3"

if __name__ == "__main__":
    app.run()