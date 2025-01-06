INSERT INTO users (id, points, duplicates, achievements) VALUES ('test1', 0, 0, 0);
INSERT INTO cards (name, type, owner_id) VALUES ('devious sangmin',  'NONE', 'test1');

DELETE FROM users where id LIKE 'test1';