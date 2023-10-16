import logging

import cv2
import qrcode

logger = logging.getLogger(__name__)

class QRReader(object):

    def __init__(self, image):
        self.image = image
        self.qr_detector = cv2.QRCodeDetector()

    def read(self):
        detection = self.qr_detector.detectAndDecodeMulti(self.image)

        if not detection[0]:
            return "Qr code is invalid"

        return detection[1][0]

