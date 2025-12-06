from flask import Flask, render_template
import os
from generate_qrs import generar_todos_los_qr

app = Flask(__name__)

# Flag para asegurarnos de ejecutar solo una vez
qr_generado = False

@app.before_request
def ejecutar_qr_una_vez():
    global qr_generado
    if not qr_generado:
        generar_todos_los_qr()
        qr_generado = True

@app.route("/")
def index():
    carnets = [f for f in os.listdir("static/carnets") 
               if f.endswith((".png", ".jpg", ".jpeg"))]
    return render_template("index.html", carnets=carnets)

@app.route("/carnet/<filename>")
def mostrar_carnet(filename):
    return render_template("carnet_view.html", filename=filename)

if __name__ == "__main__":
    app.run(debug=True)

