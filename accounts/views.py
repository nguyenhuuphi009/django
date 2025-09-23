from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Đăng ký thành công! Vui lòng đăng nhập.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"Attempting to authenticate: {username}, {password}")
            user = authenticate(request, username=username, password=password)
            print(f"User authenticated: {user}")
            if user is not None:
                login(request, user)
                messages.success(request, 'Đăng nhập thành công!')
                return redirect('home')
            else:
                print(f"Users with {username}: {list(User.objects.filter(username=username).values('password'))}")
                messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def home(request):
    return render(request, 'accounts/home.html', {'user': request.user})