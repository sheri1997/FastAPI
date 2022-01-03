"""Here We are Practising the DataBase Execution
    using pymysql"""
import errno

import mysql.connector
from mysql.connector import errorcode


class DataBase:
    @staticmethod
    def connection_database():
        conn = ""
        first_name = 'Shreesh'
        last_name = 'Pandey'
        mobile_no = '94549774891'
        email_id = 'shvspandey@gmail.com'
        location = 'Lucknow'
        state = 'Uttar Pradesh'
        try:
            print("Hello")
            conn = mysql.connector.connect(host='127.0.0.1', user='root', port='3306', password='9454977489',
                                           database='fastapi')
            print(conn)
            cursor = conn.cursor()
            sql_query = (
                "insert into details""(first_name,last_name,mobile_no,email_id,location,state)""values(%("
                "first_name)s,%(last_name)s,%(mobile_no)s,%(email_id)s,%(location)s,%(state)s)")
            info = {
                'first_name': first_name,
                'last_name': last_name,
                'mobile_no': mobile_no,
                'email_id': email_id,
                'location': location,
                'state': state
            }
            cursor.execute(sql_query, info)
            conn.commit()
        except mysql.connector.Error as er:
            if er.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something Wrong with Username and password")
            elif er.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(er)
        finally:
            conn.close()
        return conn



# ss = DataBase.connection_database()
# print(ss)


