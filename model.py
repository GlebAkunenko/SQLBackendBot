import MySQLdb

conn = MySQLdb.connect(
      host="rc1b-jcgbdwdg2bg0a6vc.mdb.yandexcloud.net",
      port=3306,
      db="db",
      user="user",
      passwd="12121212",
      ssl={'ca': 'root.crt'})

cursor = conn.cursor()



def do_query(query: str) -> str:
	cursor.execute(query)
	results = cursor.fetchall()
	return results



