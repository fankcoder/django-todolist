#-*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名/账号")
    password = forms.CharField(label="密码",widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名/账号")
    email = forms.EmailField(label="邮件地址")
    password = forms.CharField(label="密码",widget=forms.PasswordInput)
    password2= forms.CharField(label='确认密码',widget=forms.PasswordInput)
    def pwd_validate(self,p1,p2):
        return p1==p2

class ChangepwdForm(forms.Form):
    old_pwd = forms.CharField(label="旧密码",widget=forms.PasswordInput)
    new_pwd = forms.CharField(label="新密码",widget=forms.PasswordInput)
    new_pwd2 = forms.CharField(label="确认新密码",widget=forms.PasswordInput)


