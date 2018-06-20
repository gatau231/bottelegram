from pyzbar.pyzbar import decode
from PIL import Image
import db_mysql


def detect(path, chat_id):
    data = decode(Image.open("tmp/" + path))
    if data:
        # штрихкод в переменной data имеет тип bytes, поэтому конвертируем в str
        barcode = data[0][0].decode("utf-8")
        # добавляем запись в БД
        db_mysql.insertData(chat_id, path, barcode)
    else:
        barcode = 'Barcode not found'
    return barcode
