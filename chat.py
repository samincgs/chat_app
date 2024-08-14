from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my home. We appear to be lacking in <i>furniture</i>'

if __name__ == '__main__':
    app.run()