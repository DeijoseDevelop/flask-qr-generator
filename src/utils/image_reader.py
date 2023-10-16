import base64
from io import BytesIO

from PIL import Image
import numpy as np
import cv2


class ImageReader(object):

    def __init__(self, bytes_or_image: str or bytes):
        self.bytes_or_image = bytes_or_image
        self.image = None

    def convert_image_to_base64(self):
        buffered = BytesIO()
        self.image.save(buffered, format="JPEG")
        self.image = base64.b64encode(buffered.getvalue())
        return self

    def convert_base64_to_image(self):
        self.image = Image.open(BytesIO(base64.b64decode(self.bytes_or_image)))
        return self

    def create_image_from_path(self):
        self.image = Image.open(self.bytes_or_image)
        return self

    def convert_pillow_to_cv2(self):
        self.image = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
        return self

