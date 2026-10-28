from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Xin chào, Flask!</h1>"


# Bài 3: Lời chào
@app.route("/hello/", defaults={"name": "bạn"})
@app.route("/hello/<name>")
def hello(name):
    return f"Xin chào, {escape(name)}!"


# Bài 4: Bình phương số nguyên, hỗ trợ số âm
@app.route("/square/<int(signed=True):n>")
def square(n):
    return f"Bình phương của {n} là {n * n}"


if __name__ == "__main__":
    app.run(debug=True, port=8000)