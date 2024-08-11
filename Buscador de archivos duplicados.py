import os
import hashlib

def calcular_hash( ruta, Tamaño_bloque=65536 ):
    hasher = hashlib.sha256()
    with open(ruta,'rb') as archivo:
        bloque = archivo.read(Tamaño_bloque)
        while len(bloque) > 0:
            hasher.update(bloque)
            bloque = archivo.read(Tamaño_bloque)
    return hasher.hexdigest()

def BAD(directorio):
    archivos_duplicados = {}
    for directrio_raiz, _, archivo in os.walk(directorio):
        for nombre_arch in archivo:
            ruta = os.path.join(directrio_raiz,nombre_arch)
            hash_archivo = calcular_hash(ruta)
            if hash_archivo in archivos_duplicados:
                archivos_duplicados[hash_archivo].append(ruta)
            else:
                archivos_duplicados[hash_archivo] = [ruta]
    return {hash_archivo: ruta for hash_archivo, ruta in archivos_duplicados.items() if len(ruta) > 1}

directorio = input("Ingrse el directorio: ")
archivos_duplicados = BAD(directorio)

if archivos_duplicados:
    print("Archivos duplicados encontrados: ")
    for hash_archivo, rutas in archivos_duplicados.items():
        print("Hash:",hash_archivo)
        for ruta in rutas:
            print("-",ruta)
else:
    print("No se encontrado archivos duplicados en el directorio")