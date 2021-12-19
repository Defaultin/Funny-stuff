import numpy as np
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
        matrix = np.array(qr.get_matrix(), dtype=int)

        img = qr.make_image()
        img.save(file_name)

        return matrix[self.border:-self.border, self.border:-self.border]


    def decode(self, qr):
        # init
        n, m = qr.shape
        matrix = qr.copy()
        box = np.where(matrix[0] == False)[0][0]
        mask = qrcode.util.mask_func(self.mask)

        def skip(i, j):
            # error info area
            if 0 <= j <= box + 1:
                 return True
            # top right scan box
            elif 0 <= i <= box + 1 and m - box - 1 <= j <= m:
                return True
            # bottom right scan box
            elif n - 9 <= i <= n - 5 and m - 9 <= j <= m - 5:
                return True
            # top scan line
            elif i == box - 1:
                return True
            # remaining bits
            else:
                 return False

        # apply mask and retrive bits
        bits = np.array([], dtype=int)
        for j in reversed(range(0, m, 2)):
            for i in reversed(range(n)) if (j - 1) // 2 % 2 else range(n):
                if not skip(i, j):
                    bit = not matrix[i, j] if mask(i, j) else matrix[i, j]
                    bits = np.append(bits, bit)
                if not skip(i, j - 1):
                    bit = not matrix[i, j - 1] if mask(i, j - 1) else matrix[i, j - 1]
                    bits = np.append(bits, bit)

        # decode bits
        data = np.packbits(bits[12:])
        for i in range(2, data.size, 2):
            try:
                text = bytearray(data[:i]).decode()
            except UnicodeDecodeError:
                continue

        return text


def main():
    # generate QR code for message
    filename = "qr.png"
    message = "Hi there! What's up?"
    qr = QRCode()
    code = qr.generate(message, filename)
    print("QR Matrix type:", type(code))

    # mess up the QR code
    for i in range(1, 21):
        for j in range(10):
            code[i, j] = 0

    # decode bad QR code
    text = qr.decode(code)
    print(text, message in text)


if __name__ == '__main__':
    main()
