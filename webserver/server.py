from flask import Flask,render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    # return 'Hello, Sany!'
    return render_template('index.html')

@app.route('/<username>/<int:post_id>')
def good_morning(username=None,post_id=None):
    # return 'Hello, Sany!'
    return render_template('index.html',name=username,post_id=post_id)

@app.route('/<string:page_name>')
def html_page(page_name:None):
    # return 'Hello, Sany!'
    return render_template(page_name)

# @app.route('/index.html')
# def index():
#     # return 'Hello, Sany!'
#     return render_template('index.html')

# @app.route('/about.html')
# def about():
#     # return 'Hello, Sany!'
#     return render_template('about.html')

# @app.route('/components.html')
# def components():
#     # return 'Hello, Sany!'
#     return render_template('components.html')

# @app.route('/contact.html')
# def contact():
#     # return 'Hello, Sany!'
#     return render_template('contact.html')

# @app.route('/works.html')
# def works():
#     # return 'Hello, Sany!'
#     return render_template('works.html')

# @app.route('/blog')
# def blog():
#     return 'Hello, In the BLOG!'