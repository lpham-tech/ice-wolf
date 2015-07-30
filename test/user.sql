--
-- File generated with SQLiteStudio v3.0.6 on Th 5 thg 7 30 20:33:56 2015
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: user
DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(80), 
	email VARCHAR(120), 
	password VARCHAR(80), 
	first_name VARCHAR(40), 
	last_name VARCHAR(40), 
	avatar VARCHAR(512), 
	brief VARCHAR(1024), 
	role VARCHAR(20), 
	activated BOOLEAN, 
	activation_id VARCHAR(64), 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email), 
	CHECK (activated IN (0, 1))
);
INSERT INTO user (id, username, email, password, first_name, last_name, avatar, brief, role, activated, activation_id) VALUES (1, NULL, 'changed@gmail.com', '70fb874a43097a25234382390c0baeb3', 'Dzung', 'Nguyen Tien', '', 'Hello world Again', 'editor', 1, 'cd902b80e7cb42145148b41acd603042');
INSERT INTO user (id, username, email, password, first_name, last_name, avatar, brief, role, activated, activation_id) VALUES (2, NULL, 'editor2@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'Editor2', 'Nguyen', '', 'Hello world', 'editor', 1, '600ccf50ddb7c4c443ab6acb22386bf1');
INSERT INTO user (id, username, email, password, first_name, last_name, avatar, brief, role, activated, activation_id) VALUES (3, NULL, 'editor3@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'Editor3', 'Nguyen', '', 'Hello world', 'editor', 1, 'd00d4795a1ea5c2770dce6405a11b266');
INSERT INTO user (id, username, email, password, first_name, last_name, avatar, brief, role, activated, activation_id) VALUES (4, NULL, 'editor4@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', 'Editor4', 'Nguyen', '', 'Hello world', 'editor', 1, '58e0a842430cf250d284b86d1ae966e0');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
