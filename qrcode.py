import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_corrication=qrcode.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://github.com/bhattaniya")
qr.make(fit=True)
img=qr.make_image(fill_color="red",Back_color="blue")
img.save("github profile.png")