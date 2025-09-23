import os
import django
from django.conf import settings
from django.db import connection

# Cấu hình Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')
django.setup()

# Kiểm tra các bảng
with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Danh sách bảng:", tables)

    # Kiểm tra bảng accounts_user
    try:
        from accounts.models import User
        users = User.objects.all()
        print("Danh sách người dùng:", [(u.id, u.username, u.email, u.password) for u in users])
    except Exception as e:
        print("Lỗi kiểm tra bảng accounts_user:", e)