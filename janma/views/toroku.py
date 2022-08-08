"""新規登録画面での制御を行う
"""

#インポート
from operator import truediv
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime

from ..forms.toroku_form import toroku_form
from ..moduls import control_db


###################################################################################################
#イベント関数
###################################################################################################
def index(request:dict):
    """新規登録画面の初期表示を行う
    """

    #変数
    title  = '新規登録'
    form = None
    err_msg = ''
    contents = {}
    temp = 'auth.html'
    mode = 'toroku'

    try:
        if request.method == 'GET':
            form = toroku_form()

    except:
        err_msg = "＊エラーが発生しました"

    contents = {'title': title, 'form': form, 'err_msg': err_msg, 'mode': mode}
    return render(request, temp, contents)


def add(request:dict):
    """新規登録処理を行う
    """

    #変数
    title  = '新規登録'
    form = None
    err_msg = ''
    contents = {}
    temp = 'auth.html'
    mode = 'toroku'

    try:
        if request.method == 'POST':
            form = toroku_form(request.POST)
            form.is_valid()

            #登録確認
            ret, err_msg = check(form.data)
            if not ret:
                contents = {'title': title, 'form': form, 'err_msg': err_msg, 'mode': mode}
                return render(request, temp, contents)

            ret, err_msg = add_user(form.data)
            if not ret:
                err_msg = '認証に失敗しました。'
                contents = {'title': title, 'form': form, 'err_msg': err_msg, 'mode': mode}
                return render(request, temp, contents)

            #認証成功でメニュー画面へ

    except:
        err_msg = "＊エラーが発生しました"

    contents = {'title': title, 'form': form, 'err_msg': err_msg, 'mode': mode}
    return render(request, temp, contents)


###################################################################################################
#関数
###################################################################################################
def check(data):
    """新規登録画面入力のチェックを行う
    """

    #変数
    ret = True
    err_msg = ''
    con_db = control_db.connect()
    param = {
        'mail_address': data['mail_address'].replace(' ', ''),
        'password': data['password'].replace(' ', '')
    }

    try:
        #メールアドレスが既に登録済みの場合
        sql = """
            SELECT
                COUNT(*) AS cnt
            FROM
                janma_user
            WHERE
                mail_address = %(mail_address)s
        """

        with control_db.cursor(con_db, True) as cursor:
            cursor.execute(sql, param)
            cnt = cursor.fetchone()
        
        if cnt['cnt'] != 0:
            ret = False
            err_msg = '既に登録のあるメールアドレスです。'

        #パスワード、確認用パスワードが合致するか
        if data['password'].replace(' ', '') != data['re_password'].replace(' ', ''):
            ret = False
            err_msg = 'パスワードが一致しません。'

    except:
        err_msg = 'エラーが発生しました。'

    return ret, err_msg

def add_user(data):
    """画面入力のID、PASSがそんざいし、合致するかをチェック
    """

    #変数
    ret = True
    err_msg = ''
    con_db = control_db.connect()

    try:
        #登録パラメータ
        date = datetime.datetime.now()
        param = {
            'mail_address': data['mail_address'].replace(' ', ''),
            'password': data['password'].replace(' ', ''),
            'last_login_date': date,
            'sakusei_date': date
        }
        #追加SQL
        sql = """
            INSERT INTO janma_user (
                mail_address,
                password,
                last_login_date,
                sakusei_date
            ) VALUES (
                %(mail_address)s,
                %(password)s,
                %(last_login_date)s,
                %(sakusei_date)s
            )
        """

        #SQL実行
        with control_db.cursor(con_db, True) as cursor:
            cursor.execute(sql, param)

    except:
        ret = False
        err_msg = 'エラーが発生しました。'

    return ret, err_msg