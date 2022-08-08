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
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '8文字以上20文字以内',
                'class': 'form_input'
            }
        )
    )
    #再パスワード
    re_password = forms.CharField(
        label='確認用パスワード', 
        required=True,
        min_length=8, 
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '8文字以上20文字以内',
                'class': 'form_input'
            }
        )
    )
