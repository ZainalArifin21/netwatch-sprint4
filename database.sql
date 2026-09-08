CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (username, password)
VALUES ('zainal', '12345');

SELECT * FROM users;