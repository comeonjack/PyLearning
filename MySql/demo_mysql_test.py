import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="root", 
    #auth_plugin='mysql_native_password'
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

mycursor.execute("use db_library")

mycursor.execute("select * from t_book")
for x in mycursor:
    print(x)