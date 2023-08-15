Predicting House Prices

El objetivo de este modelo es predecir los precios futuros de la vivienda en base a características como pies cuadrados, baños, dormitorios, vistas y otras, vamos a construir un modelo de aprendizaje profundo que pueda predecir el precio futuro de las casas, que pueda ser consumido mediante un API

El alcance del proyecto: 

Crear con una línea base
 Crear un notebook con la solución del modelo que presente las distintas etapas para poder exponer el predictor del moldeo mediante un API.
Factorizar el anterior notebook para crear un archivo main que contenga las dependencias necesarias de las etapas Predict, Models, Preprocess, load, Train y Data.
Exponer la solución del modelo mediante un API, en la cual se pueda capturar información con baños, dormitorios, baños etc. y puede regresar la predicción del precio de las casas.

Dataset

Este conjunto de datos contiene precios de venta de casas para el condado de King, que incluye a Seattle. Incluye viviendas vendidas entre mayo de 2014 y mayo de 2015. 
21 columnas. 
21597 filas.

Feature

id: Identificación única para cada casa vendida
date: Fecha de la venta de la casa
price: Precio de cada vivienda vendida
bedrooms: Número de dormitorios
bathrooms: número de baños, donde 0,5 representa una habitación con inodoro pero sin ducha
sqft_living: pies cuadrados del espacio habitable interior de los apartamentos
sqft_lot: Pies cuadrados del espacio del terreno
floors: Número de plantas
waterfront: - Una variable ficticia para saber si el apartamento tiene vistas al paseo marítimo o no.
view: un índice de 0 a 4 de qué tan buena fue la vista de la propiedad
condition: - Un índice del 1 al 5 sobre el estado del apartamento,
grade: Un índice de 1 a 13, donde 1-3 no alcanza la construcción y el diseño de edificios, 7 tiene un nivel medio de construcción y diseño, y 11-13 tiene un nivel de construcción y diseño de alta calidad.
sqft_above: los pies cuadrados del espacio interior de la vivienda que está sobre el nivel del suelo
sqft_basement: los pies cuadrados del espacio interior de la vivienda que está por debajo del nivel del suelo
yr_built: el año en que se construyó inicialmente la casa
yr_renovated: El año de la última reforma de la casa
zipcode: en qué área de código postal se encuentra la casa
lat: latitud
long: Longitud
sqft_living15: Los pies cuadrados de espacio habitable de vivienda interior para los 15 vecinos más cercanos
sqft_lot15: Los pies cuadrados de los lotes de terreno de los 15 vecinos más cercanos

Actualmente se cuenta con un notebook que muestra una de las soluciones basada en una red neuronal ANN. Este problema también puede ser resuelto mediante distintos algoritmos como K-NN, Regresión Logística, Regresión Múltiple entre otros. 

El resultado final del proyecto, es poder realizar predicciones del precio de casas basado en información como, código postal, número de baños, latitud, longitud etc.