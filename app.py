import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_home():  # put application's code here
    blog_data = requests.get('https://api.npoint.io/65af5396f563b009b3dd').json()
    return render_template('index.html', data=blog_data)


@app.route('/about')
def get_about():
    return render_template('about.html')


@app.route('/contact')
def get_contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
