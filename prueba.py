import requests
import pandas as pd

# URL de la API y token de autenticación (reemplázalos por los valores reales)
url = "http://127.0.0.1:8000//api/MovieView/"
headers = {
    "Authorization": "Token 8a01c32363157c4a717fc9ad5441366b7712cfe7"
}

# Datos del registro que deseas enviar (incluyendo la corrección para el campo "poster")
registro = {
    "title": "Paw Patrol: La súper película (2023)",
    "release_date": "2023-10-21",
    "url_movie": "https://gnula.nu/animacion/ver-paw-patrol-la-super-pelicula-2023-online/",
    "description": "Cuando un meteorito mágico se estrella en Ciudad Aventura, los cachorros de la Patrulla Canina consiguen unos superpoderes que los transforman en ¡Los PODEROSOS CACHORROS! Para Skye, la más pequeña del equipo, sus nuevos poderes son un sueño hecho realidad. Pero las cosas se complican cuando Humdinger, el archienemigo de los cachorros que acaba de fugarse de la cárcel, se une a Victoria Vance, una desquiciada científica obsesionada con los meteoritos, y forman una alianza para robar los superpoderes y convertirse en supervillanos. Con el destino de Ciudad Aventura al filo del abismo, los Poderosos Cachorros tendrán que detener a los supervillanos antes de que sea demasiado tarde, y Skye descubrirá que hasta la más pequeña del equipo puede ser la que determine el resultado.",
    "poster": (open("static\img\movie_posters\PAW_Patrol_The_Mighty_Movie_poster_usa.jpg", "rb"), "static\img\movie_posters\PAW_Patrol_The_Mighty_Movie_poster_usa.jpg"),
    "channel": 1,
    "genre": [6]
}

# Realizar la solicitud POST con la cabecera de autenticación y los datos
response = requests.post(url, headers=headers, data=registro)

# Verificar si la solicitud fue exitosa (código de respuesta 201 para creación exitosa)
if response.status_code == 201:
    # La respuesta se encuentra en formato JSON, puedes acceder a los datos así:
    new_movie = response.json()
    print("Película creada exitosamente:")
    print(new_movie)
else:
    print(f"Error al hacer la solicitud POST. Código de respuesta: {response.status_code}")