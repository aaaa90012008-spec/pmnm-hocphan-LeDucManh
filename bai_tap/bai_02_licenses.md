# Bài 2.2 — Rà soát giấy phép các gói Python

## 1. Phạm vi khảo sát

Báo cáo được tạo bằng công cụ pip-licenses trong môi trường ảo `.venv` của repository học phần. Môi trường có các gói phục vụ thực hành Python, Flask, kiểm thử, HTTP và quản lý cơ sở dữ liệu.

Danh sách dưới đây phản ánh các gói đã cài tại thời điểm kiểm tra, bao gồm cả phụ thuộc của chúng và công cụ phục vụ bài thực hành. Đây không mặc nhiên là danh sách phụ thuộc của một ứng dụng thương mại cụ thể.

## 2. Bảng kiểm kê giấy phép

| Name               | Version    | License                              | URL                                                                   |
|--------------------|------------|--------------------------------------|-----------------------------------------------------------------------|
| Flask              | 3.1.3      | BSD-3-Clause                         | https://github.com/pallets/flask/                                     |
| Jinja2             | 3.1.6      | BSD License                          | https://github.com/pallets/jinja/                                     |
| MarkupSafe         | 3.0.4      | BSD-3-Clause                         | https://github.com/pallets/markupsafe/                                |
| Pygments           | 2.21.0     | BSD-2-Clause                         | https://pygments.org                                                  |
| SQLAlchemy         | 2.1.6      | MIT                                  | https://www.sqlalchemy.org                                            |
| Werkzeug           | 3.1.9      | BSD-3-Clause                         | https://github.com/pallets/werkzeug/                                  |
| black              | 26.10.1    | MIT                                  | https://github.com/psf/black                                          |
| blinker            | 1.9.0      | MIT License                          | https://github.com/pallets-eco/blinker/                               |
| certifi            | 2026.10.23 | Mozilla Public License 2.0 (MPL 2.0) | https://github.com/certifi/python-certifi                             |
| charset-normalizer | 3.5.2      | MIT                                  | https://github.com/jawah/charset_normalizer/blob/master/CHANGELOG.md  |
| click              | 8.5.0      | BSD-3-Clause                         | https://github.com/pallets/click/                                     |
| colorama           | 0.4.6      | BSD License                          | https://github.com/tartley/colorama                                   |
| idna               | 3.20       | BSD-3-Clause                         | https://github.com/kjd/idna                                           |
| iniconfig          | 2.3.1      | MIT                                  | https://github.com/pytest-dev/iniconfig                               |
| itsdangerous       | 2.2.0      | BSD License                          | https://github.com/pallets/itsdangerous/                              |
| markdown-it-py     | 4.2.0      | MIT License                          | https://github.com/executablebooks/markdown-it-py                     |
| mdurl              | 0.1.2      | MIT License                          | https://github.com/executablebooks/mdurl                              |
| mypy_extensions    | 1.1.0      | MIT                                  | https://github.com/python/mypy_extensions                             |
| packaging          | 26.3       | Apache-2.0 OR BSD-2-Clause           | https://github.com/pypa/packaging                                     |
| pathspec           | 1.1.1      | Mozilla Public License 2.0 (MPL 2.0) | https://python-path-specification.readthedocs.io/en/latest/index.html |
| platformdirs       | 4.13.7     | MIT                                  | https://github.com/tox-dev/platformdirs                               |
| pluggy             | 1.7.0      | MIT License                          | https://github.com/pytest-dev/pluggy                                  |
| pytest             | 9.2.0      | MIT                                  | https://docs.pytest.org/en/latest/                                    |
| python-dotenv      | 1.2.4      | BSD-3-Clause                         | https://github.com/theskumar/python-dotenv                            |
| pytokens           | 0.4.1      | MIT License                          | https://github.com/tusharsadhwani/pytokens                            |
| requests           | 2.34.2     | Apache Software License              | https://github.com/psf/requests                                       |
| rich               | 15.0.0     | MIT License                          | https://github.com/Textualize/rich                                    |
| typing_extensions  | 4.16.0     | PSF-2.0                              | https://github.com/python/typing_extensions                           |
| urllib3            | 2.8.0      | MIT                                  | https://github.com/urllib3/urllib3/blob/main/CHANGES.rst              |


