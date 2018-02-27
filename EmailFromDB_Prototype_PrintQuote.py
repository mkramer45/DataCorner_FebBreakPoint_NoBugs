import smtplib
import sqlite3
import sys
reload(sys)
sys.setdefaultencoding('utf8')

conn = sqlite3.connect('StriveDB.db')
cursor = conn.cursor()
cur2 = cursor.execute('SELECT Msg FROM Motivational')
info2 = cur2.fetchall()

y = [x[0].encode("utf-8") for x in info2]

print str(y)[1:-1]