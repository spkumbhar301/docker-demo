import mysql.connector

mydb = mysql.connector.connect(
	host = "mysql1",
	user = "root",
 	passwd ="password",
	auth_plugin = "mysql_native_password"
)
testcursor = mydb.cursor()
testcursor.execute("CREATE DATABASE studentdb")

testcursor.execute("SHOW DATABASES")

for x in testcursor:
	print(x)
