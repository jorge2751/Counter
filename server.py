from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'super secret key'  # set the secret key for the session

@app.route('/')
def index():
    if 'count' in session:
        count = session['count']
    else:
        count = 0
    if 'visits' in session:
        visits = session['visits']
        session['visits'] += 1
    else:
        visits = 1
        session['visits'] = 2
    return render_template('index.html', count=count, visits=visits)

@app.route('/add', methods=['POST'])
def add():
    increment = int(request.form['increment'])
    if 'count' in session:
        session['count'] += increment
    else:
        session['count'] = increment
    return redirect(url_for('index'))

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

