from flask import Flask,render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    # return 'Hello, Sany!'
    return render_template('index.html')

@app.route('/<username>/<int:post_id>')
def good_morning(username=None,post_id=None):
    # return 'Hello, Sany!'
    return render_template('index.html',name=username,post_id=post_id)

@app.route('/about')
def about():
    # return 'Hello, Sany!'
    return render_template('about.html')

@app.route('/blog')
def blog():
    return 'Hello, In the BLOG!'