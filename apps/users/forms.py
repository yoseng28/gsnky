from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # 需要和html中的form字段一致
    user_name = forms.CharField(required=True)
    user_password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    user_name = forms.CharField(required=True)
    user_email = forms.EmailField(required=True)
    user_password = forms.CharField(required=True)
    # captcha = CaptchaField(error_messages={'invalid:': '验证码错误！'})


