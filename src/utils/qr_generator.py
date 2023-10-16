import json
import logging

import qrcode

logger = logging.getLogger(__name__)


class QrGenerator:
    def __init__(self, box_size: int = 10, border: int = 4) -> None:
        try:
            self.qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=border,
            )
        except Exception as e:
            logger.exception(e)

    def encrypt_data(self, data: dict):
        try:
            self.qr.add_data(data)
            self.qr.make(fit=True)
            return self
        except Exception as e:
            logger.exception(e)

    def generate_image(self, fill_color: str = "black", back_color: str = "white"):
        try:
            img = self.qr.make_image(fill_color=fill_color, back_color=back_color)
            return img.get_image()
        except Exception as e:
            logger.exception(e)
