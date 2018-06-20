import get_db_connection

connection = get_db_connection.getConnection()
print("Connect successful!")

sql_select = "SELECT * FROM test"
sql_insert = "INSERT INTO test (text)" \
             + " VALUES (%s)"

try:
    # объект для работы с БД
    cursor = connection.cursor()

    cursor.execute(sql_select)

    print("cursor:description: ", cursor.description)
    print()

    for row in cursor:
        print("---------")
        print("Row: ", row)
        print("ID: ", row["id"])
        print("Text: ", row['text'])

    # cursor.execute(sql_insert, 'ten')
    #
    # cursor.execute(sql_select)
    #
    # print("cursor:description: ", cursor.description)
    # print()
    #
    # for row in cursor:
    #     print("---------")
    #     print("Row: ", row)
    #     print("ID: ", row["id"])
    #     print("Text: ", row['text'])
    #
    # connection.commit()

finally:
    connection.close()
