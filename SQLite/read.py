import sqlite3
def readData():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    a = c.execute('select * from RAJ;')
    x = a.fetchall()
    for cv in x:
        print ('ID = '+ str(cv[0])+"\tText = "+ cv[1]+"\n" )