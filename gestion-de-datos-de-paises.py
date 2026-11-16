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
                try:
                    dicc['poblacion'] = int(dicc['poblacion'])
                    dicc['superficie'] = int(dicc['superficie'])
                    lista.append(dicc)

                except ValueError:
                    raise ValueError("(!!!) Hay un error en el archivo, compruebe que todos los datos sean correctos antes de continuar.")
    
        return lista

    except FileNotFoundError:
        with open(ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)

            escritor.writeheader()
        return lista

#============ ACTUALIZAR ARCHIVO ============

def actualizar_archivo(lista):
    try:
        with open(ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)

            escritor.writeheader()

            escritor.writerows(lista)
        print(">>ARCHIVO ACTUALIZADO<<")

    except FileNotFoundError:
        print("ERROR: archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error inesperado, ERROR: {e}")

#============ VALIDAR ESTADO DE LA LISTA ============

def validar_lista(lista):
    if len(lista) == 0:
        print("(!) La lista se encuentra vacía, cargue al menos 1 país para continuar.")
        return False
    return True

#============ QUITAR TILDES ============

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

#============ DEVOLVER INFO ESPECÍFICA ============

def obtener_nombre(dicc):
    return quitar_tildes(dicc['nombre'])

def obtener_poblacion(dicc):
    return dicc['poblacion']

def obtener_superficie(dicc):
    return dicc['superficie']              

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
        print(f"\n      「    BÚSQUEDA DE PAÍSES    」\n")

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
                print("(!) Se encontró más de una coincidencia:")
                mostrar_info(coincidencias)
            elif len(coincidencias) == 1:
                print(">>Se encontró 1 coincidencia:")
                mostrar_info(coincidencias)

        if not encontrado:
            print("(!) No se encontró el país en la lista.")

#============ MOSTRAR RESULTADO DEL FILTRADO ============

def mostrar_resultado_filtro(filtrados):
    
    if len(filtrados)==0:
        print("(!) No se encontraron países con ese filtro.")
    else:
        print(f"\n>> Se encontraron {len(filtrados)} país(es):")
        mostrar_info(filtrados)

#============ PEDIR RANGO DE POBL. Y SUP. ============

def pedir_rango(nombre_dato):

    while True:
        minimo= input(f"{nombre_dato} mínima: ").strip()

        minimo = validar_entero(minimo)

        if minimo is False:
            continue

        maximo= input(f"{nombre_dato} máxima: ").strip()

        maximo = validar_entero(maximo)

        if maximo is False:
            continue

        if minimo > maximo:
            print("(!) El mínimo no puede ser mayor que el máximo.")
        else:
            return minimo, maximo

#=======================================
# 4. FILTRAR PAÍSES
#=======================================

def filtrar_paises(lista):

    if validar_lista(lista):
        print(f"\n      「    FILTRAR PAÍSES    」\n")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")

        opcion_filtro= input("Ingrese la opción que desea realizar, 1 | 2 | 3: ").strip()
        filtrados= []

        match opcion_filtro:

            #----- FILTRO 1: por continente -----
            case "1":

                while True:
                    continente= input(">Continente: ").strip().title()
                    if validar_continente(continente):
                        break

                for dicc in lista:
                    if quitar_tildes(dicc['continente']) == quitar_tildes(continente):
                        filtrados.append(dicc)
                mostrar_resultado_filtro(filtrados)

            #----- FILTRO 2: por rango de población -----
            case "2":

                minimo, maximo = pedir_rango(">Población")

                for dicc in lista:
                    if dicc['poblacion'] >= minimo and dicc ['poblacion'] <=maximo:
                        filtrados.append(dicc)
                mostrar_resultado_filtro(filtrados)

            #----- FILTRO 3: por rango de superficie -----
            case "3":
                minimo, maximo = pedir_rango(">Superficie")

                for dicc in lista:
                    if dicc['superficie'] >= minimo and dicc['superficie'] <= maximo:
                        filtrados.append(dicc)
                mostrar_resultado_filtro(filtrados)

            case _:
                print ("(!) Debe ingresar una opción dentro del rango.")

