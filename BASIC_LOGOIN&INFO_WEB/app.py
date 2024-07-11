from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Replace this with a proper database connection in a real application
users = {'user1': {'username': 'user1', 'password': 'password1'}} # here we can add and remove more users and pass. [we dont creat any database here]

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username]['password'] == password:
            return redirect(url_for('info', username=username))
        
        return render_template('login.html', message='Invalid credentials. Please try again.')
    
    return render_template('login.html')

@app.route('/info/<username>')
def info(username):
    if username in users:
        user = users[username]
        return render_template('info.html', user=user)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
