# Sử dụng một image Python làm nền
FROM python:3.9-slim

# Thiết lập biến môi trường
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Cài đặt các thư viện phụ thuộc
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ code dự án vào container
COPY . /app/

# Chạy lệnh
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]