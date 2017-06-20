import read as select
import sqlite3

con = sqlite3.connect('test.db')
con.execute('''Create table if not exists RAJ (ID INT,NAME TEXT)''')
# a = '''Insert into RAJ (ID,Name) values (120,\'H5454ello\');'''
# print(a)
# con.execute(a)
# con.commit()
select.readData()
con.close()
