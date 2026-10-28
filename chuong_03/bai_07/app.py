from flask import Flask, url_for

app = Flask(__name__)


# GET: Hiển thị form đăng nhập
@app.get("/login", strict_slashes=False)
def login_form():
    return f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <title>Đăng nhập</title>
    </head>
    <body>
        <h1>Đăng nhập</h1>

        <form method="post" action="{url_for('login_submit')}">
            <label for="username">Tên đăng nhập:</label>
            <input type="text" id="username" name="username" required>
            <button type="submit">Đăng nhập</button>
        </form>
    </body>
    </html>
    """


# POST: Xử lý yêu cầu đăng nhập
@app.post("/login", strict_slashes=False)
def login_submit():
    return "Đã nhận yêu cầu đăng nhập (POST)."


if __name__ == "__main__":
    app.run(debug=True, port=8004)