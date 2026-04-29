from flask import Flask, request, render_template_string

app = Flask(__name__)

comments = []

FLAG = "FLAG{xss_cookie_hijack}"

@app.route("/")
def home():
    comment_html = ""

    for comment in comments:
        comment_html += f"<li>{comment}</li>"

    return render_template_string(f"""
    <h2>Comment Section</h2>

    <form method="POST" action="/comment">
        <input type="text" name="comment" placeholder="Enter comment">
        <input type="submit">
    </form>

    <h3>Comments:</h3>
    <ul>
        {comment_html}
    </ul>

    <br>
    <a href="/admin">Admin Panel</a>
    """)

@app.route("/comment", methods=["POST"])
def comment():
    user_comment = request.form.get("comment")

    if user_comment:
        comments.append(user_comment)

    return "Comment submitted successfully <br><a href='/'>Back</a>"

@app.route("/admin")
def admin():
    return f"""
    <h2>Admin Dashboard</h2>
    Admin cookies: session=admin123
    <br><br>
    {FLAG}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
