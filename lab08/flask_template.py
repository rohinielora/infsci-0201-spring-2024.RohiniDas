from flask import Flask, render_template

app = Flask(__name__)

# Updated data structure for new poems
poems = [
    {"id": 0, "title": "Invictus", "author": "William Ernest Henley", "text": "Out of the night that covers me, Black as the pit from pole to pole..."},
    {"id": 1, "title": "If—", "author": "Rudyard Kipling", "text": "If you can keep your head when all about you Are losing theirs and blaming it on you..."},
    {"id": 2, "title": "The Love Song of J. Alfred Prufrock", "author": "T.S. Eliot", "text": "Let us go then, you and I, When the evening is spread out against the sky..."},
    {"id": 3, "title": "Mending Wall", "author": "Robert Frost", "text": "Something there is that doesn't love a wall, That sends the frozen-ground-swell under it..."},
    {"id": 4, "title": "Do Not Go Gentle into That Good Night", "author": "Dylan Thomas", "text": "Do not go gentle into that good night, Old age should burn and rave at close of day..."}
]

@app.route('/')
def index():
    return render_template('index.html', poems=poems)

@app.route('/poem/<int:poem_id>')
def poem(poem_id):
    poem = next((poem for poem in poems if poem['id'] == poem_id), None)
    if poem is not None:
        return render_template('poem.html', poem=poem)
    return "Poem not found", 404

if __name__ == '__main__':
    app.run(debug=True)
