# coding=utf-8
__author__ = 'andong'
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30,label="用户名：")   # 按照User类的要求
    password = forms.CharField(widget=forms.PasswordInput,label="密码：")
    email = forms.EmailField(required=False,label="邮箱：")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,label="用户名：")
    password = forms.CharField(widget=forms.PasswordInput,label="密码：")

class ModifyPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput,label="旧密码：")
    password = forms.CharField(widget=forms.PasswordInput,label="新密码：")
    re_password = forms.CharField(widget=forms.PasswordInput,label="重复密码：")

class AddCommentForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'span4'}),max_length=30,label="标题")
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'span6'}),label="内容")