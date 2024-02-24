import psycopg2

def show_databases(host, port, user, password, database):
    # Підключення до бази даних PostgreSQL
    connection = psycopg2.connect("dbname=test user=pavlenko password=1203qazxsw host=localhost")
    
    cursor = connection.cursor()

    # Виконання запиту для отримання імен баз даних
    cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false AND datallowconn = true;")
    
    # Отримання результатів та виведення імен баз даних
    databases = cursor.fetchall()
    print("Список створених баз даних:")
    for db in databases:
        print(db[0])

    # Закриття з'єднання
    connection.close()

# Виклик функції з параметрами для підключення до PostgreSQL
show_databases(host='your_host', port='your_port', user='your_user', password='your_password', database='your_database')

def show_tables(host, port, user, password, database):
    # Підключення до бази даних PostgreSQL
    connection = psycopg2.connect("dbname=test user=pavlenko password=1203qazxsw host=localhost")
    
    cursor = connection.cursor()

    # Виконання запиту для отримання імен таблиць
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    
    # Отримання результатів та виведення імен таблиць
    tables = cursor.fetchall()
    print("Список створених таблиць:")
    for table in tables:
        print(table[0])

    # Закриття з'єднання
    connection.close()

# Виклик функції з параметрами для підключення до PostgreSQL та вказання конкретної бази даних
print("postgres\n")
show_tables(host='your_host', port='your_port', user='your_user', password='your_password', database='postgres')
print("test-pavl\n")
show_tables(host='your_host', port='your_port', user='your_user', password='your_password', database='test-pavl')
print("pavl_database\n")
show_tables(host='your_host', port='your_port', user='your_user', password='your_password', database='pavl_database')
print("Test\n")
show_tables(host='your_host', port='your_port', user='your_user', password='your_password', database='Test')
print("test\n")
show_tables(host='your_host', port='your_port', user='your_user', password='your_password', database='test')
