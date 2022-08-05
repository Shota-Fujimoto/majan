"""ログインでのフォームを定義する

"""

from django import forms

class login_form(forms.Form):
    
    #ユーザーID
    id = forms.CharField(
        label='ID', 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ユーザー名もしくはメールアドレス',
                'class': 'login_input'
            }
        )
    )
    #パスワード
    password = forms.CharField(
        label='PASS', 
        required=True,
        min_length=8, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'パスワード',
                'class': 'login_input'
            }
        )
    )
