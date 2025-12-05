import os
import qrcode

BASE_URL = "https://carnets-flask.onrender.com/carnet/"
CARNETS_DIR = "static/carnets"
OUTPUT_DIR = "static/qrs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(CARNETS_DIR):
    if filename.lower().endswith(".png") or filename.lower().endswith(".jpg"):
        full_url = BASE_URL + filename
        img = qrcode.make(full_url)
        img.save(os.path.join(OUTPUT_DIR, filename.replace(".png", "_qr.png")))
        print("QR generado:", full_url)
