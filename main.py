import pyprcode

url = input("enter url to generate qr code: ")
qr_code = pyprcode.create(url)
qr_code.svg('qrcode.svg', scale = 7)
