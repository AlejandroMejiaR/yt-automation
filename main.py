from youtube_downloader import is_playlist, download_video, download_audio, download_playlist

def main():
    while True:
        # Recibir input del usuario
        link = input("Introduce el link del video de YouTube (o 'q' para salir): ")
        if link.lower() == 'q':
            break
        format = input("Introduce el formato (mp4/mp3/wav): ").lower()
        calidad = None
        if format == 'mp4':
            calidad = input("Introduce la calidad (rapida/mayor): ").lower()
        subir_a_drive = input("¿Deseas subir el archivo a Google Drive? (si/no): ").lower() == 'si'
        
        # Verificar si el enlace es una playlist
        if is_playlist(link):
            download_playlist(link, format, calidad, subir_a_drive)
        elif format == 'mp4':
            download_video(link, calidad, subir_a_drive)
        elif format in ['mp3', 'wav']:
            download_audio(link, format, subir_a_drive)

    print("Bye Bye.")

if __name__ == "__main__":
    main()
