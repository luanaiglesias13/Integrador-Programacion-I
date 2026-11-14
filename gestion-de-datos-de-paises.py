import csv

ARCHIVO = "dataset de paises.csv"
COLUMNAS = ['nombre', 'poblacion', 'superficie', 'continente']
paises = []

#============ CREAR ARCHIVO ============

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

#============ ACTUALIZAR ARCHIVO ============

def actualizar_archivo(lista):
    with open(ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)

        escritor.writeheader()

        escritor.writerows(lista)
    print(">>ARCHIVO ACTUALIZADO<<")

#============ VALIDAR ESTADO DE LA LISTA ============

def validar_lista(lista):
    if len(lista) == 0:
        print("(!) La lista se encuentra vacía, cargue al menos 1 país para continuar.")
        return False
    return True

#============ QUITAR TÍLDES ============

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

#============ BUSCAR PAÍS ============

def buscar_pais(pais, lista):
    pais = quitar_tildes(pais)

    for dicc in lista:
        nombre_limpio = quitar_tildes(dicc['nombre'])

        if pais.lower() == nombre_limpio.lower():
            return dicc
    return False

#============ VALIDAR NOMBRE ============

def validar_nombre(nombre, lista):
    if not nombre.replace(" ", "").isalpha():
        print("(!) Ingrese un nombre válido.")
        return False
    elif buscar_pais(nombre, lista) is not False:
        print("(!) El país ya se encuentra cargado en la lista.")
        return False
    return True

#============ VALIDAR NÚM ENTERO ============

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

#============ VALIDAR CONTINENTE ============

def validar_continente(continente):
    continente = quitar_tildes(continente)

    if continente.lower() not in ("america", "africa", "oceania", "europa", "asia"):
        print("(!) El continente ingresado no existe.")
        return False
    return True

#============ MOSTRAR INFO ============

def mostrar_info(lista):
    for diccionario in lista:
        print(f"País: {diccionario['nombre']} | Población: {diccionario['poblacion']} | Superficie: {diccionario['superficie']} | Continente: {diccionario['continente']}")

#=======================================
# 1. AGREGAR PAÍS
#=======================================

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

        if validar_continente(continente):
            break

    lista.append({'nombre': pais, 'poblacion': poblacion, 'superficie': superficie, 'continente': continente})
    print(">> País agregado con éxito!")
    actualizar_archivo(lista)

#=======================================
# 2. ACTUALIZAR DATOS
#=======================================

def actualizar_datos(lista):
    if validar_lista(lista):
        print(f"\n      「    ACTUALIZAR DATOS    」\n")

        pais_actualizar = input("Ingrese el país del que desea actualizar sus datos: ").strip().title()

        dicc_actualizar = buscar_pais(pais_actualizar, lista)

        if dicc_actualizar is not False:

            while True:
                poblacion_nueva = input(">Población actualizada: ").strip()

                poblacion_nueva = validar_entero(poblacion_nueva)

                if poblacion_nueva is not False:
                    dicc_actualizar['poblacion'] = poblacion_nueva
                    print(">> Población actualizada con éxito!")
                    break

            while True:
                superficie_actualizar = input(">Superficie actualizada: ").strip()

                superficie_actualizar = validar_entero(superficie_actualizar)

                if superficie_actualizar is not False:
                    dicc_actualizar['superficie'] = superficie_actualizar
                    print(">> Superficie actualizada con éxito!")
                    break
            actualizar_archivo(lista)
        else:
            print("(!) El país no se encuentra cargado en la lista.")

#=======================================
# 3. BÚSQUEDA
#=======================================

def busqueda(lista):
    if validar_lista(lista):
        print(f"\n      「    BUSQUEDA DE PAÍSES    」\n")

        coincidencias = []

        encontrado = False

        pais_buscar = input("Qué país está buscando? ").strip().title()

        dicc_buscado = buscar_pais(pais_buscar, lista)

        if dicc_buscado is not False:
            print(">>Se encontró 1 coincidencia:")
            print(f"País: {dicc_buscado['nombre']} | Población: {dicc_buscado['poblacion']} | Superficie: {dicc_buscado['superficie']} | Continente: {dicc_buscado['continente']}")
            encontrado = True

        else:
            pais_buscar = quitar_tildes(pais_buscar)
            
            for d in lista:
                d_limpio = quitar_tildes(d['nombre'])
                if pais_buscar in d_limpio:
                    coincidencias.append(d)
                    encontrado = True

            if len(coincidencias) > 1:
                print("(!) Se encontro más de una coincidencia:")
                mostrar_info(coincidencias)
            elif len(coincidencias) == 1:
                print(">>Se encontró 1 coincidencia:")
                mostrar_info(coincidencias)

        if not encontrado:
            print("(!) No se encontró el país en la lista.")

crear_archivo(paises)

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
            actualizar_datos(paises)
        case "3":
            busqueda(paises)
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
