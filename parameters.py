from flask import Flask

app = Flask(__name__)

@app.route('/<first>/<last>/')
def hello_world(first, last):
    return 'Hello ' + first + ' ' + last + '!'

if __name__ == '__main__':
    app.run()
    