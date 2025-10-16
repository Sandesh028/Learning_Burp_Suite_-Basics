# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # For demonstration, simply echo back the submitted data.
        message = f"Received login for {username} with password {password}"
    return render_template('login.html', message=message)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    return render_template('search.html', query=query)

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    comment_text = None
    if request.method == 'POST':
        comment_text = request.form.get('comment')
    return render_template('comment.html', comment=comment_text)

if __name__ == '__main__':
    # Run on port 8080 to avoid conflicts with Burp Suite's default settings if needed.
    app.run(debug=True, port=8080)
