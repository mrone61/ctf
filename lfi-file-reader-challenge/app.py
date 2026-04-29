from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>File Viewer</h2>

    Example:
    /view?file=notes.txt
    """

@app.route("/view")
def view():
    filename = request.args.get("file", "")

    try:
        with open(filename, "r") as f:
            content = f.read()

        return f"<pre>{content}</pre>"

    except:
        return "File not found"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
