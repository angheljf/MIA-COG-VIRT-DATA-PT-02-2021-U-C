from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return('Hello, World!!!')

@app.route('/about')
def about():
    page = 'about'
    return('This is {} whatever, yay').format(page)

@app.route('/contact')
def contact():
    email = 'mischaisgreat@trilogy.com'
    print('If you want to complain, do not email {}').format(email)

if __name__ == '__main__':
    app.run(debug=True)
