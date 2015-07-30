--
-- File generated with SQLiteStudio v3.0.6 on Th 5 thg 7 30 20:48:32 2015
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: post
DROP TABLE IF EXISTS post;
CREATE TABLE post (
	id INTEGER NOT NULL, 
	title VARCHAR(512), 
	content TEXT, 
	feature_image VARCHAR(512), 
	user_id INTEGER, 
	time DATETIME, 
	tags VARCHAR(128), 
	categories VARCHAR(128), 
	draft BOOLEAN, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	CHECK (draft IN (0, 1))
);
INSERT INTO post (id, title, content, feature_image, user_id, time, tags, categories, draft) VALUES (1, 'Post 1 title', '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet doloribus qui, adipisci inventore sequi fugiat dolores ullam, provident a, accusantium, necessitatibus ab nisi aliquam. Ipsam voluptas dolores magni necessitatibus provident.</p>
    <p>Sunt quo placeat fugiat nesciunt vel assumenda dolorem incidunt provident eligendi ipsa, quam autem optio id nostrum beatae corporis a. Tempore saepe quod nemo hic magni in veritatis illum natus.</p>
    <p>Et beatae ipsam repellat officiis similique cupiditate distinctio expedita rem at, aut aspernatur, voluptate quibusdam! Voluptatum aut quos porro eos nulla officiis adipisci magnam perferendis, dicta minima quis eligendi enim.</p>
    <p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>', NULL, 1, '2015-07-30 20:47:14.542205', NULL, NULL, 0);
INSERT INTO post (id, title, content, feature_image, user_id, time, tags, categories, draft) VALUES (2, 'Post 2 title', '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet doloribus qui, adipisci inventore sequi fugiat dolores ullam, provident a, accusantium, necessitatibus ab nisi aliquam. Ipsam voluptas dolores magni necessitatibus provident.</p>
    <p>Sunt quo placeat fugiat nesciunt vel assumenda dolorem incidunt provident eligendi ipsa, quam autem optio id nostrum beatae corporis a. Tempore saepe quod nemo hic magni in veritatis illum natus.</p>
    <p>Et beatae ipsam repellat officiis similique cupiditate distinctio expedita rem at, aut aspernatur, voluptate quibusdam! Voluptatum aut quos porro eos nulla officiis adipisci magnam perferendis, dicta minima quis eligendi enim.</p>
    <p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>', NULL, 2, '2015-07-30 20:47:14.675056', NULL, NULL, 0);
INSERT INTO post (id, title, content, feature_image, user_id, time, tags, categories, draft) VALUES (3, 'Post 3 title', '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet doloribus qui, adipisci inventore sequi fugiat dolores ullam, provident a, accusantium, necessitatibus ab nisi aliquam. Ipsam voluptas dolores magni necessitatibus provident.</p>
    <p>Sunt quo placeat fugiat nesciunt vel assumenda dolorem incidunt provident eligendi ipsa, quam autem optio id nostrum beatae corporis a. Tempore saepe quod nemo hic magni in veritatis illum natus.</p>
    <p>Et beatae ipsam repellat officiis similique cupiditate distinctio expedita rem at, aut aspernatur, voluptate quibusdam! Voluptatum aut quos porro eos nulla officiis adipisci magnam perferendis, dicta minima quis eligendi enim.</p>
    <p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>', NULL, 3, '2015-07-30 20:47:14.776556', NULL, NULL, 0);
INSERT INTO post (id, title, content, feature_image, user_id, time, tags, categories, draft) VALUES (4, 'Post 4 title', '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet doloribus qui, adipisci inventore sequi fugiat dolores ullam, provident a, accusantium, necessitatibus ab nisi aliquam. Ipsam voluptas dolores magni necessitatibus provident.</p>
    <p>Sunt quo placeat fugiat nesciunt vel assumenda dolorem incidunt provident eligendi ipsa, quam autem optio id nostrum beatae corporis a. Tempore saepe quod nemo hic magni in veritatis illum natus.</p>
    <p>Et beatae ipsam repellat officiis similique cupiditate distinctio expedita rem at, aut aspernatur, voluptate quibusdam! Voluptatum aut quos porro eos nulla officiis adipisci magnam perferendis, dicta minima quis eligendi enim.</p>
    <p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>', NULL, 4, '2015-07-30 20:47:14.884545', NULL, NULL, 0);
INSERT INTO post (id, title, content, feature_image, user_id, time, tags, categories, draft) VALUES (5, 'Post Hello title', '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet doloribus qui, adipisci inventore sequi fugiat dolores ullam, provident a, accusantium, necessitatibus ab nisi aliquam. Ipsam voluptas dolores magni necessitatibus provident.</p>
    <p>Sunt quo placeat fugiat nesciunt vel assumenda dolorem incidunt provident eligendi ipsa, quam autem optio id nostrum beatae corporis a. Tempore saepe quod nemo hic magni in veritatis illum natus.</p>
    <p>Et beatae ipsam repellat officiis similique cupiditate distinctio expedita rem at, aut aspernatur, voluptate quibusdam! Voluptatum aut quos porro eos nulla officiis adipisci magnam perferendis, dicta minima quis eligendi enim.</p>
    <p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>', NULL, 1, '2015-07-30 20:47:14.976785', NULL, NULL, 0);
INSERT INTO post (id, title, content, feature_image, user_id, time, tags, categories, draft) VALUES (6, 'Good morning', '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet doloribus qui, adipisci inventore sequi fugiat dolores ullam, provident a, accusantium, necessitatibus ab nisi aliquam. Ipsam voluptas dolores magni necessitatibus provident.</p>
    <p>Sunt quo placeat fugiat nesciunt vel assumenda dolorem incidunt provident eligendi ipsa, quam autem optio id nostrum beatae corporis a. Tempore saepe quod nemo hic magni in veritatis illum natus.</p>
    <p>Et beatae ipsam repellat officiis similique cupiditate distinctio expedita rem at, aut aspernatur, voluptate quibusdam! Voluptatum aut quos porro eos nulla officiis adipisci magnam perferendis, dicta minima quis eligendi enim.</p>
    <p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>', NULL, 2, '2015-07-30 20:47:15.085568', NULL, NULL, 0);
INSERT INTO post (id, title, content, feature_image, user_id, time, tags, categories, draft) VALUES (7, 'First day at Moscow', '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet doloribus qui, adipisci inventore sequi fugiat dolores ullam, provident a, accusantium, necessitatibus ab nisi aliquam. Ipsam voluptas dolores magni necessitatibus provident.</p>
    <p>Sunt quo placeat fugiat nesciunt vel assumenda dolorem incidunt provident eligendi ipsa, quam autem optio id nostrum beatae corporis a. Tempore saepe quod nemo hic magni in veritatis illum natus.</p>
    <p>Et beatae ipsam repellat officiis similique cupiditate distinctio expedita rem at, aut aspernatur, voluptate quibusdam! Voluptatum aut quos porro eos nulla officiis adipisci magnam perferendis, dicta minima quis eligendi enim.</p>
    <p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>', NULL, 2, '2015-07-30 20:47:15.171251', NULL, NULL, 0);
INSERT INTO post (id, title, content, feature_image, user_id, time, tags, categories, draft) VALUES (8, 'Surprising', '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet doloribus qui, adipisci inventore sequi fugiat dolores ullam, provident a, accusantium, necessitatibus ab nisi aliquam. Ipsam voluptas dolores magni necessitatibus provident.</p>
    <p>Sunt quo placeat fugiat nesciunt vel assumenda dolorem incidunt provident eligendi ipsa, quam autem optio id nostrum beatae corporis a. Tempore saepe quod nemo hic magni in veritatis illum natus.</p>
    <p>Et beatae ipsam repellat officiis similique cupiditate distinctio expedita rem at, aut aspernatur, voluptate quibusdam! Voluptatum aut quos porro eos nulla officiis adipisci magnam perferendis, dicta minima quis eligendi enim.</p>
    <p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>', NULL, 3, '2015-07-30 20:47:15.272530', NULL, NULL, 0);
INSERT INTO post (id, title, content, feature_image, user_id, time, tags, categories, draft) VALUES (9, 'So awesome lake', '<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet doloribus qui, adipisci inventore sequi fugiat dolores ullam, provident a, accusantium, necessitatibus ab nisi aliquam. Ipsam voluptas dolores magni necessitatibus provident.</p>
    <p>Sunt quo placeat fugiat nesciunt vel assumenda dolorem incidunt provident eligendi ipsa, quam autem optio id nostrum beatae corporis a. Tempore saepe quod nemo hic magni in veritatis illum natus.</p>
    <p>Et beatae ipsam repellat officiis similique cupiditate distinctio expedita rem at, aut aspernatur, voluptate quibusdam! Voluptatum aut quos porro eos nulla officiis adipisci magnam perferendis, dicta minima quis eligendi enim.</p>
    <p>Sed itaque dignissimos eligendi reprehenderit, nesciunt ducimus voluptates dolores suscipit fugit ipsam aperiam praesentium laborum odit qui libero ipsum tempora, eos quis hic, sapiente perspiciatis amet labore voluptatibus alias. Vitae.</p>', NULL, 3, '2015-07-30 20:47:15.372949', NULL, NULL, 0);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
