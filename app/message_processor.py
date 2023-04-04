import sqlite3
from config.config import DATABASE_URI

def process_messages(messages):
    # Implement your message processing logic here
    questions_answers = []
    return questions_answers

def store_questions_answers(questions_answers):
    conn = sqlite3.connect(DATABASE_URI)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS qa (
                        id INTEGER PRIMARY KEY,
                        question TEXT,
                        answer TEXT,
                        timestamp TEXT,
                        user TEXT)''')
    conn.commit()

    cursor.executemany('''INSERT INTO qa (question, answer, timestamp, user)
                           VALUES (?, ?, ?, ?)''', questions_answers)
    conn.commit()

    cursor.close()
    conn.close()

