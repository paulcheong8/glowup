CREATE DATABASE glowupdb;

CREATE EXTENSION pgcrypto;

CREATE TABLE users (
    user_id SERIAL,
    nickname varchar(255),
    email varchar(255),
    created_date timestamp default current_timestamp,
    password varchar(255),
    organisation varchar(255),
    PRIMARY KEY (user_id)
);


CREATE TABLE posts (
    post_id SERIAL,
    user_id int,
    created_date timestamp default current_timestamp,
    category varchar(255),
    title varchar(255),
    advice varchar(255),
    PRIMARY KEY (post_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE comments (
    comment_id SERIAL,
    user_id int,
    post_id int,
    created_date timestamp default current_timestamp,
    comment varchar(255),
    comment_reply_id int UNIQUE,
    PRIMARY KEY (comment_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id),
    FOREIGN KEY (comment_reply_id) REFERENCES comments(comment_reply_id)
);

CREATE TABLE views (
    view_id SERIAL,
    user_id int,
    post_id int,
    created_date timestamp default current_timestamp,
    PRIMARY KEY (view_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
);

CREATE TABLE likes (
    like_id SERIAL,
    user_id int,
    comment_id int,
    created_date timestamp default current_timestamp,
    PRIMARY KEY (like_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (comment_id) REFERENCES comments(comment_id)
);