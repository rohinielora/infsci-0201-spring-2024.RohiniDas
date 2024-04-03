from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('poems.db')
    conn.row_factory = sqlite3.Row
    return conn

def setup_database():
    conn = get_db_connection()
    conn.execute('DROP TABLE IF EXISTS poems;')
    conn.execute('''
        CREATE TABLE poems (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            text TEXT
        );
    ''')
    poems = [
        ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
        ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
        ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o\'er vales and hills...'),
        ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer\'s day? Thou art more lovely and more temperate...'),
        ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...')
    ]
    conn.executemany('INSERT INTO poems (title, author, text) VALUES (?, ?, ?);', poems)
    conn.commit()
    conn.close()

@app.route('/')
def show_poems():
    conn = get_db_connection()
    poems = conn.execute('SELECT * FROM poems;').fetchall()
    conn.close()
    return render_template('show_poems.html', poems=poems)

if __name__ == '__main__':
    setup_database()
    app.run(debug=True)
