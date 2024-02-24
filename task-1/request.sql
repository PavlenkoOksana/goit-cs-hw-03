-- #1
SELECT * FROM tasks WHERE user_id = 135;

-- #2
SELECT *
FROM tasks
WHERE status_id = (SELECT id FROM status WHERE name = 'new');

-- #3
UPDATE tasks
SET status_id = (SELECT id FROM status WHERE name = 'new') 
WHERE id = 6; 

-- #4
SELECT * FROM users
WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

-- #5
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Назва завдання', 'Опис завдання', (SELECT id FROM status WHERE name = 'new'), 109);

-- #6
SELECT * FROM tasks
WHERE status_id != (SELECT id FROM status WHERE name = 'completed');

-- #7
DELETE FROM tasks WHERE id = 24;

-- #8
SELECT * FROM users WHERE email LIKE '%richard23@example.net%';

-- #9
UPDATE users
SET fullname = 'LLL' 
WHERE id = 107; 

-- #10
SELECT status.name, COUNT(tasks.id) AS task_count
FROM tasks
JOIN status ON tasks.status_id = status.id
GROUP BY status.name;

-- #11
SELECT tasks.*
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.email LIKE '%mharper@example.org';

-- #12
SELECT * FROM tasks WHERE description IS NULL OR description = '';

-- #13
SELECT users.fullname, tasks.title, tasks.description, status.name
FROM users
INNER JOIN tasks ON users.id = tasks.user_id
INNER JOIN status ON tasks.status_id = status.id
WHERE status.name = 'in progress';

-- #14
SELECT users.id, users.fullname, COUNT(tasks.id) AS task_count
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.id, users.fullname;
