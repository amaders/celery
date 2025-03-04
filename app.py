import os
from flask import Flask, flash, render_template, redirect, request
from tasks import add

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', "super-secret")


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/add', methods=['POST'])
def add_inputs():
    x = int(request.form['x'] or 0)
    y = int(request.form['y'] or 0)
    add.apply_async(args=[x, y, 2])
    flash("Your addition job has been submitted.")
    print("APP.PY TEST MESSAGE")
    return redirect('/')
