from fastapi import FastAPI
import pandas as pd

app = FastAPI()


release_date = pd.read_csv("release_date.csv", sep=",")
production_countries = pd.read_csv("production_countries.csv", sep=",")
movies_production_countries = pd.read_csv("movies_production_countries.csv", sep=",")

@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str):
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    # assert mes in ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'], f'Debe ingresar el nombre del mes en español. Ej: "Septiembre"'
    cantidad  = len(release_date[release_date['month']==mes])
    return {'mes':mes, 'cantidad':cantidad}

@app.get('/peliculas_dis/{dis}')
def peliculas_dia(dia:str):
    '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrebaron ese dia historicamente'''
    assert dia in ['lunes','martes','miercoles','jueves', 'viernes', 'sabado', 'domingo'], f'Debe ingresar el nombre del mes en español. Ej: "Septiembre"'
    cantidad  = len(release_date[release_date['day_name']==dia])
    return {'dia':dia, 'cantidad':cantidad}

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais:str):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    assert pais in production_countries['name'].unique(), f'Error al ingresar el pais. Intente nuevamente. (Ej: "Germany)"'
    id = production_countries[production_countries.name == pais].iloc[0,0]
    cantidad  = len(movies_production_countries[movies_production_countries['id_production_countries']==id])
    return {'pais':pais, 'cantidad':cantidad}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)