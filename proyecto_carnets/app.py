from flask import Flask, render_template, abort
import os

app = Flask(__name__)

CARNETS_DIR = "static/carnets"

@app.route("/")
def index():
    # Lista todos los carnets disponibles
    imagenes = os.listdir(CARNETS_DIR)
    return render_template("index.html", imagenes=imagenes)

@app.route("/carnet/<name>")
def show_carnet(name):
    # Verifica que la imagen exista
    imagenes = os.listdir(CARNETS_DIR)
    if name not in imagenes:
        abort(404)
    return render_template("show.html", image_name=name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
