from flask import Flask, request
import jwt

app = Flask(__name__)

SECRET_KEY = "supersecretkey"
FLAG = "FLAG{jwt_none_algorithm_bypass}"

@app.route("/")
def home():
    token = jwt.encode(
        {"user": "guest"},
        SECRET_KEY,
        algorithm="HS256"
    )

    return f"""
    <h2>JWT Login Portal</h2>
    Your token:<br><br>

    {token}

    <br><br>
    Visit:
    /admin?token=YOUR_TOKEN
    """

@app.route("/admin")
def admin():
    token = request.args.get("token")

    try:
        decoded = jwt.decode(
            token,
            options={"verify_signature": False},
            algorithms=["HS256", "none"]
        )

        if decoded.get("user") == "admin":
            return FLAG

        return "Access denied: not admin"

    except:
        return "Invalid token"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
