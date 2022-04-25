import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# set-up tables
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id      integer not null primary key autoincrement unique,
    name    text unique
);

Create table Course (
    id      integer not null primary key autoincrement unique,
    title   text unique
);

Create table Member (
    user_id     integer,
    course_id   integer,
    role        integer,
    primary key (user_id, course_id)
)
''')