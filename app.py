<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Ver Notas</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            background-color: #f5f5f5;
        }
        h1 { color: #333; text-align: center; }
        .card {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
        .nota-titulo {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-bottom: 8px;
        }
        .nota-contenido {
            color: #555;
            margin-bottom: 8px;
        }
        .nota-fecha {
            font-size: 12px;
            color: #999;
        }
        .empty {
            text-align: center;
            color: #999;
            padding: 30px;
        }
        a {
            display: block;
            text-align: center;
            margin-top: 15px;
            color: #4A90E2;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <h1>Notas Registradas</h1>

    {% if notas %}
        {% for nota in notas %}
        <div class="card">
            <div class="nota-titulo">{{ nota.titulo }}</div>
            <div class="nota-contenido">{{ nota.contenido }}</div>
            <div class="nota-fecha">{{ nota.fecha }}</div>
        </div>
        {% endfor %}
    {% else %}
        <div class="card empty">
            <p>No hay notas registradas aún.</p>
        </div>
    {% endif %}

    <a href="/">← Volver al menú</a>
</body>
</html>