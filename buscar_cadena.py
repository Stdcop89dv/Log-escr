import os

def buscar_cadena_en_archivos(carpeta, cadena):
    archivos_encontrados = []
    for nombre_archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                if cadena in contenido:
                    archivos_encontrados.append(nombre_archivo)
    return archivos_encontrados

if __name__ == '__main__':
    carpeta = input("Introduce la ruta de la carpeta a buscar: ")
    cadena_buscar = input("Introduce la cadena a buscar en los archivos: ")
    archivos_encontrados = buscar_cadena_en_archivos(carpeta, cadena_buscar)

    if archivos_encontrados:
        print("Archivos que contienen la cadena:")
        for archivo in archivos_encontrados:
            print(archivo)
    else:
        print("No se encontró la cadena en ningún archivo.")
