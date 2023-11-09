import MySQLdb

conn = MySQLdb.connect(
      host="rc1b-jcgbdwdg2bg0a6vc.mdb.yandexcloud.net",
      port=3306,
      db="db",
      user="user",
      passwd="12121212",
      ssl={'ca': 'root.crt'})



def do_query(query: str) -> str:
	cursor = conn.cursor()
	try:
		cursor.execute(query)
		conn.commit()
	except Exception as e:
		conn.rollback()
		return str(e)
	results = cursor.fetchall()
	return results



