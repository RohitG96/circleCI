from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'HEllo world'


if __name__ == '__main__':
    app.run()
