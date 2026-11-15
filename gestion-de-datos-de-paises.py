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

#=======================================
# 4. FILTRAR PAISES
#=======================================

def mostrar_resultado_filtro(filtrados):
    # Si la lista quedó vacía, ningún país cumplió el filtro
    if len(filtrados)==0:
        print("(!)No se encontraron paises con ese filtro.")
    else:
        # len() cuenta cuántos países se encontraron
        print(f"Se encontraron {len(filtrados)} pais(es):")
        # mostrar_info (de la compañera) imprime cada país
        mostrar_info(filtrados)


def pedir_rango(nombre_dato):
    # El while True repite todo hasta que los datos sean válidos
    while True:
        # PASO 1: pedir el mínimo (.strip() borra espacios sobrantes)
        minimo= input(f"{nombre_dato} minima:").strip()
        # validar_entero (de la compañera) devuelve el número,
        # o False si no es entero o es menor a 1
        minimo = validar_entero(minimo)
        if minimo is False:      # dato inválido: vuelve al inicio del while
            continue

        # PASO 2: pedir el máximo, con la misma validación
        maximo= input(f"{nombre_dato} maxima: ").strip()
        maximo = validar_entero(maximo)
        if maximo is False:
            continue

        # PASO 3: comprobar que el rango tenga sentido
        if minimo > maximo:
            print("(!)El minimo no puede ser mayor que el maximo")
        else:
            # Si todo está bien, devuelve los dos valores y termina el while
            return minimo, maximo

def filtrar_paises(lista):
    # validar_lista avisa si no hay países cargados y no deja seguir
    if validar_lista(lista):
        print(f"\nFILTRAR PAISES  \n")
        print("1. Por continente")
        print("2. Por rango de poblacion")
        print("3. Por rango de superficie")

        opcion_filtro= input("Ingrese la opcion que desea realizar, 1 | 2 | 3:").strip()
        filtrados= []            # lista vacía: acá se van guardando los que cumplen
        match opcion_filtro:

            # ----- FILTRO 1: por continente -----
            case "1":
                # PASO 1: pedir el continente hasta que sea uno válido
                # (.title() lo pasa a formato "America", "Europa", etc.)
                while True:
                    continente= input("Continente: ").strip().title()
                    if validar_continente(continente):
                        break

                # PASO 2: recorrer todos los países y comparar el continente.
                # quitar_tildes evita problemas con "América" vs "america".
                for dicc in lista:
                    if quitar_tildes(dicc['continente']) == quitar_tildes(continente):
                        filtrados.append(dicc)     # si coincide, lo guarda

                # PASO 3: mostrar el resultado
                mostrar_resultado_filtro(filtrados)

            # ----- FILTRO 2: por rango de población -----
            case "2":
                # PASO 1: pedir mínimo y máximo (devuelve los dos valores)
                minimo, maximo = pedir_rango("Poblacion")

                # PASO 2: guardar los países cuya población está entre los dos números
                for dicc in lista:
                    if dicc['poblacion'] >= minimo and dicc ['poblacion'] <=maximo:
                        filtrados.append(dicc)

                # PASO 3: mostrar el resultado
                mostrar_resultado_filtro(filtrados)

            # ----- FILTRO 3: por rango de superficie -----
            # Igual que el anterior, pero con la clave 'superficie'
            case "3":
                minimo, maximo = pedir_rango("Superficie")

                for dicc in lista:
                    if dicc['superficie'] >= minimo and dicc['superficie'] <= maximo:
                        filtrados.append(dicc)
                mostrar_resultado_filtro(filtrados)

            # Cualquier otra cosa que escriba el usuario es una opción inválida
            case _:
                print ("(!)Debe ingresar una opcion dentro del rango.")

#=======================================
# 5. ORDENAR PAISES
#=======================================

def obtener_nombre(dicc):
    # quitar_tildes pasa a minúsculas y sin tildes, asi los paises que tengan se ordena donde corresponde y no al final
    return quitar_tildes(dicc['nombre'])

def obtener_poblacion(dicc):
    return dicc['poblacion']

def obtener_superficie(dicc):
    return dicc['superficie']              

