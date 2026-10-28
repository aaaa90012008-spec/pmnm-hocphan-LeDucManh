from flask import Flask, jsonify
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# Converter nhận danh sách số nguyên cách nhau bằng dấu phẩy
class ListConverter(BaseConverter):
    # Cho phép số nguyên dương, 0 và số nguyên âm
    # Ví dụ: 1,2,3 hoặc -1,4,10
    regex = r"-?\d+(?:,-?\d+)*"

    def to_python(self, value):
        """Chuyển chuỗi URL thành danh sách số nguyên."""
        return [int(number) for number in value.split(",")]

    def to_url(self, values):
        """Chuyển danh sách số nguyên thành chuỗi URL."""
        return ",".join(str(int(number)) for number in values)


# Đăng ký converter với Flask
app.url_map.converters["list"] = ListConverter


@app.route("/")
def index():
    return "<h1>Bài 5 - Custom URL Converter</h1>"


@app.route("/sum/<list:numbers>")
def sum_numbers(numbers):
    return jsonify(
        numbers=numbers,
        sum=sum(numbers)
    )


if __name__ == "__main__":
    app.run(debug=True, port=8002)