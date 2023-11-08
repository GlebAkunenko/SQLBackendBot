import mysql.connector
import config

# Устанавливаем соединение с базой данных
conn = mysql.connector.connect(
    host=config.server_address,  # Укажите адрес хоста базы данных
    user='user',  # Укажите имя пользователя для подключения к базе данных
    password='0000',  # Укажите пароль пользователя
    database='test'  # Укажите имя базы данных
)

# Создаем объект cursor для выполнения SQL-запросов
cursor = conn.cursor()


def do_query(query: str) -> str:
	cursor.execute(query)
	results = cursor.fetchall()
	return results



