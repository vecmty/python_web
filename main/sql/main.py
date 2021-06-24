import email

import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successfully connected")
    print("#" * 20)

    try:

        # # create table
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users` (id int AUTO_INCREMENT, name varchar(32), password varchar(32), email varchar(32), PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")
        #
        #
        # # insert data
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Aaddddnna', '1213313', 'anna@aaaa');"
        #     cursor.execute(insert_query)
        #     connection.commit()
        #
        #
        # # update data
        # with connection.cursor() as cursor:
        #     update_table_query = "UPDATE `users` SET password = 'xxxyyyyxx' WHERE id = 5;"
        #     cursor.execute(update_table_query)
        #     connection.commit()
        #
        #
        # # delete data
        # with connection.cursor() as cursor:
        #     delete_table_query = "DELETE FROM `users` WHERE id = 5"
        #     cursor.execute(delete_table_query)
        #     connection.commit()
        #
        #
        # # drop table
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `users`;"
        #     cursor.execute(drop_table_query)
        #
        #
        # select all data from table
        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `users`"
            cursor.execute(select_all_rows)
            # cursor.execute("SELECT * FROM `users`")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("#" * 20)


    finally:
        connection.close()

except Exception as ex:
    print("Connection refused")
    print(ex)
