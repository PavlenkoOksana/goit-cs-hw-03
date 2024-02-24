# from datetime import datetime
# import faker
# from random import randint, choice
# import psycopg2

# NUMBER_USERS = 3
# NUMBER_TASKS = 2

# def generate_fake_data(number_users, number_tasks) -> tuple:
#     fake_data = faker.Faker()

#     fake_users = []
#     fake_tasks = []

#     # Генерація даних для таблиці users
#     for _ in range(number_users):
#         fullname = fake_data.name()
#         email = fake_data.email()
#         fake_users.append((fullname, email))

#     # Генерація даних для таблиці tasks
#     for _ in range(number_tasks):
#         title = fake_data.text(20)
#         description = fake_data.text(100)
#         status_id = randint(1, 3)  # Виберіть випадковий статус_id з існуючих статусів
#         user_id = randint(1, number_users)  # Виберіть випадковий user_id

#         fake_tasks.append((title, description, status_id, user_id))

#     # Генерація даних для таблиці status
#     fake_status = [('new',), ('in progress',), ('completed',)]

#     return fake_users, fake_tasks, fake_status

# # Підключення до бази даних PostgreSQL
# connection = psycopg2.connect("dbname=test user=pavlenko password=1203qazxsw host=localhost")
# cursor = connection.cursor()

# # Генерація фейкових даних
# fake_users, fake_tasks, fake_status = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)

# # Вставка даних в таблиці users
# cursor.executemany('INSERT INTO users (fullname, email) VALUES (%s, %s)', fake_users)

# # Вставка даних в таблиці status
# cursor.executemany('INSERT INTO status (name) VALUES (%s)', fake_status)

# # Вставка даних в таблиці tasks
# cursor.executemany('INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)', fake_tasks)

# # Збереження змін та закриття з'єднання
# connection.commit()
# connection.close()

from faker import Faker
import psycopg2
from random import choice

NUMBER_USERS = 30
NUMBER_TASKS = 20

def generate_fake_data(number_users, number_tasks) -> tuple:
    fake_data = Faker()

    fake_users = []
    fake_tasks = []

    # Генерація фейкових даних для таблиці users
    for _ in range(number_users):
        fullname = fake_data.name()
        email = fake_data.email()

        # Перевірка, чи email вже існує в базі даних
        cursor.execute('SELECT id FROM users WHERE email = %s', (email,))
        existing_user = cursor.fetchone()

        # Якщо email вже існує, можна повторно згенерувати новий email
        while existing_user:
            email = fake_data.email()
            cursor.execute('SELECT id FROM users WHERE email = %s', (email,))
            existing_user = cursor.fetchone()

        fake_users.append((fullname, email))

    # Вставка даних в таблицю users
    cursor.executemany('INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id', fake_users)
    connection.commit()

    # Отримання існуючих user_id
    cursor.execute('SELECT id FROM users')
    user_ids = [row[0] for row in cursor.fetchall()]

    # Генерація фейкових даних для таблиці tasks
    for _ in range(number_tasks):
        title = fake_data.text(20)
        description = fake_data.text(100)
        status_name = choice(['new', 'in progress', 'completed'])
        user_id = choice(user_ids)  # Вибір існуючого user_id

        # Отримання id статусу за його ім'ям
        cursor.execute('SELECT id FROM status WHERE name = %s', (status_name,))
        status_id = cursor.fetchone()[0]

        fake_tasks.append((title, description, status_id, user_id))

    return fake_users, fake_tasks

# Підключення до бази даних PostgreSQL
connection = psycopg2.connect("dbname=test user=pavlenko password=1203qazxsw host=localhost")
cursor = connection.cursor()

# Генерація фейкових даних
fake_users, fake_tasks = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)

# Вставка даних в таблиці tasks
cursor.executemany('INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)', fake_tasks)

# Збереження змін та закриття з'єднання
connection.commit()
connection.close()