from flask import Flask, request, render_template_string

app = Flask(__name__)

FLAG = "FLAG{ssti_template_escape}"

@app.route("/")
def home():
    return """
    <h2>Welcome Page Generator</h2>

    <form method="GET" action="/greet">
        Enter your name:
        <input type="text" name="name">
        <input type="submit">
    </form>
    """

@app.route("/greet")
def greet():
    name = request.args.get("name", "")

    template = f"""
    <h2>Hello {name}</h2>
    """

    if "config" in name:
        return FLAG

    return render_template_string(template)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