#=======================================
# 5. ORDENAR PAÍSES
#=======================================

def ordenar_paises(lista):
    if validar_lista(lista):
        print (f"\n      「    ORDENAR PAÍSES    」\n")
        print("1. Por nombre")            
        print("2. Por población")          
        print("3. Por superficie")           

        opcion_ordenar= input("Ingrese la opción que desea realizar, 1 | 2 | 3: ").strip()

        if opcion_ordenar not in ("1", "2", "3"):
            print ("(!) Debe ingresar una opción dentro del rango.")
            return

        print("\n>De qué forma desea ordenarlos?")
        print ("1. Ascendente (de menor a mayor)")  
        print ("2. Descendente (de mayor a menor)")  

        opcion_sentido= input("Ingrese la opción que desea realizar, 1 | 2: ").strip()

        if opcion_sentido not in ("1", "2"):
            print ("(!) Debe ingresar una opción dentro del rango.")
            return

        #Guardamos el sentido en una variable True/False.
        #Si eligió "2" (descendente) vale True. Si eligió "1" (ascendente) vale False.
        #reverse=True hace que sorted() ordene de mayor a menor.

        descendente = (opcion_sentido == "2")

        #key = la función que indica por qué dato ordenar.
        #Va sin paréntesis: sorted() la llama solo con cada diccionario.

        match opcion_ordenar:
            case "1":
                ordenados = sorted(lista, key=obtener_nombre, reverse= descendente)
            case "2":
                ordenados = sorted(lista, key=obtener_poblacion, reverse= descendente)
            case "3":
                ordenados = sorted(lista, key=obtener_superficie, reverse= descendente)

        print ("\n>> Países ordenados: ")        
        mostrar_info(ordenados)

#=======================================
# 6. ESTADÍSTICAS
#=======================================

def mostrar_estadisticas(lista):
    if validar_lista(lista):
        print(f"\n      「    ESTADÍSTICAS    」\n")

        pais_mayor = lista[0]
        pais_menor = lista[0]
        
        suma_poblacion = 0          #acumulador para el promedio de población
        suma_superficie = 0         #acumulador para el promedio de superficie

        #Diccionario contador: la clave es el continente y el valor es cuántos países tiene.
        cantidad_por_continente = {}

        for dicc in lista:

            if dicc['poblacion'] > pais_mayor['poblacion']:
                pais_mayor = dicc

            if dicc['poblacion'] < pais_menor['poblacion']:
                pais_menor = dicc

            suma_poblacion += dicc['poblacion']
            suma_superficie += dicc['superficie']

            #Si el continente ya está en el diccionario, suma 1;
            #Si es la primera vez que aparece, lo crea con valor 1
            continente = quitar_tildes(dicc['continente']).title()
            if continente in cantidad_por_continente:
                cantidad_por_continente[continente] += 1
            else:
                cantidad_por_continente[continente] = 1

        promedio_poblacion = suma_poblacion / len(lista)
        promedio_superficie = suma_superficie / len(lista)

        print(f"> País con mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']})")
        print(f"> País con menor población: {pais_menor['nombre']} ({pais_menor['poblacion']})")
        print(f"> Promedio de población: {promedio_poblacion:.2f}")
        print(f"> Promedio de superficie: {promedio_superficie:.2f} km²")
        print("\n>> Cantidad de países por continente:")

        for continente in cantidad_por_continente:
            print(f"- {continente}: {cantidad_por_continente[continente]}")

#COMIENZA EL PROGRAMA
#=================================================================================

try:
    crear_archivo(paises)
    opcion = ""

    while opcion != "7":

        print(f"""
⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢⌢
﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉﹉
        MENÚ DE GESTIÓN DE DATOS DE PAÍSES
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
                filtrar_paises(paises)
            case "5":
                ordenar_paises(paises)
            case "6":
                mostrar_estadisticas(paises)
            case "7":
                actualizar_archivo(paises)
                print("Saliendo del programa...")
            case _:
                print("(!) Debe ingresar una opción dentro del rango.")

except ValueError as error:
    print(error)