## 3. Kết quả rà soát và phân tích rủi ro copyleft

### 3.1. Kết quả kiểm kê

Bảng kiểm kê được tạo bằng công cụ pip-licenses trong môi trường ảo `.venv` của repository học phần. Kết quả hiện ghi nhận 29 gói Python, bao gồm các thư viện phục vụ phát triển ứng dụng web, gửi HTTP request, kiểm thử và quản lý cơ sở dữ liệu cùng những gói phụ thuộc.

Trong danh sách được công cụ nhận diện, chưa phát hiện gói mang giấy phép GPL hoặc AGPL. Kết luận này chỉ áp dụng cho danh sách gói trong môi trường đã kiểm tra tại thời điểm khảo sát. Nó không chứng minh rằng mọi phụ thuộc của một ứng dụng khác đều không có GPL hoặc AGPL, cũng không thay thế việc kiểm tra các giấy phép chưa được nhận diện đầy đủ.

### 3.2. Các giấy phép cần chú ý

Hai gói `certifi` và `pathspec` được báo cáo dưới giấy phép Mozilla Public License 2.0 (MPL 2.0). Đây là giấy phép copyleft ở cấp độ tệp: khi phân phối mã nguồn thuộc phạm vi MPL đã được sửa đổi, các nghĩa vụ của MPL áp dụng đối với phần mã nguồn được bảo vệ. Tuy nhiên, MPL cho phép kết hợp mã được cấp phép theo MPL với các thành phần riêng biệt theo giấy phép khác, miễn là vẫn tuân thủ các điều kiện dành cho thành phần MPL.

Gói `packaging` được ghi nhận với lựa chọn giấy phép Apache-2.0 OR BSD-2-Clause. Gói `requests` được ghi nhận là Apache Software License. Nhiều gói khác trong bảng sử dụng MIT, BSD hoặc PSF-2.0. Khi phân phối phần mềm sử dụng những gói này, cần tuân thủ điều kiện của giấy phép tương ứng, đặc biệt là giữ thông báo bản quyền và văn bản giấy phép theo yêu cầu.

### 3.3. Rủi ro khi phát triển phần mềm thương mại đóng mã nguồn

Dựa trên bảng hiện tại, chưa có bằng chứng về gói GPL hoặc AGPL trong môi trường được kiểm tra. Vì vậy, không nên kết luận rằng dự án này phải công bố toàn bộ mã nguồn do phụ thuộc GPL/AGPL. Tuy nhiên, việc sử dụng MPL 2.0 vẫn cần được rà soát nếu sửa đổi và phân phối các tệp thuộc phạm vi giấy phép. Các nghĩa vụ cụ thể phụ thuộc nội dung được sử dụng, cách tích hợp và cách phân phối phần mềm.

Đối với ứng dụng thương mại đóng mã nguồn, nhóm phát triển nên kiểm kê cả phụ thuộc trực tiếp và gián tiếp, xác minh các mục có giấy phép chưa rõ, lưu giữ thông báo pháp lý và kiểm tra giấy phép trước mỗi lần phát hành. Báo cáo tự động là bước sàng lọc hữu ích, nhưng không thay thế việc đọc giấy phép gốc và đánh giá cách sử dụng thực tế.

## 4. Tài liệu tham khảo

- pip-licenses: https://pypi.org/project/pip-licenses/
- Mozilla Public License 2.0: https://www.mozilla.org/en-US/MPL/2.0/
- GNU GPL v3.0: https://www.gnu.org/licenses/gpl-3.0.html
- GNU AGPL v3.0: https://www.gnu.org/licenses/agpl-3.0.html
- GNU LGPL v3.0: https://www.gnu.org/licenses/lgpl-3.0.html
