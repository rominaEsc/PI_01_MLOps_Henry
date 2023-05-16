
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>
# <p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">

## Objetivos:
Los objetivo de este MPV son:

### Transformaciones
- A partir del dataset [movies_Dataset.csv](https://github.com/rominaEsc/PI_01_MLOps_Henry/blob/main/movies_dataset.csv).
 realizar las siguientes transformaciones:

- Algunos campos, como belongs_to_collection, production_companies y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.

- Los valores nulos de los campos revenue, budget deben ser rellenados por el número 0.

- Los valores nulos del campo release date deben eliminarse.

- De haber fechas, deberán tener el formato AAAA-mm-dd, además deberán crear la columna release_year donde extraerán el año de la fecha de estreno.

- Crear la columna con el retorno de inversión, llamada return con los campos revenue y budget, dividiendo estas dos últimas revenue / budget, cuando no hay datos disponibles para calcularlo, deberá tomar el valor 0.

- Eliminar las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage.

_Estas transformaciones se realizaron en el archivo 1_ETL.ipynb. Este crea, en la carpeta data, los datasets a partir del archivo movies_Dataset.csv_ 

### Desarrollo API:
Crear 6 funciones para los endpoints que se consumirán en la API, que deben tener un decorador por cada una (@app.get(‘/’)).

- def peliculas_mes(mes): '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') historicamente''' return {'mes':mes, 'cantidad':respuesta}

- def peliculas_dia(dia): '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente''' return {'dia':dia, 'cantidad':respuesta}

- def franquicia(franquicia): '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio''' return {'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':respuesta, 'ganancia_promedio':respuesta}

- def peliculas_pais(pais): '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo''' return {'pais':pais, 'cantidad':respuesta}

- def productoras(productora): '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron''' return {'productora':productora, 'ganancia_total':respuesta, 'cantidad':respuesta}

- def retorno(pelicula): '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo''' return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia':respuesta,'retorno':respuesta, 'anio':respuesta}

_Estas funciones se realizaron y probaron en el archivo 2_funciones.ipynb_

### Deployment
Realizar el deployment para poder consumir la API

_Las consultas a la API pueden realizarse en el siguiente link: https://pi-01-mlops-henry.onrender.com/docs_

### Análisis exploratorio de los datos
Realizar un analisis exploratorio de datos. El EDA debería incluir gráficas interesantes para extraer datos.

_Pendiente_

### Sistema de recomendación
El sistema consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score de similaridad y devolverá una lista de Python con 5 valores, cada uno siendo el string del nombre de las películas con mayor puntaje, en orden descendente. Debe ser deployado como una función adicional de la API anterior y debe llamarse:

def recomendacion('titulo'): '''Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores''' return {'lista recomendada': respuesta}

_Pendiente_

## Video: 
Realizar un video mostrando el resultado de las consultas propuestas y de tu modelo de ML entrenado!

_ Video Explicativo del avance del proyecto_
 

