import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for
from scripts.automation import Automation
from scripts.database import Database
from config.config import SECRET_KEY, DEBUG

app = Flask(__name__)
app.secret_key = SECRET_KEY

automation = Automation()
db = Database()

@app.route('/')
def index():
    uploads = db.get_uploads()
    return render_template('index.html', uploads=uploads)

@app.route('/upload', methods=['POST'])
def upload():
    reel_url = request.form['reel_url']
    description = request.form.get('description', '')
    result = automation.process_reel(reel_url, description)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=DEBUG)