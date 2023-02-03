from flask import render_template, Flask

app = Flask(__name__)

todo_list = ['Eat', 'Sleep', 'Code', 'Run']

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name, todo_list=todo_list)

if __name__ == '__main__':
    app.run()
    