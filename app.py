from flask import Flask, redirect, render_template, request, url_for, flash
from db import db

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        value = db.authenticate(
            request.form['username'],
            request.form['password'])
        if (value == 1):
            print "About to login"
            return redirect(url_for('index'))
        else:
            error = 'Invalid username or password \
            Please try again!'
            return render_template('login.html', error=error)
    return render_template('login.html')


@app.route('/reg?is%2')
def registration():
    return render_template('registration.html')


@app.route("/registform", methods=['POST'])
def register():
    data = db.user_alreadyexits(request.form['field3'],
                                request.form['field1'],
                                request.form['field2'],
                                request.form['field4'])
    if (data == 1):
        flash('Duplicate user')
    print data
    flash('You were successfull')
    return render_template('/login.html')


@app.route('/login')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8081, debug=True)
