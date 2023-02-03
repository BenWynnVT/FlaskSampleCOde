from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/hello/world/')
def hello_world():
    return 'Hello World but with a different endpoint'

if __name__ == '__main__':
    app.run()
    