from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = 'random string'


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'Deepak' or \
           request.form['password'] != 'Deepak':
            error = 'Invalid username or password \
            Please try again!'
        else:
            return redirect(url_for('index'))

    return render_template('login.html', error=error)


@app.route('/reg?is%2')
def registration():
    return render_template('registration.html')


@app.route('/login')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80, debug=True)
