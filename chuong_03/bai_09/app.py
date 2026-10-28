from flask import Flask, request, jsonify, abort

app = Flask(__name__)


@app.get("/calc")
def calculate():
    # Đọc hai số từ query string
    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    # Phép toán mặc định là add
    op = request.args.get("op", "add")

    # Kiểm tra thiếu tham số hoặc dữ liệu không phải số
    if a is None or b is None:
        abort(400, description="Tham số a và b phải được cung cấp dưới dạng số.")

    # Kiểm tra phép toán hợp lệ
    if op not in {"add", "sub", "mul", "div"}:
        abort(400, description="Phép toán không hợp lệ. Dùng add, sub, mul hoặc div.")

    # Thực hiện phép tính
    if op == "add":
        result = a + b
        symbol = "+"

    elif op == "sub":
        result = a - b
        symbol = "-"

    elif op == "mul":
        result = a * b
        symbol = "*"

    else:  # op == "div"
        if b == 0:
            abort(400, description="Không thể chia cho 0.")

        result = a / b
        symbol = "/"

    # Tạo biểu thức dễ đọc, ví dụ: 5 + 3
    expression = f"{a:g} {symbol} {b:g}"

    # Trả dữ liệu JSON
    return jsonify({
        "a": a,
        "b": b,
        "op": op,
        "expression": expression,
        "result": result
    })


# Chuyển lỗi HTTP 400 thành JSON
@app.errorhandler(400)
def handle_bad_request(error):
    return jsonify({
        "error": error.description
    }), 400


if __name__ == "__main__":
    app.run(debug=True, port=8006)
    