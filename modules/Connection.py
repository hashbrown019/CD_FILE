import sqlite3

class sqlite:
	def init_db():
		conn = None
		try:
			conn = sqlite3.connect('assets\\db\\db.db')
		except Error as e:
			print(e)
		return conn

	def do(sql):
		conn = sqlite.init_db()
		cur = conn.cursor()
		cur.execute(sql)
		conn.commit()
		return cur.lastrowid

	def select(sql):
		conn = sqlite.init_db()
		cur = conn.cursor()
		cur.execute(sql)
		rows = cur.fetchall()
		return rows