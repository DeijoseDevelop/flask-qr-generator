import json
from io import StringIO, BytesIO
import os

from flask import (
    Flask,
    request,
    current_app,
    views,
    send_file,
)

from src.utils import (
    CustomResponse,
    ImageReader,
    QRReader,
    QrGenerator,
)


app = Flask(__name__)

class GenerateQRView(views.MethodView):
    def post(self):
        data = request.data or {}
        if os.path.exists('test.jpeg'):
            os.remove('test.jpeg')

        if not data:
            return CustomResponse({"message": 'Data not found'}, status=404)

        try:
            qr_generator = QrGenerator().encrypt_data(json.dumps(json.loads(data)))
        except json.decoder.JSONDecodeError:
            qr_generator = QrGenerator().encrypt_data(data)

        image = qr_generator.generate_image()

        image.save('test.jpeg', format="JPEG")

        return send_file('test.jpeg', mimetype='image/jpeg')

class ReadQRView(views.MethodView):
    def post(self):
        image = request.files.get('image', False)

        if not image:
            return CustomResponse({"message": 'Image not found'}, status=404)

        image_reader = ImageReader(image)\
            .create_image_from_path()\
            .convert_pillow_to_cv2()
        qr_reader = QRReader(image_reader.image)

        try:
            response = json.loads(qr_reader.read())
        except json.decoder.JSONDecodeError:
            response = qr_reader.read()

        return CustomResponse({"result": response})


app.add_url_rule("/generate/", view_func=GenerateQRView.as_view("GenerateQRView"))
app.add_url_rule("/read/", view_func=ReadQRView.as_view("ReadQRView"))