def ordenar_paises(lista):
    if validar_lista(lista):
        # PASO 1: mostrar el menú de criterios
        print (f"\n ORDENAR PAISES \n")
        print("1. Por nombre")            
        print("2. Por poblacion")          
        print("3. Por superficie")           

        opcion_ordenar= input("Ingrese la opcion que desea realizar, 1 | 2 | 3:").strip()

        # PASO 2: validar. Si no es 1, 2 ni 3, avisa y sale (return)
        if opcion_ordenar not in ("1", "2", "3"):
            print ("(!)Debe ingresar una opcion dentro del rango.")
            return

        # PASO 3: preguntar el sentido del orden
        print ("\n1. Ascendente (de menor a mayor)")  
        print ("2. Descendente (de mayor a menor)")       
        opcion_sentido= input("Ingrese la opcion que desea realizar, 1 | 2:").strip()

        if opcion_sentido not in ("1", "2"):
            print ("(!)Debe ingresar una opcion dentro del rango.")
            return

        # PASO 4: guardar el sentido en una variable True/False.
        # Si eligió "2" (descendente), vale True; si eligió "1", vale False.
        # reverse=True hace que sorted() ordene de mayor a menor.
        descendente = (opcion_sentido == "2")

        # PASO 5: ordenar con sorted().
        # key = la función que indica por qué dato ordenar.
        # Va SIN paréntesis: sorted() la llama solo con cada país.
        match opcion_ordenar:
            case "1":
                ordenados = sorted(lista, key=obtener_nombre, reverse= descendente)
            case "2":
                ordenados = sorted(lista, key=obtener_poblacion, reverse= descendente)
            case "3":
                ordenados = sorted(lista, key=obtener_superficie, reverse= descendente)

        # PASO 6: mostrar la lista ya ordenada
        print ("Paises ordenados: ")        
        mostrar_info(ordenados)

#=======================================
# 6. ESTADÍSTICAS
#=======================================

def mostrar_estadisticas(lista):
    if validar_lista(lista):
        print(f"\n  ESTADÍSTICAS  \n")

        # PASO 1: variables de partida.
        # pais_mayor y pais_menor arrancan con el primer país de la lista
        # y se van reemplazando si aparece uno con más/menos población.
        pais_mayor = lista[0]
        pais_menor = lista[0]
        suma_poblacion = 0          # acumulador para el promedio de población
        suma_superficie = 0         # acumulador para el promedio de superficie
        # Diccionario contador: la clave es el continente y el valor es cuántos países tiene. Ejemplo: {"Asia": 3, "Europa": 5}
        cantidad_por_continente = {}

        # PASO 2: recorrer todos los países
        for dicc in lista:
            # Comparar la población de este país con el mayor y el menor actuales
            if dicc['poblacion'] > pais_mayor['poblacion']:
                pais_mayor = dicc
            if dicc['poblacion'] < pais_menor['poblacion']:
                pais_menor = dicc

            # Sumar los datos de este país a los acumuladores
            suma_poblacion += dicc['poblacion']
            suma_superficie += dicc['superficie']

            # Contar el país en su continente:
            # si el continente ya está en el diccionario, suma 1;
            # si es la primera vez que aparece, lo crea con valor 1
            continente = quitar_tildes(dicc['continente']).title()
            if continente in cantidad_por_continente:
                cantidad_por_continente[continente] += 1
            else:
                cantidad_por_continente[continente] = 1

        # PASO 3: calcular los promedios (suma total / cantidad de países)
        promedio_poblacion = suma_poblacion / len(lista)
        promedio_superficie = suma_superficie / len(lista)

        # PASO 4: mostrar los resultados
        # (:.2f muestra el número con 2 decimales)
        print(f"País con mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']})")
        print(f"País con menor población: {pais_menor['nombre']} ({pais_menor['poblacion']})")
        print(f"Promedio de población: {promedio_poblacion:.2f}")
        print(f"Promedio de superficie: {promedio_superficie:.2f} km²")
        print("Cantidad de países por continente:")
        # Recorre el diccionario contador: continente → cantidad
        for continente in cantidad_por_continente:
            print(f"  - {continente}: {cantidad_por_continente[continente]}")

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
            filtrar_paises(paises)
        case "5":
            ordenar_paises(paises)
        case "6":
            mostrar_estadisticas(paises)
        case "7":
            print("Saliendo del programa...")
        case _:
            print("(!) Debe ingresar una opción dentro del rango.")
