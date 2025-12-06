from flask import Flask, render_template
import os
# Generar QR automáticamente al iniciar
from generate_qrs import generar_todos_los_qr

@app.before_first_request
def generar_qrs_en_render():
    generar_todos_los_qr()

app = Flask(__name__)

@app.route("/")
def index():
    carnets = [f for f in os.listdir("static/carnets") if f.endswith((".png", ".jpg", ".jpeg"))]
    return render_template("index.html", carnets=carnets)

@app.route("/carnet/<filename>")
def mostrar_carnet(filename):
    return render_template("carnet_view.html", filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
