## Gestión del conjunto de datos

1. Descargar y descomprimir [conjunto de datos de cartas](https://www.kaggle.com/datasets/gpiosenka/cards-image-datasetclassification/data) en `./data/` y renombrar como `raw_cards`.

    Debería de quedar algo así:
        
        - PRACTICA_2/
            - data/
                - raw_cards/
                    - ...
                - sort.py


2. Eliminar modelos (aquellos con extensión `.h5`) y el fichero `.csv`. 

3. Ejecutar el script [sort.py](data/sort.py) desde la carpeta `./data/`

    Como resultado debería de haberse creado una nueva carpeta con las imágenes reordenadas:

        - PRACTICA_2/
            - data/
                - cards/ #Carpeta ordenada
                - raw_cards/
                    - ...
                - sort.py

Ya podemos borrar la carpeta `./data/raw_cards/`.