import sqlite3

def create():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreign_keys=on')

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY,
            name VARCHAR
        )
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS question (
            id INTEGER PRIMARY KEY,
            question VARCHAR,
            answer VARCHAR,
            wrong1 VARCHAR,
            wrong2 VARCHAR,
            wrong3 VARCHAR
        )
        '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS quiz_content (
            id INTEGER PRIMARY KEY,
            quiz_id INTEGER,
            question_id INTEGER,
            FOREIGN KEY (quiz_id) REFERENCES quiz (id),
            FOREIGN KEY (question_id) REFERENCES question (id)
        )
        '''
    )

    conn.close()