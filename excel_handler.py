import pandas as pd

def save_video_links(file_path, sheet_name, link, format, playlist_status, calidad):
    # Intentar leer el archivo Excel existente, si no existe, crear un DataFrame vacío
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Videos", "Formato", "Playlist", "Calidad"])

    # Crear una nueva fila con los datos del enlace de video
    new_row = pd.DataFrame({
        "Videos": [link],
        "Formato": [format],
        "Playlist": [playlist_status],
        "Calidad": [calidad]
    })
    # Añadir la nueva fila al DataFrame existente
    df = pd.concat([df, new_row], ignore_index=True)
    
    # Guardar el DataFrame actualizado en el archivo Excel
    df.to_excel(file_path, sheet_name=sheet_name, index=False)
