from flask import Flask, request
import requests

app = Flask(__name__)

FLAG = "FLAG{ssrf_internal_metadata_access}"

@app.route("/")
def home():
    return """
    <h2>Website Screenshot Service</h2>

    <form method="GET" action="/fetch">
        URL:
        <input type="text" name="url">
        <input type="submit">
    </form>
    """

@app.route("/fetch")
def fetch():
    url = request.args.get("url", "")

    if not url.startswith("http"):
        return "Invalid URL"

    try:
        if "169.254.169.254" in url:
            return FLAG

        response = requests.get(url, timeout=3)
        return response.text[:500]

    except:
        return "Request failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
