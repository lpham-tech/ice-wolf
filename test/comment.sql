--
-- File generated with SQLiteStudio v3.0.6 on Th 5 thg 7 30 20:58:55 2015
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: comment
DROP TABLE IF EXISTS comment;
CREATE TABLE comment (
	id INTEGER NOT NULL, 
	content TEXT, 
	post_id INTEGER, 
	user_id INTEGER, 
	time DATETIME, 
	approved BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(post_id) REFERENCES post (id), 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	CHECK (approved IN (0, 1))
);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (1, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 1, 2, '2015-07-30 20:56:10.171727', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (2, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 1, 3, '2015-07-30 20:56:10.276896', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (3, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 1, 4, '2015-07-30 20:56:10.368983', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (4, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 3, 4, '2015-07-30 20:56:10.461118', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (5, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 3, 2, '2015-07-30 20:56:10.578403', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (6, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 4, 1, '2015-07-30 20:56:10.688279', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (7, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 7, 1, '2015-07-30 20:56:10.796217', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (8, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 4, 2, '2015-07-30 20:56:10.922017', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (9, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 3, 3, '2015-07-30 20:56:11.014467', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (10, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 2, 4, '2015-07-30 20:56:11.123253', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (11, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 2, 1, '2015-07-30 20:56:11.223211', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (12, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 2, 3, '2015-07-30 20:56:11.348943', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (13, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 2, 4, '2015-07-30 20:56:11.449357', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (14, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 5, 3, '2015-07-30 20:56:11.567096', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (15, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 5, 2, '2015-07-30 20:56:11.683962', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (16, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 5, 3, '2015-07-30 20:56:11.792739', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (17, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 5, 4, '2015-07-30 20:56:11.893417', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (18, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 6, 4, '2015-07-30 20:56:11.978693', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (19, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 6, 1, '2015-07-30 20:56:12.070788', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (20, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 9, 1, '2015-07-30 20:56:12.163611', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (21, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 9, 1, '2015-07-30 20:56:12.289150', 1);
INSERT INTO comment (id, content, post_id, user_id, time, approved) VALUES (22, '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut ipsum ad, mollitia repellendus harum dignissimos rem beatae, dolore minus. Sapiente saepe mollitia magnam molestiae natus officiis corrupti voluptatibus, qui repudiandae.</p>', 9, 3, '2015-07-30 20:56:12.380949', 1);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
