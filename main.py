from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd
import datetime as dt
import locale


app = FastAPI()

df = pd.read_csv('datasets/movies_clean.csv')
df['release_date'] = pd.to_datetime(df['release_date'])
df['release_month'] = df['release_date'].dt.month_name()
df['release_day'] = df['release_date'].dt.day_name()
def traductor_mes():
    meses = {'January':'Enero', 'February':'Febrero', 'March':'Marzo', 'April':'Abril', 'May':'Mayo', 'June':'Junio', 'July':'Julio', 'August':'Agosto', 'September':'Septiembre', 'October':'Octubre', 'November':'Noviembre', 'December':'Diciembre'}
    df['release_month'] = df['release_month'].map(meses)
traductor_mes()
def traductor_dia():
    dias = {'Monday':'Lunes', 'Tuesday':'Martes', 'Wednesday':'Miercoles', 'Thursday':'Jueves', 'Friday':'Viernes', 'Saturday':'Sabado', 'Sunday':'Domingo'}
    df['release_day'] = df['release_day'].map(dias)
traductor_dia()

@app.get("/peliculas_mes/{mes}")
def peliculas_mes(mes):
    # Obtiene la cantidad de películas estrenadas en el mes especificado
    df_mes = df[df['release_month'] == mes]
    cantidad = len(df_mes)
    return {'mes':mes, 'cantidad':cantidad}
@app.get("/peliculas_dia/{dia}")
def peliculas_dia(dia):
    # Obtiene la cantidad de películas estrenadas en el día especificado
    df_dia = df[df['release_day'] == dia]
    cantidad = len(df_dia)
    return {'dia':dia, 'cantidad':cantidad}
@app.get("/franquicia/{franquicia}")
def franquicia(franquicia):
    # Obtiene la cantidad de películas, la ganancia total y el promedio de ganancias para la franquicia especificada
    df_franquicia = df[df['collection_name'] == franquicia]
    cantidad = len(df_franquicia)
    ganancia_total = df_franquicia['revenue'].sum()
    ganancia_promedio = df_franquicia['revenue'].mean()
    return {'franquicia':franquicia, 'cantidad':cantidad, 'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio}
@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais):
    # Obtiene la cantidad de películas producidas en el país especificado
    df_pais = df[df['country'] == pais]
    cantidad = len(df_pais)
    return {'pais':pais, 'cantidad':cantidad}
@app.get("/productoras/{productora}")
def productoras(productora):
    #productio_companies_name esta en el dataset como una lista con todas las productoras de la pelicula, por lo que se debe buscar en cada lista si esta la productora
    df_productora = df[df['production_companies_names'].str.contains(productora)]
    cantidad = len(df_productora)
    ganancia_total = df_productora['revenue'].sum()
    return {'productora':productora, 'ganancia_total':ganancia_total, 'cantidad':cantidad}

@app.get("/retorno/{pelicula}")
def retorno(pelicula):
    #def retorno(pelicula): '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo''' return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia':respuesta,'retorno':respuesta, 'anio':respuesta}
    df_pelicula = df[df['title'] == pelicula]
    inversion = df_pelicula['budget'].sum()
    ganancia = df_pelicula['revenue'].sum()
    retorno = df_pelicula['return'].sum()
    anio = df_pelicula['release_year'].sum()
    
    return {'pelicula':pelicula, 'inversion':inversion, 'ganacia':ganancia,'retorno':retorno, 'año':anio}










'''@app.get("/peliculas_dia/{dia}")
def peliculas_dia(dia: str):
    respuesta = 0
    # Obtiene la cantidad de películas estrenadas en el día especificado
    # Puedes implementar la lógica para obtener esta información desde el dataframe aquí
    return {'dia':dia, 'cantidad':respuesta}

# Función para obtener información sobre una franquicia
@app.get("/franquicia/{franquicia}")
def franquicia(franquicia: str):
    respuesta_cantidad = 0
    respuesta_ganancia_total = 0
    respuesta_ganancia_promedio = 0
    # Obtiene la cantidad de películas, la ganancia total y el promedio de ganancias para la franquicia especificada
    # Puedes implementar la lógica para obtener esta información desde el dataframe aquí
    return {'franquicia':franquicia, 'cantidad':respuesta_cantidad, 'ganancia_total':respuesta_ganancia_total, 'ganancia_promedio':respuesta_ganancia_promedio}

# Función para obtener cantidad de películas producidas en un país
@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais: str):
    respuesta = 0
    # Obtiene la cantidad de películas producidas en el país especificado
    # Puedes implementar la lógica para obtener esta información desde el dataframe aquí
    return {'pais':pais, 'cantidad':respuesta}

# Función para obtener información sobre una productora
@app.get("/productoras/{productora}")
def productoras(productora: str):
    respuesta_cantidad = 0
    respuesta_ganancia_total = 0
    # Obtiene la cantidad de películas producidas y la ganancia total para la productora especificada
    # Puedes implementar la lógica para obtener esta información desde el dataframe aquí
    return {'productora':productora, 'ganancia_total':respuesta_ganancia_total, 'cantidad':respuesta_cantidad}

# Función para obtener información sobre una película específica
@app.get("/retorno/{pelicula}")
def retorno(pelicula: str):
    respuesta_inversion = 0
    respuesta_ganancia = 0
    respuesta_retorno = 0
    respuesta_anio = 0
    # Obtiene información sobre la inversión, ganancia, retorno y año de una película específica
    # Puedes implementar la lógica para obtener esta información desde el dataframe aquí
    return {'pelicula':pelicula, 'inversion':respuesta_inversion, 'ganacia':respuesta_ganancia,'retorno':respuesta_retorno, 'anio':respuesta_anio}'''
