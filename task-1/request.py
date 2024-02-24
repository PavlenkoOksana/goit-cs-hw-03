import psycopg2

# Параметри підключення до бази даних
db_params = {
    'dbname': 'test',
    'user': 'pavlenko',
    'password': '1203qazxsw',
    'host': 'localhost',
}

# Підключення до бази даних
connection = psycopg2.connect(**db_params)
cursor = connection.cursor()

def user_exists(cursor, user_id):
    # Перевірка існування користувача за його id
    cursor.execute('SELECT EXISTS(SELECT 1 FROM users WHERE id = %s)', (user_id,))
    return cursor.fetchone()[0]


def get_tasks_by_user_id(user_id):
    if user_exists(cursor, user_id):
        try:
            # SQL-запит для отримання завдань користувача за його user_id
            sql_query = f"SELECT * FROM tasks WHERE user_id = {user_id};"

            # Виконання запиту та отримання результатів
            cursor.execute(sql_query)
            tasks = cursor.fetchall()

            # Виведення результатів
            for task in tasks:
               print(task)

        except psycopg2.Error as e:
            print(f"Помилка виконання SQL-запиту: {e}")
    else:
            print(f"Користувача з id={user_id} не існує.")   


def get_tasks_by_status(status):
    try:
        # SQL-запит для отримання завдань користувача за його user_id
        sql_query = f"SELECT * FROM tasks WHERE status_id = (SELECT id FROM status WHERE name = %s);"

        # Виконання запиту та отримання результатів
        cursor.execute(sql_query, (status,))
        tasks = cursor.fetchall()

        # Виведення результатів
        for task in tasks:
            print(task)

    except psycopg2.Error as e:
        print(f"Помилка виконання SQL-запиту: {e}")

    

# Виклик функції для отримання завдань для певного користувача
get_tasks_by_user_id(129)
get_tasks_by_user_id(135)
get_tasks_by_status('new')




# Закриття курсора (підключення залишається відкритим)
cursor.close()