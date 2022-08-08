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
                'placeholder': 'メールアドレス',
                'class': 'form_input'
            }
        )
    )
    #パスワード
    password = forms.CharField(
        label='パスワード', 
        required=True,
        min_length=8, 
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '8文字以上20文字以内',
                'class': 'form_input'
            }
        )
    )
