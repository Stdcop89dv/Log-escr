import os
import chardet

def buscar_cadena_en_archivos(carpeta, cadena):
    archivos_encontrados = {}
    for nombre_archivo in os.listdir(carpeta):
        ruta_archivo = os.path.join(carpeta, nombre_archivo)
        if os.path.isfile(ruta_archivo):
            try:
                # Detectar la codificación del archivo
                with open(ruta_archivo, 'rb') as archivo:
                    resultado = chardet.detect(archivo.read())
                    codificacion = resultado['encoding']

                # Leer el archivo con la codificación detectada
                with open(ruta_archivo, 'r', encoding=codificacion) as archivo:
                    lineas = archivo.readlines()
                    lineas_coincidentes = []
                    for i, linea in enumerate(lineas):
                        if cadena.lower() in linea.lower():
                            lineas_coincidentes.append(str(i))
                    if lineas_coincidentes:
                        archivos_encontrados[nombre_archivo] = lineas_coincidentes
            except Exception as e:
                print(f"Error al leer el archivo: {nombre_archivo}. Ignorando el archivo. Detalles: {str(e)}")
    return archivos_encontrados

if __name__ == '__main__':
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    cadena_buscar = input("Introduce la cadena a buscar en los archivos: ")
    archivos_encontrados = buscar_cadena_en_archivos(carpeta_actual, cadena_buscar)

    if archivos_encontrados:
        print("Archivos que contienen la cadena o parte de ella:")
        for archivo, lineas in archivos_encontrados.items():
            lineas_encontradas = ",".join(lineas)
            print(f"{archivo}: {lineas_encontradas}")
    else:
        print("No se encontró la cadena en ningún archivo.")
