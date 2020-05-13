drop table if exists posts;
    CREATE TABLE posts (
        id int PRIMARY KEY,
        name text NOT NULL,
        content text NOT NULL
    );
    