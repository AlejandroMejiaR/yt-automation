from pytube import YouTube
from pytube import Playlist

def is_playlist(link):
    # Verificar si el enlace contiene 'list=', lo que generalmente indica una playlist
    return 'playlist?list=' in link

    
def download_video(link, resolution="720p", output_path="./YT"):
    yt = YouTube(link)
    video_stream = yt.streams.filter(res=resolution, file_extension='mp4').first()
    if video_stream:
        print(f"Descargando video: {link} en resolución {resolution}")
        video_stream.download(output_path)
    else:
        print(f"No se encontró un stream de video para la resolución {resolution}")

def download_audio(link, output_path="./YT", audio_format="mp3"):
    yt = YouTube(link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream:
        print(f"Descargando audio: {link}")
        audio_file = audio_stream.download(output_path)
        # Convertir a mp3 si es necesario
        if audio_format == "mp3":
            from moviepy.editor import AudioFileClip
            audio_clip = AudioFileClip(audio_file)
            audio_clip.write_audiofile(audio_file.replace(".mp4", ".mp3"))
            audio_clip.close()