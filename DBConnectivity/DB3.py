from mysql import connector
myDbConnection=connector.connect(host='localhost',user='root',password='root',database='pythonmagnus')

c1 = myDbConnection.cursor()

c1.execute("select * from employee")
result = c1.fetchall()
print(result)

for i in result:
     print(i)
myDbConnection.close()
