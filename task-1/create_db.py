# import psycopg2
# from psycopg2 import sql

# def create_tables():
#     # Встановлення підключення до бази даних PostgreSQL
#     conn = psycopg2.connect("dbname=test user=pavlenko password=1203qazxsw host=localhost")
#     cur = conn.cursor()

#     sql = ["CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, fullname VARCHAR(100), email VARCHAR(100) UNIQUE);", "Інші запити"]
    
#     for command in sql:
#         cur.execute(command)

# if __name__ == "__main__":
#     create_tables()

# import psycopg2
# from psycopg2 import sql

# def create_tables():
#     conn = psycopg2.connect("dbname=pavl_database user=pavlenko password=1203qazxsw host=localhost")
#     cur = conn.cursor()

#     with open('D:/Projects/My_Repository/goit-cs-hw-03/goit-cs-hw-03/task-1/create_tables.sql', 'r') as f:
#         sql_statements = f.read()

   
#     for statement in sql_statements.split(';'):
#         if statement.strip():  
#             cur.execute(sql.SQL(statement))

 
#     conn.commit()

  
#     cur.close()
#     conn.close()
#     print("\nOK\n")

# if __name__ == "__main__":
#     create_tables()



import psycopg2
from psycopg2 import sql

def create_tables():
    conn = psycopg2.connect("dbname=pavl_database user=pavlenko password=1203qazxsw host=localhost")
    cur = conn.cursor()

    with open('D:/Projects/My_Repository/goit-cs-hw-03/goit-cs-hw-03/task-1/create_tables.sql', 'r') as f:
        sql_statements = f.read()

   
    for statement in sql_statements.split(';'):
        if statement.strip():  
            cur.execute(sql.SQL(statement))

 
    conn.commit()

  
    cur.close()
    conn.close()
    print("\nOK\n")

if __name__ == "__main__":
    create_tables()