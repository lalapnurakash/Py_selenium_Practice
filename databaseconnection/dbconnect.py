import os
import sqlite3

import pyodbc

# Trusted Connection to Named Instance
# conn= pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
#                             'SERVER=WIN-7RVMQN2\SQLEXPRESS'
#                             'DATABASE=AdventureWorks2019;'
#                             'Trusted_Connection=yes;')
# print(os.getcwd())
# mydb=c.connect(host='localhost',user='root',passwd='12345678')
print(pyodbc.dataSources())



# import pyodbc
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};'
                      'SERVER=  SERVER=WIN-7RVMQN2\SQLEXPRESS;'
                      'DATABASE= AdventureWorks2019;'
                      'Trusted_connection = yes;'
                      )
# pyodbc.connect("Driver = {SQL Server Native Client 11.0};"
#                "Server = Server_Name;"
#                "Database = Database_Name;"
#                "username = User_Name;"
#                "password = User_Password;"
#                "Trusted_Connection = yes;")
#


conn.cursor()
conn.execute("use AdventureWorks2019")

conn.execute("select * from  HumanResources.Employee;")
#'uid=.\adminhyd'