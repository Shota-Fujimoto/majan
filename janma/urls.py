"""JanmaアプリのURLを管理
"""

from django.urls import path
from .views.login import index, auth

app_name = 'janma'

urlpatterns = [
    #ログイン
    path('login/', index, name='janma_login'),
    #ログイン認証
    path('auth/', auth, name='login_auth')
]