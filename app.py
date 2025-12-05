from flask import Flask, render_template, abort, send_from_directory
import os

app = Flask(__name__)

CARNETS_DIR = "static/carnets"

@app.route("/")
def index():
    imagenes = os.listdir(CARNETS_DIR)
    return render_template("index.html", imagenes=imagenes)

@app.route("/carnet/<name>")
def show_carnet(name):
    # Verifica si existe
    if not os.path.exists(os.path.join(CARNETS_DIR, name)):
        abort(404)
    return render_template("show.html", image_name=name)
