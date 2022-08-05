"""ログインでのフォームを定義する

"""

from django import forms

class toroku_form(forms.Form):
    
    #ユーザーID
    id = forms.CharField(
        label='ID', 
        required=True, 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ユーザー名もしくはメールアドレス',
                'class': 'toroku_input'
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
                'class': 'toroku_input'
            }
        )
    )
    #再パスワード
    re_password = forms.CharField(
        label='RE_PASS', 
        required=True,
        min_length=8, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'パスワード',
                'class': 'toroku_input'
            }
        )
    )
