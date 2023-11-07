import mysql.connector

# Устанавливаем соединение с базой данных
conn = mysql.connector.connect(
    host='158.160.56.43',  # Укажите адрес хоста базы данных
    user='user',  # Укажите имя пользователя для подключения к базе данных
    password='0000',  # Укажите пароль пользователя
    database='test'  # Укажите имя базы данных
)

# Создаем объект cursor для выполнения SQL-запросов
cursor = conn.cursor()

# Пример выполнения SQL-запроса для получения данных из таблицы
sql_query = "SELECT * FROM users"  # Укажите имя вашей таблицы
cursor.execute(sql_query)

# Получаем все строки результата запроса
results = cursor.fetchall()

# Выводим результаты
for row in results:
    print(row)

# Закрываем соединение с базой данных
conn.close()
