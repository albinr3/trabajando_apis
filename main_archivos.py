import requests

if __name__=='__main__':
    url='https://i.imgur.com/ocpoGKN.jpeg'
    
    response = requests.get(url, stream=True) #realiza la peticion sin cerrar la conexion, para despues descargar el archivo
    with open("imagen.jpg", "wb") as f:
        for chunk in response.iter_content(): #descargar la imagen poco a poco
            f.write(chunk)
    response.close
