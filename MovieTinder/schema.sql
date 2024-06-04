\i schema_drop.sql

CREATE TABLE IF NOT EXISTS Users(
	id INT GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(60),
	password VARCHAR(120),
	PRIMARY KEY (id) 
);

CREATE TABLE IF NOT EXISTS HasFriends(
	id1 INT,
    id2 INT,
    FOREIGN KEY (id1) REFERENCES Users(id),
    FOREIGN KEY (id2) REFERENCES Users(id)
);


CREATE TABLE IF NOT EXISTS Movies(
    id INT GENERATED ALWAYS AS IDENTITY,
    imdb_id VARCHAR(120),
    title VARCHAR(120),
    year INT,
    summary TEXT,
    PRIMARY KEY (id)
);

COPY Movies(imdb_id,title,year,summary)
FROM 'C:\Users\Laust\Postgres Import\movies_shaved.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE IF NOT EXISTS Likes(
	user_id INT,
    movie_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
);

