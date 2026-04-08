Yêu cầu hệ thống

Python: Phiên bản 3.10 trở lên.

IDE: Visual Studio Code (VS Code).

Extensions: Cài đặt extension Python và Jupyter trên VS Code.

## 1. Khởi tạo môi trường ảo (Virtual Environment)
```bash
# Tạo môi trường ảo tên là 'venv'
python -m venv venv
```

## 2. Kích hoạt môi trường ảo
Windows (PowerShell):
```PowerShell
.\venv\Scripts\Activate.ps1
```
Windows (Command Prompt):
```DOS
.\venv\Scripts\activate
```
macOS/Linux:
```bash
source venv/bin/activate
```

## 3.Cài đặt các thư viện cần thiết
Sau khi kích hoạt venv (bạn sẽ thấy chữ (venv) ở đầu dòng lệnh), tiến hành cài đặt:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 4. Chạy Notebook 
Chạy Notebook trong VS Code
Để chạy các file .ipynb một cách mượt mà:

Mở file notebook (ví dụ: 5.4.ipynb) trong VS Code.

Nhìn vào góc trên bên phải của cửa sổ editor, chọn "Select Kernel".

Chọn "Python Environments..." và trỏ đến môi trường ảo venv bạn vừa tạo.

Nhấn "Run All" để thực thi các cell.

