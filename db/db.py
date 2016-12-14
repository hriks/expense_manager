import psycopg2 as pg
import settings

database = settings.DATABASE
user = settings.USER
password = settings.PASSWORD
host = settings.PORT
port = settings.PORT


def get_connection():
    conn = pg.connect(
        database='cred_db',
        user='postgres',
        password='postgres',
        host='127.0.0.1',
        port=5432)
    return conn


def create_db():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE LOGS
       (USERID       TEXT    UNIQUE    NOT Null,
       NAME           TEXT    NOT NULL,
       EMAIL            TEXT     NOT NULL,
       PASSWORD        TEXT);''')
    print "Table created successfully"
    get_connection().commit()
    get_connection().close()


def insert_db(USER, NAME, EMAIL, PASSWORDV):
    connection = get_connection()
    cursor = connection.cursor()
    print "cur is created"
    query = """INSERT INTO LOGS(USERID,NAME,EMAIL,PASSWORD) VALUES('%s', '%s', '%s', '%s');"""
    query = query % (
        USER, NAME, EMAIL, PASSWORDV)
    print query
    cursor.execute(query)
    connection.commit()
    print "Records created successfully"


def user_alreadyexits(USER, NAME, EMAIL, PASSWORDV):
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT USERID from LOGS where USERID='%s';"""
    query = query % (USER, )
    cursor.execute(query)
    rows = cursor.fetchall()
    print rows
    try:
        if (len(rows) == 0):
            insert_db(USER, NAME, EMAIL, PASSWORDV)
        else:
            return 1
    except Exception as error:
        return error


def authenticate(username, password):
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT USERID, PASSWORD from LOGS where USERID='%s' and PASSWORD='%s';"""
    query = query % (username, password)
    cursor.execute(query)
    rows = cursor.fetchall()
    print rows
    try:
        if (rows[0][0] == username) and (rows[0][1] == password):
            return 1
        else:
            return 0
    except Exception as error:
        return error
    connection.close()


def select_db():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT USERID, FULLNAME, EMAILID, PASSWORD  from LOGINSS")
    rows = cursor.fetchall()
    for row in rows:
        print "User ID = ", row[0]
        print "Your Name = ", row[1]
        print "Registered Name = ", row[2]
        print "Password = ", row[3], "\n"
    print "Operation done successfully"
    cursor.close()


def update_db(id, ags, par):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE LOGINSS set ags = par where USERID=id")
    cursor.commit()
    print "Total number of rows updated :", cursor.rowcount

    cursor.execute("SELECT USERID, FULLNAME, EMAILID, PASSWORD  from LOGINSS")
    rows = cursor.fetchall()
    for row in rows:
        print "USER ID = ", row[0]
        print "FULL NAME = ", row[1]
        print "REGISTERED EMAIL ID = ", row[2]
        print "PASSWORD = ", row[3], "\n"

        print "Operation done successfully"
        cursor.close()


def delete_db(useri):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE from LOGINSS where USERID=useri;")
    cursor.commit()
    print "Total number of rows deleted :", cursor.rowcount
    cursor.execute("SELECT USERID, FULLNAME, EMAILID, PASSWORD  from LOGINSS")
    rows = cursor.fetchall()
    for row in rows:
        print "USER ID = ", row[0]
        print "FULL NAME = ", row[1]
        print "REGISTERED EMAIL = ", row[2]
        print "PASSWORD = ", row[3], "\n"

    print "Operation done successfully"
    cursor.close()
