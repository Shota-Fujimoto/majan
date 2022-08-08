"""JanmaアプリのURLを管理
"""

from django.urls import path
from .views import login, toroku

app_name = 'janma'

urlpatterns = [
    #ログイン
    path('login/', login.index, name='login_index'),
    #ログイン認証
    path('login/auth/', login.auth, name='login_auth'),
    #新規登録
    path('toroku/', toroku.index, name='toroku_index'),
    #新規登録
    path('toroku/add/', toroku.add, name='toroku_add'),
]