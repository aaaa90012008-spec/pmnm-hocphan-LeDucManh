
from flask import Flask, request, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Trang chủ</h1>"


@app.route("/about")
def about():
    return "<h1>Giới thiệu</h1>"


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    return f"<h1>Bài viết số {post_id}</h1>"


@app.route("/user/<username>")
def user_profile(username):
    return f"<h1>Hồ sơ: {escape(username)}</h1>"


@app.route("/search")
def search():
    query = request.args.get("q", "")
    return f"<h1>Tìm kiếm: {escape(query)}</h1>"


@app.route("/menu")
def menu():
    links = [
        ("Trang chủ", url_for("index")),
        ("Giới thiệu", url_for("about")),
        ("Bài viết số 7", url_for("post_detail", post_id=7)),
        (
            "Hồ sơ Nguyễn An",
            url_for("user_profile", username="Nguyễn An"),
        ),
        ("Tìm Flask và Python", url_for("search", q="flask & python")),
    ]

    items = "".join(
        f'<li><a href="{escape(href)}">{escape(label)}</a></li>'
        for label, href in links
    )

    return f"<h1>Menu</h1><ul>{items}</ul>"


if __name__ == "__main__":
    app.run(debug=True, port=8003)
