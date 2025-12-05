import qrcode
import os

CARNETS_DIR = "static/carnets"
QRS_DIR = "static/qrs"

# IMPORTANTE → cambia localhost por tu IP local para escanear desde celular
BASE_URL = "http://localhost:5000/carnet/"  

os.makedirs(QRS_DIR, exist_ok=True)

imagenes = os.listdir(CARNETS_DIR)

for img in imagenes:
    url = BASE_URL + img
    qr = qrcode.make(url)

    qr_filename = img.split('.')[0] + "_QR.png"
    output_path = os.path.join(QRS_DIR, qr_filename)
    qr.save(output_path)

    print(f"QR generado: {output_path}")
