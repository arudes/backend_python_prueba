from flask import Flask, jsonify, render_template
import json, sqlite3
from podcast import podcast
from best20podcast import bestPodcast 

app = Flask(__name__)

#Pagina HTML con detalles del proyecto
@app.route('/')
def principal():
    return render_template("index.html")

#Ruta de prueba que muestra los datos JSON guardados en el archivo podcast.py
@app.route('/podcast')
def getPodcast():
    return jsonify(podcast)

#Ruta para buscar un podcast especifico por medio del nombre del artista
@app.route('/podcast/<string:nombre>')
def searchPodcast(nombre):
    resultado = podcast[0]['feed']['results'] #Devuelve los podcast
    encontrados = [
        pod for pod in resultado if pod['artistName'] == nombre] #Itera en los podcast hasta encontrar el que se busca
    if(len(encontrados)>0):
        return jsonify({'pod': encontrados[0]}) #Retorna el que se encontro
    return jsonify({'message': 'Podcast no encontrado'})

#Ruta para crear un archivo JSON en la carpeta del proyecto con los 20 mejores podcast
@app.route('/best20')
def best():
    mejores = bestPodcast[0]['feed']['results']
    x=0
    resultado = []
    for x in range(20):
        resultado.append({'Bests': mejores[x]}) #Se crea una lista con los 20 mejores podcast
        if x == 20:
            break
    try:
        with open('C:\\Users\\Desarrollo\\Desktop\\Prueba_backend_python\\bestPodcast.json', 'w', encoding="utf-8") as file:
            json.dump(resultado, file, indent=4, ensure_ascii=False) #Se crea el documento JSON 
        return jsonify({"message":"Archivo generado con exito"})
    except KeyError:
        return jsonify({"message":"No se pudo generar el archivo"})

#Ruta para reemplazar los 20 mejores por los 20 ultimos podcast en el mismo archivo
@app.route('/last20')
def last():
    mejores = bestPodcast[0]['feed']['results']
    ultimos = []
    for x in range(100):
        if x >= 80:
            ultimos.append({'Last': mejores[x]}) #Se obtienen los ultimos 20
    try:
        with open('C:\\Users\\Desarrollo\\Desktop\\Prueba_backend_python\\bestPodcast.json','w', encoding='utf-8') as file:
            json.dump(ultimos, file, indent=4, ensure_ascii=False) #Se crea el archivo
        return jsonify({"message":"Archivo reemplazado con exito"})
    except KeyError:
        return jsonify({"message":"Error no se realizo la accion"})

#Ruta para eliminar un podcast por nombre del artista
@app.route('/podcastdel/<string:id>')
def deletePodcast(id):
    resultado = podcast[0]['feed']['results']
    encontrados = [
        d for d in resultado if d['artistName'] == id] #Busca el podcast por nombre del artista
    if (len(encontrados) > 0):
        resultado.remove(encontrados[0]) #Devuelve lo encontrado
        return jsonify({
            'message':'Podcast eliminado',
            'Lista de podcast': resultado
            })

#Usando una base de datos SQlite
#Lista los 20 podcast de la base de datos datbase/podcast.db
@app.route('/podcastdb')
def dbpodcast():
    con = sqlite3.connect('database/podcast.db')
    c = con.cursor()
    fila = c.execute("SELECT * FROM podcast")
    resultado = c.fetchall()
    veinte =[]
    for x in range(20):
        veinte.append({'Bests20': resultado[x]})
    return jsonify(veinte)

if __name__ == '__main__':
    app.run(debug=True, port=4000)