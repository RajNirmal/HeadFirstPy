import read as select
import sqlite3
from testClass import Hello as deb
con = sqlite3.connect('test.db')
con.execute('''Create table if not exists RAJ (ID INT,NAME TEXT)''')
# a = '''Insert into RAJ (ID,Name) values (120,\'H5454ello\');'''
# print(a)
# con.execute(a)
# con.commit()
A = deb()
A.printHello("This works SUCKA")
# select.readData()
con.close()
