import werkzeug
import flask
from flask import Flask, abort, render_template

app = Flask(__name__)

@app.route("/fourzerozero/")
def user_profile():
    abort(400)
    
@app.route("/fourzerofour/")
def fourzerofour():
    abort(404)

@app.route('/twozerotwo/')
def twozerotwo():
    return flask.Response(response="Here is an example of a 202 status code", status=202)
    
@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400

@app.errorhandler(werkzeug.exceptions.NotFound)
def handle_exception(e):
    return render_template("not_found.html"), 404

if __name__ == '__main__':
    app.run()