import sys
from flask import Flask
from importlib.metadata import version

if sys.version_info[:3] != (3, 11, 9):
    raise RuntimeError("PythonIntermediate requires Python 3.11.9")

if version("Flask") != "3.0.3":
    raise RuntimeError("PythonIntermediate requires Flask 3.0.3")

app = Flask(__name__)

@app.route("/")
def home():
    return "PythonIntermediate: Python 3.11.9 + Flask 3.0.3"

if __name__ == "__main__":
    app.run()