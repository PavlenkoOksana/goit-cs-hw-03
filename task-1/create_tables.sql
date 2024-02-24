-- Створення таблиці users
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- Створення таблиці status
CREATE TABLE IF NOT EXISTS status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE
);

-- Заповнення таблиці status 
INSERT INTO status (name) VALUES ('new'), ('in progress'), ('completed');

-- Створення таблиці tasks з використанням зовнішніх ключів
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER REFERENCES status(id),
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);