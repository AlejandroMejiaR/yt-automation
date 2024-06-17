from excel_handler import save_video_links
from youtube_downloader import is_playlist, download_video, download_audio, download_playlist
import pandas as pd

def main():
    # Ruta y configuración del archivo Excel
    file_path = 'enlaces_videos/enlaces.xlsx'
    sheet_name = 'Hoja1'
    
    # Crear un DataFrame vacío si el archivo no existe
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Videos", "Formato", "Playlist", "Calidad"])
        df.to_excel(file_path, sheet_name=sheet_name, index=False)

    while True:
        # Recibir input del usuario
        link = input("Introduce el link del video de YouTube (o 'q' para salir): ")
        if link.lower() == 'q':
            break
        format = input("Introduce el formato (mp4/mp3/wav): ").lower()
        calidad = None
        if format == 'mp4':
            calidad = input("Introduce la calidad (rapida/mayor): ").lower()
        
        # Verificar si el enlace es una playlist
        playlist_status = "Si" if is_playlist(link) else "No"

        # Guardar los datos en el Excel
        save_video_links(file_path, sheet_name, link, format, playlist_status, calidad)

        # Descargar el video o el audio según el formato seleccionado
        if playlist_status == "Si":
            download_playlist(link, format, calidad)
        elif format == 'mp4':
            download_video(link, calidad)
        elif format in ['mp3', 'wav']:
            download_audio(link, format)

    print("Enlaces guardados en el Excel con éxito.")

if __name__ == "__main__":
    main()
