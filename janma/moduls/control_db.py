"""DBへの接続、カーソルを定義
"""

#インポート
import pymysql.cursors

def connect():
    """DB接続
        DBの接続を行う
    戻り値:
        DBインスタンス
    """
    con_db = pymysql.connect(
        host='localhost',
        user='root',
        password='Sankyo*0118',
        db='sankyo_db',
        charset='utf8')
    con_db.autocommit(False)
    return con_db

#DBの切断を行う
def disconnect(con_db):
    """DB切断
        DBの切断を行う
    引数:
        con_db:DBインスタンス
    """
    con_db.close()

def cursor(con_db, is_dict):
    """カーソル設定
        カーソルの設定を行う
    引数:
        con_db:DBインスタンス
        is_dict(bool):True:dictionary型のデータ/False:tuple型のデータ
    戻り値:
        カーソル
    """
    if is_dict:
        return con_db.cursor(pymysql.cursors.DictCursor)
    else:
        return con_db.cursor()

def debug(cursor, sql, param):
    """SQLクエリデバッグ
        クエリのデバッグ出力を行う
    引数:
        cursor:カーソル
        sql(str):sqlクエリ
        param(dictionary):パラメータ
    """
    sql = cursor.mogrify(sql, param)
    print(sql)