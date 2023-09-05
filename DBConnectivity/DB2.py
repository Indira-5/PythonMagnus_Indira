from mysql import connector
myDbConnection=connector.connect(host='localhost',user='root',password='root',database='pythonmagnus')

c1=myDbConnection.cursor()

#c1.execute("create table employee (empno int,ename varchar(40),sal int,deptno int)")
#c1.execute("insert into employee values(101, 'abc', 2500, 1)")
#c1.execute("insert into employee values(102,'def',3500,2)")
#sql = "insert into employee values(%s,%s,%s,%s)"
#data = (103,'ghf',3700,3)
#c1.execute(sql,data)

vempno = int(input("Enter the Empno Value:"))
vename = input("Enter the Ename Value:")
vsal = int(input("Enter the Sal Value:"))
vdeptno = int(input("Enter the deptno Value:"))

c1.execute("insert into employee (empno,ename,sal,deptno) values(%s,%s,%s,%s)",(vempno,vename,vsal,vdeptno))

myDbConnection.commit()
myDbConnection.close()
