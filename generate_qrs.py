import os
import qrcode

CARNETS_DIR = "static/carnets"
QR_DIR = "static/qrs"

def generar_todos_los_qr():
    # Crear la carpeta QR si no existe
    if not os.path.exists(QR_DIR):
        os.makedirs(QR_DIR)

    # Recorrer todos los carnets
    for filename in os.listdir(CARNETS_DIR):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            archivo_carnet = filename
            nombre_qr = filename.replace(".png", "_qr.png").replace(".jpg", "_qr.png")

            # URL pública del carnet
            url = f"https://carnets-flask.onrender.com/carnet/{archivo_carnet}"

            # Crear el QR
            img = qrcode.make(url)
            img.save(os.path.join(QR_DIR, nombre_qr))

    print("✓ QR generados correctamente en Render")
