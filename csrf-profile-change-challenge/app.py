from flask import Flask, request

app = Flask(__name__)

current_email = "user@safe.com"
FLAG = "FLAG{csrf_account_takeover}"

@app.route("/")
def home():
    global current_email

    return f"""
    <h2>User Profile</h2>
    Current Email: {current_email}

    <form method="POST" action="/change-email">
        New Email:
        <input type="text" name="email">
        <input type="submit" value="Update">
    </form>
    """

@app.route("/change-email", methods=["POST"])
def change_email():
    global current_email

    new_email = request.form.get("email")

    if new_email:
        current_email = new_email

    if current_email == "attacker@evil.com":
        return FLAG

    return f"Email updated to: {current_email}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
