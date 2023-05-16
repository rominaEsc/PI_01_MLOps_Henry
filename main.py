from fastapi import FastAPI
import pandas as pd

app = FastAPI()


release_date = pd.read_csv("data/release_date.csv", sep=",")
production_countries = pd.read_csv("data/production_countries.csv", sep=",")
movies_production_countries = pd.read_csv("data/movies_production_countries.csv", sep=",")
collections = pd.read_csv("data/collections.csv", sep=",")
movies = pd.read_csv("data/movies.csv", sep=",")
production_companies = pd.read_csv("data/production_companies.csv", sep=",")
movies_production_companies = pd.read_csv("data/movies_production_companies.csv", sep=",")

# Funciones:
#1
@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    assert mes in ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'], f'Debe ingresar el nombre del mes en español. Ej: "Septiembre"'
    cantidad  = len(release_date[release_date['month']==mes])
    return {'mes':mes, 'cantidad':cantidad}

#2
@app.get('/peliculas_dis/{dis}')
def peliculas_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrebaron ese dia historicamente'''
    assert dia in ['lunes','martes','miercoles','jueves', 'viernes', 'sabado', 'domingo'], f'Debe ingresar el nombre del día en español(sin tilde). Ej: "miercoles"'
    cantidad  = len(release_date[release_date['day_name']==dia])
    return {'dia':dia, 'cantidad':cantidad}

#3
@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    id = collections[collections.name == franquicia].iloc[0,0]
    cantidad  = len(movies[movies['id_collection'] == id])
    ganancia_total = movies['revenue'][movies['id_collection']==id].sum()
    ganancia_promedio = movies['revenue'][movies['id_collection']==id].mean()
    return {'franquicia':franquicia, 'cantidad':cantidad,'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio}

#4
@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    assert pais in production_countries['name'].unique(), f'Error al ingresar el pais. Intente nuevamente. (Ej: "Germany)"'
    id = production_countries[production_countries.name == pais].iloc[0,0]
    cantidad  = len(movies_production_countries[movies_production_countries['id_production_countries']==id])
    return {'pais':pais, 'cantidad':cantidad}

#5
@app.get('/productoras/{productora}')
def productoras(productora:str):
    '''Ingresas la productora, retornando la ganancia toal y la cantidad de peliculas que produjeron'''
    id = production_companies[production_companies.name == productora].iloc[0,0]
    cantidad  = len(movies_production_companies[movies_production_companies['id_production_companies'] == id])
    lista_de_pelis = movies_production_companies['id_movie'][movies_production_companies['id_production_companies']==id].to_list()
    ganancia_total = movies['revenue'][movies['id_movie'].isin(lista_de_pelis)].sum()

    return {'productora':productora, 'ganancia_total':ganancia_total, 'cantidad':cantidad}

#6
@app.get('/retorno/{pelicula}')
def retorno(pelicula:str):
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    inversion = movies[movies.title == pelicula].iloc[0,12] # budget
    ganacia = movies[movies.title == pelicula].iloc[0,13] # revenue
    retorno = movies[movies.title == pelicula].iloc[0,14] # return
    anio_lanzamiento = movies[movies.title == pelicula].iloc[0,9] # release_year
    return {'pelicula':pelicula,'inversion':inversion, 'ganacia':ganacia,'retorno':retorno,'anio':anio_lanzamiento}

    # return {'pelicula':pelicula, 'inversion':inversion, 'ganacia':ganacia,'retorno':retorno, 'anio':anio_lanzamiento}

# # ML
# @app.get('/recomendacion/{titulo}')
# def recomendacion(titulo:str):
#     '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
#     return {'lista recomendada': respuesta}
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)