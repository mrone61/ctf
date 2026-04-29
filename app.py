from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Login Panel</h2>
    <form method="POST" action="/login">
        Username: <input type="text" name="username"><br>
        Password: <input type="text" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    print("Query executed:", query)

    result = cur.execute(query).fetchone()

    if result:
        return "Welcome Admin! FLAG{web_exploitation_master}"
    else:
        return "Login failed"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
