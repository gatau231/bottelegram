import pymysql.cursors


# функция возвращает соединение с БД
def getConnection():
    # параметры соединения
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='0000',
                                 db='barcodes',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
