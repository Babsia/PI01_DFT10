# PI01_DFT10.

Recomendador de películas y series

Descripción
Este proyecto consiste en la creación de un modelo de recomendación de películas y series para una startup que provee servicios de agregación de plataformas de streaming. El modelo es capaz de proporcionar recomendaciones personalizadas para cada usuario en función de sus preferencias y comportamiento previo.

Ciclo de vida del proyecto
Este proyecto sigue un ciclo de vida completo de un proyecto de Machine Learning. Incluye desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

Rol desempeñado
El objetivo de este proyecto era crear un sistema de recomendación de películas y series como Data Scientist en una startup. En este rol, se llevó a cabo la tarea de transformar los datos, desarrollar una API, realizar el análisis exploratorio de datos y proporcionar soluciones de implementación.

Transformaciones
Para el MVP, se realizaron las siguientes transformaciones a los datos:

Desanidar algunos campos, como belongs_to_collection, production_companies, y otros, para poder unirlos al dataset de nuevo hacer alguna de las consultas de la API.
Rellenar los valores nulos de los campos revenue y budget con el número 0.
Eliminar los valores nulos del campo release date.
Formatear las fechas con el formato AAAA-mm-dd y crear la columna release_year donde extraerán el año de la fecha de estreno.
Crear la columna return con el retorno de inversión, dividiendo los campos revenue y budget. Cuando no hay datos disponibles para calcularlo, se tomará el valor 0.
Eliminar las columnas que no serán utilizadas, video, imdb_id, adult, original_title, vote_count, poster_path y homepage.
Desarrollo de la API
Se desarrolló una API para acceder a los datos de la empresa utilizando el framework FastAPI. Las consultas disponibles son las siguientes:

peliculas_mes(mes): Esta función retorna la cantidad de películas que se estrenaron en un mes determinado históricamente. Se ingresa el mes en formato string, ejemplo 'enero'.
peliculas_dia(dia): Esta función retorna la cantidad de películas que se estrenaron en un día determinado de la semana históricamente. Se ingresa el día de la semana en formato string, ejemplo 'lunes'.
franquicia(franquicia): Esta función retorna la cantidad de películas, la ganancia total y el promedio de ganancia de una franquicia determinada. Se ingresa el nombre de la franquicia en formato string.
peliculas_pais(pais): Esta función retorna la cantidad de películas producidas en un país determinado. Se ingresa el nombre del país en formato string.
productoras(productora): Esta función retorna la ganancia total y la cantidad de películas que produjo una productora determinada. Se ingresa el nombre de la productora en formato string.
retorno(pelicula): Esta función retorna la inversión, la ganancia, el retorno y el año de lanzamiento de una película determinada. Se ingresa el nombre de la película en formato string.
Para cada función, se implementó un decorador @app.get() en la API.
