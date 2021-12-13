import cv2
import qrcode


class QRCode:
    def __init__(self, version=None,
                 error=qrcode.constants.ERROR_CORRECT_L,
                 size=10, border=4, mask=0):
        self.version = version
        self.error = error
        self.size = size
        self.border = border
        self.mask = mask


    def generate(self, data, file_name="qr.png"):
        qr = qrcode.QRCode(
            version=self.version,
            error_correction=self.error,
            box_size=self.size,
            border=self.border,
            mask_pattern=self.mask
        )

        qr.add_data(data)
        qr.make(fit=True)
        image = qr.make_image()
        image.save(file_name)


    def decode(self, file_name="qr.png"):
        image = cv2.imread(file_name)
        detector = cv2.QRCodeDetector()
        data, vertices, matrix = detector.detectAndDecode(image)
        return data
