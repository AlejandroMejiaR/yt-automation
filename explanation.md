# Explicación del Código

Este archivo proporciona una descripción detallada de las funciones y la estructura del código en este proyecto.

## `main.py`

Este archivo es el punto de entrada principal del programa.

- **Función `main`**:
  - Solicita al usuario los enlaces de los videos de YouTube y el formato de descarga.
  - Pregunta si el usuario desea subir los archivos a Google Drive.
  - Llama a las funciones correspondientes para descargar y, si es necesario, subir los archivos.

## `youtube_downloader.py`

Este archivo contiene las funciones para descargar videos y audios de YouTube.

- **Función `is_playlist(link)`**:
  - Verifica si el enlace es una playlist de YouTube.

- **Función `sanitize_filename(filename)`**:
  - Elimina caracteres no válidos del nombre del archivo para asegurar que el nombre sea seguro para el sistema de archivos.

- **Función `download_video(link, calidad, subir_a_drive, output_path="./videos")`**:
  - Descarga un video de YouTube según la calidad especificada (rápida o mayor).
  - Si `subir_a_drive` es `True`, sube el archivo descargado a Google Drive, manteniendo la estructura de carpetas.

- **Función `download_audio(link, format, subir_a_drive, output_path="./audio")`**:
  - Descarga el audio de un video de YouTube en el formato especificado (mp3 o wav).
  - Si `subir_a_drive` es `True`, sube el archivo descargado a Google Drive, manteniendo la estructura de carpetas.

- **Función `download_playlist(link, format, calidad, subir_a_drive)`**:
  - Descarga todos los videos de una playlist de YouTube.
  - Llama a `download_video` o `download_audio` según el formato especificado para cada video en la playlist.

## `drive_uploader.py`

Este archivo maneja la autenticación y la subida de archivos a Google Drive.

- **Función `login()`**:
  - Maneja la autenticación en Google Drive utilizando las credenciales proporcionadas.

- **Función `subir_archivo(ruta_archivo, local_folder_path)`**:
  - Sube un archivo a Google Drive, manteniendo la estructura de carpetas local.
  - Utiliza `obtener_o_crear_carpeta` para asegurar que las carpetas necesarias existan en Google Drive.

- **Función `obtener_o_crear_carpeta(local_folder_path, credenciales)`**:
  - Verifica si una carpeta existe en Google Drive, y si no, la crea.
  - Navega a través de la estructura de carpetas local y crea las carpetas correspondientes en Google Drive si no existen.

## Limitaciones
- Si el video de YouTube está marcado como contenido con restricción de edad, no es posible descargarlo.
- La biblioteca `pytube` no permite descargar videos en la mayor calidad disponible en YouTube, sino que los descarga en un máximo de 1080p a 30fps al seleccionar una calidad mayor en el presente código. Si se desea filtrar de una forma específica, se puede revisar en la [documentación](https://pytube.io/en/latest/index.html).