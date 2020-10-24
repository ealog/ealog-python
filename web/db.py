import sqlite3
conn = sqlite3.connect('test.db')

cur = conn.cursor()


cur.execute("CREATE TABLE demo(num int,str varchar(20));")

cur.execute("INSERT INTO demo VALUES (%d,'%s')" %(1,'aaa'))
cur.execute("INSERT INTO demo VALUES (%d,'%s')" %(2,'bbb'))
cur.execute("INSERT INTO demo VALUES (%d,'%s')" %(3,'ccc'))

cur.execute("UPDATE demo SET str = '%s'  WHERE num = %d" %('ddd',3))

cur.execute("select * from demo")