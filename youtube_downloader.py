from pytube import YouTube, Playlist
from pytube.exceptions import AgeRestrictedError
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import re

def is_playlist(link):
    # Verificar si el enlace contiene 'playlist?list=', lo que generalmente indica una playlist
    return 'playlist?list=' in link

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

def download_video(link, calidad, output_path="./mp4"):
    try:
        yt = YouTube(link)
    except AgeRestrictedError:
        print(f"Video restringido por edad: {link}")
        return
    
    if calidad == 'rapida':
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if video_stream:
            print(f"Descargando video: {yt.title} en resolución {video_stream.resolution}")
            sanitized_title = sanitize_filename(yt.title)
            video_stream.download(output_path, filename=f"{sanitized_title}.mp4")
        else:
            print("No se encontró un stream de video adecuado.")
    else:
        # Para calidad 'media' o 'mayor'
        video_stream = yt.streams.filter(file_extension='mp4', progressive=False).order_by('resolution').desc().first()
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        
        if video_stream and audio_stream:
            print(f"Descargando video: {yt.title} en resolución {video_stream.resolution}")
            sanitized_title = sanitize_filename(yt.title)
            
            video_path = video_stream.download(output_path, filename=f"{sanitized_title}_video.mp4")
            audio_path = audio_stream.download(output_path, filename=f"{sanitized_title}_audio.mp4")
            
            # Combinar video y audio
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)
            final_clip = video_clip.set_audio(audio_clip)
            
            final_clip.write_videofile(os.path.join(output_path, f"{sanitized_title}.mp4"), codec='libx264')
            
            # Eliminar archivos temporales
            video_clip.close()
            audio_clip.close()
            os.remove(video_path)
            os.remove(audio_path)
        else:
            print("No se encontró un stream de video o audio adecuado.")

def download_audio(link, format, output_path="./mp3"):
    yt = YouTube(link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream:
        print(f"Descargando audio: {yt.title}")
        sanitized_title = sanitize_filename(yt.title)
        audio_file = audio_stream.download(output_path, filename="temp_audio.mp4")
        
        # Convertir a mp3 o wav si es necesario
        base, ext = os.path.splitext(audio_file)
        new_file = os.path.join(output_path, f"{sanitized_title}.{format}")
        
        audio_clip = AudioFileClip(audio_file)
        try:
            audio_clip.write_audiofile(new_file, codec='mp3' if format == 'mp3' else 'pcm_s16le')
        except Exception as e:
            print(f"Error al convertir el archivo de audio: {e}")
        finally:
            audio_clip.close()
        
        os.remove(audio_file)  # Eliminar el archivo original .mp4
        print(f"Audio convertido a {format} y guardado como {new_file}")
    else:
        print("No se encontró un stream de audio adecuado.")

def download_playlist(link, format, calidad):
    pl = Playlist(link)
    playlist_title = pl.title
    sanitized_playlist_title = sanitize_filename(playlist_title)

    # Crear una carpeta para la playlist
    output_path = os.path.join("./Playlist", sanitized_playlist_title)
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Descargar cada video en la playlist
    for video in pl.videos:
        try:
            print(f"Descargando video: {video.title}")
            if format.lower() == 'mp4':
                download_video(video.watch_url, calidad, output_path)
            elif format.lower() in ['mp3', 'wav']:
                download_audio(video.watch_url, format, output_path)
        except AgeRestrictedError:
            print(f"Video restringido por edad: {video.watch_url}")
