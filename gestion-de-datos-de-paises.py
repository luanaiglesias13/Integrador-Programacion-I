import csv

ARCHIVO = "dataset de paises.csv"
COLUMNAS = ['nombre', 'poblacion', 'superficie', 'continente']
paises = []

#Funcion crear archivo

def crear_archivo(lista):
    try:
        with open(ARCHIVO, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            for dicc in lector:
                dicc['poblacion'] = int(dicc['poblacion'])
                dicc['superficie'] = int(dicc['superficie'])
                lista.append(dicc)
        return lista

    except FileNotFoundError:
        with open(ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)

            escritor.writeheader()
        return lista

    except Exception as e:
        print(f"Ocurrió un error inesperado, ERROR: {e}")

#Funcion validar pais

def validar_nombre(nombre, lista):
    if not nombre.replace(" ", "").isalpha():
        print("(!) Ingrese un nombre válido.")
        return False
    elif buscar_pais(nombre, lista) is not False:
        print("(!) El país ya se encuentra cargado en la lista.")
        return False
    return True

#Buscar pais

def buscar_pais(pais, lista):
    pais = quitar_tildes(pais)

    for dicc in lista:
        nombre_limpio = quitar_tildes(dicc['nombre'])

        if pais.lower() == nombre_limpio.lower():
            return dicc
    return False

#Funcion validar numero entero

def validar_entero(numero):
    try:
        numero = int(numero)

        if numero <= 0:
            print("(!) El dato ingresado no puede ser menor a 1.")
            return False
        return numero
    except ValueError:
        print("(!) Ingrese un número entero.")
        return False

#validar continente

def validar_continente(continente):
    if continente.lower() not in ("america", "africa", "oceania", "europa", "asia"):
        print("(!) El continente ingresado no existe.")
        return False
    return True

#sacar tildes

def quitar_tildes(texto):
    texto = texto.lower()
    remplazos = (
      ("á", "a"),
      ("é", "e"),
      ("í", "i"),
      ("ó", "o"),
      ("ú", "u"),
  )

    for a, b in remplazos:
        texto = texto.replace(a, b)
    return texto

#===========================================================

def agregar_pais(lista):
    print(f"\n      「    AGREGAR PAÍS    」\n")
    while True:
        pais = input(">País: ").strip().title()

        if validar_nombre(pais, lista):
            break

    while True:
        poblacion = input(">Población: ").strip()

        poblacion = validar_entero(poblacion)

        if poblacion is not False:
            break

    while True:
        superficie = input(">Superficie en km²: ").strip()

        superficie = validar_entero(superficie)

        if superficie is not False:
            break

    while True:
        continente = input(">Continente: ").strip().title()

        continente_limpio = quitar_tildes(continente)

        if validar_continente(continente_limpio):
            break

#Creamos el archivo o cargamos la lista:
crear_archivo(paises)
print(paises) #esto hay que sacarlo

opcion = ""

while opcion != "7":

    print(f"""
⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢
﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉
        MENÚ DE GESTIÓN DE DATOS DE PAISES
﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍﹍
⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣⌣

1. Agregar país
2. Actualizar Población y Superficie
3. Buscar país
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. SALIR
""")

    opcion = input("Ingrese la opción que desea realizar: ").strip()

    match opcion:
        case "1":
            agregar_pais(paises)
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            print("Saliendo del programa...")
        case _:
            print("(!) Debe ingresar una opción dentro del rango.")
