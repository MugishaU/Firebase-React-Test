DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    uid varchar(28),
    username varchar(255)
);

INSERT INTO users (uid, username)
VALUES
('yKyLmkyIKmTTr3W7jJay6ygRULv2','user1'),
('sOBdjNvWYcdXV1O0niEIawWEDNu2','user2'),
('D4Pe4XwHp0ZmSso7ek4jcu5fnYH2','user3')
;