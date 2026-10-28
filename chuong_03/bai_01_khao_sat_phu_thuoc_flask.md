# Chương 3 — Bài 1: Khảo sát các gói phụ thuộc của Flask

## 1. Thông tin Flask

Sử dụng lệnh `pip show Flask` để khảo sát thông tin của Flask trong môi trường Python.

- Tên gói: Flask
- Phiên bản: 3.1.3
- Giấy phép: BSD-3-Clause
- Công dụng: Flask là framework Python dùng để xây dựng ứng dụng web.
- Các gói phụ thuộc trực tiếp (Requires): blinker, click, itsdangerous, Jinja2, MarkupSafe và Werkzeug.

## 2. Bảng khảo sát các gói phụ thuộc

| Gói | Phiên bản | Giấy phép | Vai trò |
|---|---|---|---|
| Flask | 3.1.3 | BSD-3-Clause | Framework xây dựng ứng dụng web bằng Python |
| Werkzeug | 3.1.9 | BSD-3-Clause | Cung cấp các thành phần WSGI, xử lý request, response và routing |
| Jinja2 | 3.1.6 | BSD-3-Clause | Bộ máy dựng mẫu HTML, cho phép kết hợp dữ liệu với giao diện |
| MarkupSafe | 3.0.4 | BSD-3-Clause | Xử lý chuỗi và hỗ trợ escape nội dung để giảm nguy cơ chèn mã HTML |
| blinker | 1.9.0 | MIT | Cung cấp cơ chế signal để các thành phần thông báo sự kiện cho nhau |
| click | 8.5.0 | BSD-3-Clause | Hỗ trợ xây dựng giao diện dòng lệnh và các lệnh quản trị |
| itsdangerous | 2.2.0 | BSD-3-Clause | Hỗ trợ ký và xác minh dữ liệu, chẳng hạn dữ liệu được truyền qua cookie |

Lưu ý: Phiên bản và giấy phép trong bảng cần được đối chiếu với kết quả `pip show` của môi trường Flask đang khảo sát. Nếu kết quả máy tính khác, hãy cập nhật bảng theo dữ liệu thực tế.

## 3. Cách kiểm tra thông tin giấy phép

Để kiểm tra thông tin của từng gói, sử dụng các lệnh:

```powershell
python -m pip show Flask
python -m pip show Werkzeug
python -m pip show Jinja2
python -m pip show MarkupSafe
python -m pip show blinker
python -m pip show click
python -m pip show itsdangerous