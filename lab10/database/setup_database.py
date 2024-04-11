import sqlite3

def setup_database():
    conn = sqlite3.connect('poems.db')
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS poems;
        CREATE TABLE poems (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            text TEXT
        );
    ''')
    poems = [
        ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood,
