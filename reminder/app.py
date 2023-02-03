from flask import Flask, render_template, request, redirect
from PIL import ImageOps, Image
import io

app = Flask(__name__)

todo_list = []

@app.route('/remove/', methods=['DELETE'])
def remove():
    item = request.form['item']
    todo_list.remove(item)
    return redirect('/')

@app.route('/add/', methods=['POST'])
def add():
    todo_list.append(request.form['item'])
    return redirect('/')

@app.route('/', methods=['GET'])
def list():
    return render_template('home.html', todo_list=todo_list)

if __name__ == '__main__':
    app.run()