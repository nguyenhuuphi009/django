from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]  # Đảm bảo có dấu đóng ngoặc vuông và không có lỗi cú pháp