import psycopg2

def user_exists(cursor, user_id):
    # Перевірка існування користувача за його id
    cursor.execute('SELECT EXISTS(SELECT 1 FROM users WHERE id = %s)', (user_id,))
    return cursor.fetchone()[0]

def get_user_tasks(cursor, user_id):
    # Отримання задач користувача за його id
    cursor.execute('SELECT id, title, description, status_id FROM tasks WHERE user_id = %s', (user_id,))
    return cursor.fetchall()

def delete_user(user_id):
    try:
        # Підключення до бази даних
        connection = psycopg2.connect("dbname=test user=pavlenko password=1203qazxsw host=localhost")
        cursor = connection.cursor()

        # Перевірка існування користувача перед видаленням
        if user_exists(cursor, user_id):
            # Отримання задач користувача перед видаленням
            user_tasks_before = get_user_tasks(cursor, user_id)
            
            # Видалення користувача за його id
            cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))

            # Отримання задач користувача після видалення
            user_tasks_after = get_user_tasks(cursor, user_id)

            print(f"Користувач з id={user_id} успішно видалений.")
            print("Задачі користувача перед видаленням:")
            print(user_tasks_before)
            print("Задачі користувача після видалення:")
            print(user_tasks_after)
            
            # Збереження змін та закриття з'єднання
            connection.commit()
            cursor.close()
            connection.close()
        else:
            print(f"Користувача з id={user_id} не існує.")
            # Закриття курсора та з'єднання в разі відсутності користувача
            cursor.close()
            connection.close()
    except Exception as e:
        print(f"Помилка: {e}")

# Приклад використання: видалення користувача з id=1
delete_user(134)