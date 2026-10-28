from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/info", methods=["GET", "POST"], strict_slashes=False)
def info():
    # Thông tin cơ bản của HTTP request
    method = escape(request.method)
    path = escape(request.path)
    full_path = escape(request.full_path)
    full_url = escape(request.url)

    # Địa chỉ IP và trình duyệt gửi request
    ip_address = escape(request.remote_addr or "Không xác định")
    user_agent = escape(
        request.headers.get("User-Agent", "Không có User-Agent")
    )

    # Lấy các tham số query, ví dụ ?x=1&y=2
    query_params = request.args

    if query_params:
        query_rows = ""

        for key, values in query_params.lists():
            for value in values:
                query_rows += f"""
                <tr>
                    <td>{escape(key)}</td>
                    <td>{escape(value)}</td>
                </tr>
                """
    else:
        query_rows = """
        <tr>
            <td colspan="2">Không có tham số query</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Thông tin HTTP Request</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 40px auto;
                padding: 0 20px;
                background: #f4f7fb;
                color: #243247;
            }}
            h1, h2 {{ color: #164b8b; }}
            table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
                margin-bottom: 24px;
            }}
            th, td {{
                border: 1px solid #cbd5e1;
                padding: 12px;
                text-align: left;
                overflow-wrap: anywhere;
            }}
            th {{
                background: #164b8b;
                color: white;
            }}
            tr:nth-child(even) {{ background: #eef4fa; }}
            a {{ color: #0866c6; }}
        </style>
    </head>
    <body>
        <h1>Thông tin HTTP Request</h1>

        <table>
            <tr><th>Thông tin</th><th>Giá trị</th></tr>
            <tr><td>Phương thức</td><td>{method}</td></tr>
            <tr><td>Đường dẫn</td><td>{path}</td></tr>
            <tr><td>Đường dẫn kèm query</td><td>{full_path}</td></tr>
            <tr><td>URL đầy đủ</td><td>{full_url}</td></tr>
            <tr><td>Địa chỉ IP</td><td>{ip_address}</td></tr>
            <tr><td>User-Agent</td><td>{user_agent}</td></tr>
        </table>

        <h2>Các tham số query</h2>
        <table>
            <tr><th>Tên tham số</th><th>Giá trị</th></tr>
            {query_rows}
        </table>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True, port=8005)