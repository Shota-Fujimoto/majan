"""パスワード再設定画面の処理を行う
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request:dict):
    """初期表示
    """

    #変数
    title  = 'パスワード再設定'
    form = None
    err_msg = ''
    contents = {}
    temp = ''

    try:
        if request.method == 'GET':

            pass

    except:
        err_msg = "＊エラーが発生しました"

    return render(request, temp, contents)
