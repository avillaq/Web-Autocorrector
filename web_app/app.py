from flask import Flask, request, render_template, url_for, send_from_directory
from autocorrect import Speller
import os
import json

app = Flask(__name__)

# Cargamos los datos
with open("data/cess_esp_word_count.json", "r", encoding="utf-8") as file:
    nlp_data = json.load(file)

speller = Speller(lang="es", nlp_data=nlp_data)

# Carpeta para guardar los archivos corregidos
CARPETA_ARCHIVOS = os.path.join(os.path.dirname(__file__), "archivos_corregidos")
if not os.path.exists(CARPETA_ARCHIVOS):
    os.makedirs(CARPETA_ARCHIVOS)

def limpiar_carpeta():
    for archivo in os.listdir(CARPETA_ARCHIVOS):
        ruta_archivo = os.path.join(CARPETA_ARCHIVOS, archivo)
        if os.path.isfile(ruta_archivo):
            os.unlink(ruta_archivo)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")
    
    elif request.method == "POST":
        if "texto" in request.form:
            texto = request.form["texto"]
            
            texto_corregido = speller(texto)
            return render_template("index.html", texto=texto, texto_corregido=texto_corregido)
        
        elif "archivos" in request.files:
            archivos = request.files.getlist("archivos")
            limpiar_carpeta()
            archivos_procesados = []
            for archivo in archivos:
                if archivo.filename != "":
                    ruta_archivo = os.path.join(CARPETA_ARCHIVOS, archivo.filename)
                    archivo.save(ruta_archivo)

                    with open(ruta_archivo, "r", encoding="utf-8") as file:
                        texto = file.read()
                        texto_corregido = speller(texto)
                    with open(ruta_archivo, "w", encoding="utf-8") as file:
                        file.write(texto_corregido)
                        archivos_procesados.append({
                            "nombre": archivo.filename,
                            "texto_corregido": texto_corregido,
                            "url": url_for("descargar_archivo", nombre_archivo=f"{archivo.filename}")
                        })

            return render_template("index.html", archivos_corregidos=archivos_procesados)
        
        return render_template("index.html")

@app.route("/descargar/<nombre_archivo>")
def descargar_archivo(nombre_archivo):
    return send_from_directory(CARPETA_ARCHIVOS, nombre_archivo, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)