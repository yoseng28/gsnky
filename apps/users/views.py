from django.contrib import auth
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from django.views.generic.base import View

from users.forms import RegisterForm, LoginForm


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect('/')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('user_name')
            user_password = request.POST.get('user_password')
            user = auth.authenticate(username=user_name, password=user_password)
            if user is not None:
                auth.login(request, user)
                request.session['username'] = user_name
                return redirect('/')
            else:
                return render(request, 'login.html', {'message_error': '用户名或密码错误！'})
        else:
            return render(request, 'login.html', {
                'login_error': login_form,
                'message_error': '登录信息有误！'
            })


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('user_name')
            user_password = request.POST.get('user_password')
            user_email = request.POST.get('user_email')

            user = User.objects.filter(Q(username=user_name) | Q(email=user_email))
            if user:
                return render(request, 'register.html', {
                    'register_error': register_form,
                    'message_error': '该用户名、邮箱已注册！'
                })

            user = User.objects.create_user(username=user_name, password=user_password, email=user_email)
            user.save()

            # 添加到session
            request.session['username'] = user_name
            # 调用auth登录
            auth.login(request, user)
            # 重定向到首页
            return redirect('/')


# 自定义登录
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            print(e)
            return None
