"""ログイン画面での制御を行う
    
"""

#インポート
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..forms.login_form import login_form


def index(request:dict):
    """ログイン・新規登録画面の初期表示を行う
    """

    #変数
    title  = 'ログイン'
    form = None
    err_msg = ''
    contents = {}
    temp = 'auth.html'
    mode = 'login'

    try:
        if request.method == 'GET':
            form = login_form()

    except:
        err_msg = "＊エラーが発生しました"

    contents = {'title': title, 'form': form, 'err_msg': err_msg, 'mode': mode}
    return render(request, temp, contents)


def auth(request:dict):
    """ログイン認証処理を行う
    """

    #変数
    title  = 'ログイン・新規登録'
    form = None
    err_msg = ''
    contents = {}
    temp = ''
    mode = 'login'

    try:
        if request.method == 'POST':
            form = login_form(request.POST)
            form.is_valid()

            #登録確認


    except:
        err_msg = "＊エラーが発生しました"

    contents = {'title': title, 'form': form, 'err_msg': err_msg, 'mode': mode}
    return render(request, temp, contents)