from flask import Flask, request
import os

app = Flask(__name__)

FLAG = "FLAG{command_execution_success}"

@app.route("/")
def home():
    return """
    <h2>Ping Tool</h2>

    <form method="GET" action="/ping">
        Target IP/Host:
        <input type="text" name="target">
        <input type="submit">
    </form>
    """

@app.route("/ping")
def ping():
    target = request.args.get("target", "")

    command = f"ping -c 1 {target}"
    output = os.popen(command).read()

    if "cat /flag.txt" in target:
        return FLAG

    return f"<pre>{output}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
