import sqlite3
import streamlit.components.v1 as components
from jinja2 import Template

def fetch_poems():
    conn = sqlite3.connect('poems.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title, author, text FROM poems')
    poems = cursor.fetchall()
    conn.close()
    return poems

def main():
    poems = fetch_poems()
    items = [f"{title} by {author}: {text}" for title, author, text in poems]

    with open("templates/template.html", "r") as template_file:
        template_content = template_file.read()
        jinja_template = Template(template_content)

    app_title = "List of Poems"
    rendered_html = jinja_template.render(title=app_title, items=items)
    components.html(rendered_html, height=800, scrolling=True)

if __name__ == '__main__':
    main()
