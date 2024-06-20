# YouTube Downloader and Uploader

Este proyecto permite descargar videos y audios de YouTube y subirlos a una carpeta de Google Drive. 

## Funcionalidades

- Descargar videos de YouTube en formato MP4.
- Descargar audios de YouTube en formato MP3 o WAV.
- Elegir entre dos calidades para los videos: rápida (maximo 720p) y mayor (resolución más alta disponible posible).
- Subir los archivos descargados a Google Drive manteniendo la estructura de carpetas local.

## Requisitos

- Python 3.x
- Las siguientes bibliotecas de Python:
  - `pytube`
  - `moviepy`
  - `pydrive2`

## Instalación

1. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

2. Configura las credenciales de Google Drive:
    - Crea un proyecto en Google Cloud Console, activa la API de Google Drive y genera un client ID y client secret.
    - Pega el client ID y client secret en el archivo `settings.yaml`.
      
    - Ejecuta `drive_quickstart.py` para autenticarse en la aplicación y obtener las credenciales del usuario:
      ```bash
      python drive_quickstart.py
      ```
    - Añade al código `drive_uploader.py` el ID de la carpeta donde se van a subir los vídeos descargados de YouTube.

## Uso

Para ejecutar el script principal:

```bash
python main.py
 ```
 
## Proyecto Base

Este proyecto es una modificación de un proyecto original creado por [Valantoni](https://github.com/valantoni/yt-automation). Puedes ver el video explicativo del proyecto original [aquí](https://www.youtube.com/watch?v=JHjOZRcuqmE&t=523s&ab_channel=ToniDev).
