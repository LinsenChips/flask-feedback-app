from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Verbindung zur MongoDB-Datenbank herstellen
client = MongoClient("mongodb://mongo:27017/")  # "mongo" ist der Name des MongoDB-Containers
db = client.feedbackapp
entries_collection = db.entries

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entry = request.form.get('entry')
        if entry:
            # Füge den Eintrag zur MongoDB-Datenbank hinzu
            entries_collection.insert_one({'entry': entry})
            return redirect(url_for('index'))
    entries = [entry['entry'] for entry in entries_collection.find()]
    return render_template('index.html', entries=entries)

@app.route('/delete_entry', methods=['POST'])
def delete_entry():
    entry_to_delete = request.form.get('entry')
    entries_collection.delete_one({'entry': entry_to_delete})
    return jsonify({'entries': [entry['entry'] for entry in entries_collection.find()]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
