from flask import Flask, render_template, request, redirect, url_for
import json, os
from datetime import datetime

app = Flask(__name__)

ARCHIVO_NOTAS    = "datos_notas.json"
ARCHIVO_HISTORIAL = "historial_tareas.txt"

#cambie algo saben ustedes que es?

# ─── FUNCIONES ─────────────────────────────────────────

def cargar_notas():
    if not os.path.exists(ARCHIVO_NOTAS):
        return []
    with open(ARCHIVO_NOTAS, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_nota(titulo, contenido):
    notas = cargar_notas()
    notas.append({
        "id": len(notas) + 1,
        "titulo": titulo,
        "contenido": contenido,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    with open(ARCHIVO_NOTAS, "w", encoding="utf-8") as f:
        json.dump(notas, f, ensure_ascii=False, indent=4)

def cargar_historial():
    if not os.path.exists(ARCHIVO_HISTORIAL):
        return []
    tareas = []
    with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as f:
        for linea in f:
            partes = linea.strip().split(" | ")
            tarea  = {}
            for p in partes:
                if ": " in p:
                    k, v = p.split(": ", 1)
                    tarea[k] = v
            if tarea:
                tareas.append(tarea)
    return tareas

def guardar_tarea(tarea, inicio, fin, estado):
    with open(ARCHIVO_HISTORIAL, "a", encoding="utf-8") as f:
        f.write(f"TAREA: {tarea} | INICIO: {inicio} | FIN: {fin} | ESTADO: {estado.upper()}\n")


# ─── RUTAS ─────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('Menu.html')

@app.route('/create_note', methods=['GET', 'POST'])
def Create():
    if request.method == 'POST':
        guardar_nota(request.form['titulo'], request.form['contenido'])
        return redirect(url_for('View'))
    return render_template('Create.html')

@app.route('/view_Note')
def View():
    return render_template('View.html', notas=cargar_notas())

@app.route('/view_history', methods=['GET', 'POST'])
def History():
    if request.method == 'POST':
        guardar_tarea(request.form['tarea'], request.form['fecha_inicio'],
                      request.form['fecha_final'], request.form['estado'])
        return redirect(url_for('History'))
    return render_template('History.html', tareas=cargar_historial())


# ─── RUN ───────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)
