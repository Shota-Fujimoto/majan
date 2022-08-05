"""メニュー画面での制御を行う
    
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request:dict):
    """メニュー画面の初期表示を行う
    """

    #変数
    title  = ''
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
