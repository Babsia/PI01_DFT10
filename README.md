# PROYECTO INDIVIDUAL HENRRY ML

# Proyecto de recomendación de películas
Este proyecto consiste en la creación de un sistema de recomendación de películas para una start-up que provee servicios de agregación de plataformas de streaming. En este README se describe el proceso seguido para la implementación del sistema de recomendación, así como la creación de una API para acceder a los datos de la empresa.

# Requerimientos
Para la implementación de este proyecto se han utilizado las siguientes herramientas y tecnologías:

Python 3.x
Pandas
FastAPI
Render
# Transformaciones de datos
Se han realizado las siguientes transformaciones en los datos para prepararlos para su uso en el modelo de recomendación:

Desanidar los campos "belongs_to_collection" y "production_companies" para poder unirlos al dataset y hacer consultas a la API.
Rellenar los valores nulos de los campos "revenue" y "budget" con el número 0.
Eliminar los valores nulos del campo "release date".
Dar formato AAAA-mm-dd a las fechas del campo "release date" y crear la columna "release_year" donde se extrae el año de la fecha de estreno.
Crear la columna "return" con el retorno de inversión, calculando la división entre "revenue" y "budget". En caso de que no haya datos disponibles para calcularlo, se toma el valor 0.
Eliminar las columnas que no serán utilizadas: "video", "imdb_id", "adult", "original_title", "vote_count", "poster_path" y "homepage".
# Desarrollo de la API
Se ha propuesto disponibilizar los datos de la empresa mediante el framework FastAPI, creando 6 funciones para los endpoints que se consumirán en la API:

peliculas_mes(mes): se ingresa el mes y la función retorna la cantidad de películas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') históricamente.
peliculas_dia(dia): se ingresa el día y la función retorna la cantidad de películas que se estrenaron ese día (de la semana, en str, ejemplo 'lunes') históricamente.
franquicia(franquicia): se ingresa la franquicia, retornando la cantidad de películas, ganancia total y promedio.
peliculas_pais(pais): se ingresa el país, retornando la cantidad de películas producidas en el mismo.
productoras(productora): se ingresa la productora, retornando la ganancia total y la cantidad de películas que produjeron.
retorno(pelicula): se ingresa la película, retornando la inversión, la ganancia, el retorno y el año en el que se lanzó.
# Deployment
Se ha utilizado Render para desplegar la API y permitir que sea consumida desde la web.

# Análisis exploratorio de datos
Se ha realizado un análisis exploratorio de los datos para investigar las relaciones que hay entre las variables de los datasets, ver si hay outliers o anomalías y ver si hay algún patrón interesante que valga la pena explorar en un análisis.

# Conclusión
Se ha creado un sistema de recomendación de películas y una API para acceder a los datos de la empresa. Se han realizado transformaciones de los datos para prepararlos para su uso en el modelo de recomendación, se ha desplegado la API en Render y se ha realizado un análisis exploratorio de los datos para investigar las relaciones que hay entre las variables. Este proyecto ha permitido mejorar los servicios de la start-up de agregación de plataformas de streaming y proporcionar recomendaciones de películas más precisas y personalizadas a los usuarios. Además, la creación de la API permite el acceso a los datos de la empresa de manera más sencilla y eficiente. En resumen, este proyecto ha sido una contribución valiosa para mejorar la calidad del servicio ofrecido por la start-up.
