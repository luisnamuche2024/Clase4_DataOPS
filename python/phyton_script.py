import os
#### carpeta dataset ####

location = 'C:/Users/Ingenieria/Documents/proyecto_parcial/python/dataset'

#### validad si existe carpeta ####

if not os.path.exists(location): ####  la carpeta no existe
      #### si la carpeta no existe, la creo ####  
      os.mkdir(location)
else: ####  la carpeta existe
     #### borrar contenido
     for root, dirs, files in os.walk(location,topdown=False): 
           for name in files:
                 os.remove(os.path.join(root,name))#### eliminar los archivos
           for name in dirs:
                 os.rmdir(os.path.join(root,name))#### eliminar los carpetas


#### importar libreria API kaggle #### 

from kaggle.api.kaggle_api_extended import KaggleApi 

#### Autenticarnos #### 

api= KaggleApi()
api.authenticate()

#### Descargar dataset ##
###print(api.dataset_list(search=''))

#### Descargar dataset ##

####api.dataset_download_file('rahulvyasm/netflix-movies-and-tv-shows','netflix_titles.csv',path="dataset",force = True, quiet = False)
api.dataset_download_files('rahulvyasm/netflix-movies-and-tv-shows',path=location,force = True, quiet = False,unzip=True)
