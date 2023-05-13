from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd
import datetime as dt
import locale
import ast
from sklearn.neighbors import NearestNeighbors



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
@app.get("/peliculas_recomendadas/{pelicula}")
def Movies_ML(selected_title):
    df = pd.read_csv('datasets/movies_clean.csv')
    print(df['title'].head())
    df['tagline'] = df['tagline'].fillna('')
    
    # Drop rows with missing values in important columns
    df = df.dropna(subset=['overview', 'tagline', 'genre_names', 'title', 'id'])
    
    # Create a dataframe with dummy variables for genres
    generos_df = df['genre_names'].str.join(sep='|').str.get_dummies()
    
    # Compute genre similarity between movies
    selected_genres = df.loc[df['title'] == selected_title]['genre_names'].values
    if len(selected_genres) == 0:
        return "No se encontró la película " + selected_title
    selected_genres = ast.literal_eval(selected_genres[0])
    df['genre_similarity'] = df['genre_names'].apply(lambda x: len(set(selected_genres) & set(ast.literal_eval(x))) / len(set(selected_genres) | set(ast.literal_eval(x))))
    
    # Create a binary variable indicating whether movies belong to the same series
    df['same_series'] = df['title'].apply(lambda x: 1 if selected_title.lower() in x.lower() else 0)
    
    # Create a dataframe with all the relevant features
    features_df = pd.concat([generos_df, df['vote_average'], df['genre_similarity'], df['same_series']], axis=1)

    # Compute similar movies using k-NN
    k = 6
    knn = NearestNeighbors(n_neighbors=k+1, algorithm='auto')
    knn.fit(features_df)
    indices = knn.kneighbors(features_df.loc[df['title'] == selected_title])[1].flatten()
    recommended_movies = list(df.iloc[indices]['title'])

    # Sort recommended movies by relevance
    selected_score = df.loc[df['title'] == selected_title]['vote_average'].values[0]
    recommended_movies = sorted(recommended_movies, key=lambda x: (df.loc[df['title'] == x]['same_series'].values[0], df.loc[df['title'] == x]['vote_average'].values[0], df.loc[df['title'] == x]['genre_similarity'].values[0]), reverse=True)
    recommended_movies = [movie for movie in recommended_movies if movie != selected_title]

    # Print recommended movies
    if len(recommended_movies) == 0:
        return "No se encontraron películas similares a " + selected_title
    else:
        output_str = f"Película seleccionada: {selected_title} ({selected_score}):\n\nPelículas Recomendadas:\n"
        for i, pelicula in enumerate(recommended_movies[:5]):
            score = df.loc[df['title'] == pelicula]['vote_average'].values[0]
            genres = df.loc[df['title'] == pelicula]['genre_names'].values[0]
            gen_str = ', '.join(ast.literal_eval(genres))

            output_str += f"-{pelicula}  | Géneros: {gen_str} | Puntaje: {score} |\n"
            if i == 4:
                break
        return output_str











