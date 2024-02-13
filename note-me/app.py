from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Chargement des notes depuis le fichier JSON
def load_notes():
    try:
        with open('data.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

# Sauvegarde des notes dans le fichier JSON
def save_notes(notes):
    with open('data.json', 'w') as file:
        json.dump(notes, file, indent=4)

@app.route('/')
def index():
    notes = load_notes()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    notes = load_notes()
    titre = request.form['titre']
    contenu = request.form['contenu']
    notes.append({'titre': titre, 'contenu': contenu})
    save_notes(notes)
    return redirect(url_for('index'))

@app.route('/delete_note/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    notes = load_notes()
    if 0 <= note_id < len(notes):
        del notes[note_id]
        save_notes(notes)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
