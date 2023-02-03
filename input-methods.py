from flask import Flask, request, send_file
from PIL import ImageOps, Image
import io

app = Flask(__name__)

def convert_PIL_image(img):
    img_io = io.BytesIO()
    img.save(img_io, 'JPEG')
    img_io.seek(0)
    return img_io

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World'


@app.route('/birthday/', methods=['POST'])
def birthday():
    input_json = request.get_json()
    birthday = input_json['birthday']
    first = input_json['first']
    last = input_json['last']
    return first + " " + last + "'s birthday is " + birthday

@app.route('/', methods=['POST'])
def invert():
    req = request.get_data()
    mime = request.content_type
    pil_image = ImageOps.invert(Image.open(io.BytesIO(req)))
    return send_file(convert_PIL_image(pil_image), mimetype=mime)


if __name__ == '__main__':
    app.run()
    