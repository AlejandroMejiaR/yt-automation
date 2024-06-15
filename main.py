from excel_handler import save_video_links
from youtube_downloader import is_playlist
import pandas as pd

def main():
    # Ruta y configuración del archivo Excel
    file_path = 'enlaces_videos/enlaces.xlsx'
    sheet_name = 'Hoja1'
    
    # Crear un DataFrame vacío si el archivo no existe
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Videos", "Formato", "Playlist"])
        df.to_excel(file_path, sheet_name=sheet_name, index=False)

    while True:
        # Recibir input del usuario
        link = input("Introduce el link del video de YouTube (o 'q' para salir): ")
        if link.lower() == 'q':
            break
        format = input("Introduce el formato (mp4/mp3): ")
        
        # Verificar si el enlace es una playlist
        playlist_status = "Si" if is_playlist(link) else "No"

        # Guardar los datos en el Excel
        save_video_links(file_path, sheet_name, link, format, playlist_status)

    print("Enlaces guardados en el Excel con éxito.")

if __name__ == "__main__":
    main()
