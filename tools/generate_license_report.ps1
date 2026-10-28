$ErrorActionPreference = 'Stop'

# Run this script from the root of the PMMNM_LeDucManh repository.
# It uses the repository's .venv so the report reflects a real, reproducible environment.
$python = Join-Path (Get-Location) '.venv\Scripts\python.exe'
$cli = Join-Path (Get-Location) '.venv\Scripts\pip-licenses.exe'
$report = Join-Path (Get-Location) 'bai_tap\bai_02_licenses.md'

if (-not (Test-Path $python)) {
    throw "Cannot find .venv Python at $python. Run this script from the repository root and activate/create .venv first."
}

New-Item -ItemType Directory -Force -Path (Split-Path $report) | Out-Null

Write-Host 'Installing audit tool and a practical set of Python packages in .venv...' -ForegroundColor Cyan
& $python -m pip install --upgrade pip-licenses Flask requests pytest python-dotenv SQLAlchemy rich black
if ($LASTEXITCODE -ne 0) { throw 'pip install failed; report was not generated.' }

$packages = & $python -m pip list --format=json | ConvertFrom-Json
if ($packages.Count -lt 10) {
    throw "Only $($packages.Count) distributions detected after installation. Install/check packages before submitting; assignment requires at least 10 packages."
}

$pythonInfo = & $python -c "import sys; print(sys.version.split()[0] + ' | ' + sys.executable)"
$date = Get-Date -Format 'yyyy-MM-dd HH:mm:ss K'

@"
# Bài 2.2 — Rà soát giấy phép các gói Python

- Thời điểm kiểm kê: $date
- Python: $pythonInfo
- Số distribution nhìn thấy trong môi trường: $($packages.Count)
- Phương pháp: `pip-licenses --format=markdown --with-urls --with-authors` chạy trong `.venv` của repository.

## Bảng kiểm kê từ môi trường thực tế

"@ | Set-Content -Path $report -Encoding utf8

$table = & $cli --format=markdown --with-urls --with-authors --from=mixed
if ($LASTEXITCODE -ne 0) { throw 'pip-licenses failed; review the environment and retry.' }
$table | Add-Content -Path $report -Encoding utf8

@'

## Phân tích copyleft và rủi ro với phần mềm thương mại đóng mã nguồn

Sau khi xem bảng phía trên, hãy phân loại theo giấy phép được công cụ ghi nhận và xác minh văn bản gốc khi tên giấy phép chưa rõ. Đặc biệt kiểm tra GPL và AGPL; LGPL và MPL cần được đánh giá riêng vì phạm vi copyleft khác nhau.

- **Gói GPL/AGPL có phát hiện:** ghi tên gói, phiên bản, giấy phép và cách dự án dùng/phân phối gói đó. Không kết luận chỉ từ tên gói rằng toàn bộ ứng dụng bắt buộc phải công bố mã nguồn; phạm vi nghĩa vụ phụ thuộc cách tích hợp và phân phối.
- **Nếu không có GPL/AGPL trong bảng:** ghi “Không phát hiện gói GPL/AGPL trong môi trường được kiểm tra tại thời điểm này.” Kết quả chỉ phản ánh môi trường hiện tại, không phải kiểm toán toàn bộ mọi thành phần có thể được đưa vào sản phẩm.
- **Rủi ro:** khi phân phối phần mềm bao gồm tác phẩm thuộc phạm vi GPL, có thể phát sinh nghĩa vụ cung cấp mã nguồn tương ứng và tuân thủ điều kiện cấp phép. AGPL có thêm điều khoản về tương tác mạng trong những trường hợp nhất định. Doanh nghiệp cần giữ thông báo bản quyền, kiểm tra NOTICE khi áp dụng, ghi nhận nguồn gốc phụ thuộc và rà soát giấy phép trước mỗi bản phát hành.

## Tài liệu tham khảo

- [pip-licenses trên PyPI](https://pypi.org/project/pip-licenses/)
- [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html)
- [GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.html)
- [GNU LGPL v3.0](https://www.gnu.org/licenses/lgpl-3.0.html)
'@ | Add-Content -Path $report -Encoding utf8

Write-Host "Report generated: $report" -ForegroundColor Green
Write-Host "Review the generated table and the copyleft notes before committing." -ForegroundColor Yellow
