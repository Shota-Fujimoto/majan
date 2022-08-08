"""ログイン画面での制御を行う
"""

#インポート
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..forms.login_form import login_form
from ..moduls import control_db


###################################################################################################
#イベント関数
###################################################################################################
def index(request:dict):
    """ログイン画面の初期表示を行う
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
    title  = 'ログイン'
    form = None
    err_msg = ''
    contents = {}
    temp = 'auth.html'
    mode = 'login'

    try:
        if request.method == 'POST':
            form = login_form(request.POST)
            form.is_valid()

            #登録確認
            ret, err_msg = check_id_pass(form.data)
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
def check_id_pass(data):
    """ログイン画面入力のID、PASSが存在し、合致するかをチェック
    """

    #変数
    ret = True
    err_msg = ''
    con_db = control_db.connect()

    try:
        #検索パラメータ
        param = {
            'mail_address': data['id'].replace(' ', ''),
            'password': data['password'].replace(' ', '')
        }

        #検索SQL
        sql = """
            SELECT
                COUNT(*) AS cnt
            FROM
                janma_user
            WHERE
                mail_address = %(mail_address)s
            AND
                password = %(password)s
        """

        #SQL実行
        with control_db.cursor(con_db, True) as cursor:
            cursor.execute(sql, param)
            cnt = cursor.fetchone()

        #存在確認
        if cnt['cnt'] == 0:
            ret = False
            err_msg = '認証に失敗しました。'

    except:
        ret = False
        err_msg = 'エラーが発生しました。'

    return ret, err_msg
