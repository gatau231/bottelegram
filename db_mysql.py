import get_db_connection
import datetime


def insertData(chat_id, file_path, barcode):
    connection = get_db_connection.getConnection()

    sql = "INSERT INTO images (chat_id, file_path, barcode, created_at)" \
          + " VALUES (%s, %s, %s, %s)"
    try:
        # объект для работы с БД
        cursor = connection.cursor()

        cursor.execute(sql, (chat_id, file_path, barcode, datetime.datetime.now()))

        connection.commit()
    finally:
        connection.close()
