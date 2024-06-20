from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

# Ruta a las credenciales de Google Drive
directorio_credenciales = 'credentials_module.json'
# ID de la carpeta en Google Drive donde se subirán los archivos
id_folder = ''

# Iniciar sesión en Google Drive
def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = directorio_credenciales
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)
    
    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8092])
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(directorio_credenciales)
    credenciales = GoogleDrive(gauth)
    return credenciales

# Subir un archivo a Google Drive
def subir_archivo(ruta_archivo, local_folder_path):
    credenciales = login()
    folder_id = obtener_o_crear_carpeta(local_folder_path, credenciales)
    archivo = credenciales.CreateFile({'parents': [{"kind": "drive#fileLink", "id": folder_id}]})
    archivo['title'] = os.path.basename(ruta_archivo)
    archivo.SetContentFile(ruta_archivo)
    archivo.Upload()

def obtener_o_crear_carpeta(local_folder_path, credenciales):
    # Verificar si la carpeta ya existe en Google Drive, si no, crearla
    folder_names = local_folder_path.split(os.sep)
    parent_id = id_folder
    for folder_name in folder_names:
        query = f"title='{folder_name}' and mimeType='application/vnd.google-apps.folder' and '{parent_id}' in parents and trashed=false"
        folder_list = credenciales.ListFile({'q': query}).GetList()
        if folder_list:
            parent_id = folder_list[0]['id']
        else:
            folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [{'id': parent_id}]}
            folder = credenciales.CreateFile(folder_metadata)
            folder.Upload()
            parent_id = folder['id']
    return parent_id
