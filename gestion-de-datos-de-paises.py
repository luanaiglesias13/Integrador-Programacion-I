import csv

ARCHIVO = "dataset de paises.csv"
COLUMNAS = ['nombre', 'poblacion', 'superficie', 'continente']
paises = []

#============ CREAR ARCHIVO ============

def crear_archivo(lista):
    try: #Dentro de un try-except intentamos abrir el archivo para lectura
        with open(ARCHIVO, "r", encoding="utf-8", newline="") as archivo:
            lector = csv.DictReader(archivo)

            #Recorremos el archivo con un for

            for dicc in lector:
                try: #Intentamos convertir a entero las columnas de 'poblacion' y 'superficie'
                    dicc['poblacion'] = int(dicc['poblacion'])
                    dicc['superficie'] = int(dicc['superficie'])
                    lista.append(dicc) #Si no ocurrió ningún problema agregamos el diccionario a la lista vacía

                except ValueError: #Si hay un error al convertir a entero levantamos un error
                    raise ValueError("(!!!) Hay un error en el archivo, compruebe que todos los datos sean correctos antes de continuar.")
    
        return lista #Si no ocurrió ningun problema devolvemos la lista completa

    except FileNotFoundError: #Si no se encuenta la lista, la crea
        with open(ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)

            escritor.writeheader() #Escribimos los encabezados
        return lista #Y devolvemos la lista vacía

#============ ACTUALIZAR ARCHIVO ============

def actualizar_archivo(lista):
    try: #Abrimos el archivo en modo lectura
        with open(ARCHIVO, "w", encoding="utf-8", newline="") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)

            escritor.writeheader() #Escribimos el encabezado

            escritor.writerows(lista) #Y reescribimos el archivo dandole la lista como parámetro
        print(">>ARCHIVO ACTUALIZADO<<")

    except FileNotFoundError: #Si el archivo no existe
        print("ERROR: archivo no encontrado.")
    except Exception as e: #Si ocurrió algún error inesperado
        print(f"Ocurrió un error inesperado, ERROR: {e}")

#============ VALIDAR ESTADO DE LA LISTA ============

def validar_lista(lista):
    if len(lista) == 0: #Si la lista está vacía imprimimos un mensaje
        print("(!) La lista se encuentra vacía, cargue al menos 1 país para continuar.")
        return False
    return True

#============ QUITAR TILDES ============

def quitar_tildes(texto):
    texto = texto.lower() #Pasamos el texto a minúscula

    remplazos = (
      ("á", "a"),
      ("é", "e"),
      ("í", "i"),
      ("ó", "o"),
      ("ú", "u"),
  )
    for a, b in remplazos: #Remplazamos las vocales que tengan tildes en el texto
        texto = texto.replace(a, b)
    return texto #Y devolvemos el texto modificado

#============ BUSCAR PAÍS ============

def buscar_pais(pais, lista):
    pais = quitar_tildes(pais) #Le quitamos las tildes al país para que no hayan errores

    for dicc in lista: #Por cada diccionario de la lista le quitamos las tildes al nombre del país
        nombre_limpio = quitar_tildes(dicc['nombre'])

        if pais.lower() == nombre_limpio.lower():
            return dicc #Si los nombres coinciden devolvemos el diccionario completo
    return False

#============ VALIDAR NOMBRE ============

def validar_nombre(nombre, lista):
    if not nombre.replace(" ", "").isalpha(): #Si el nombre no se trata de solo letras imprimimos un mensaje
        print("(!) Ingrese un nombre válido.")
        return False
    elif buscar_pais(nombre, lista) is not False: #Si la funcion buscar país no devuelve Falso es porque el país ya se encuentra cargado
        print("(!) El país ya se encuentra cargado en la lista.")
        return False
    return True #Si ninguna condición se cumple devolvemos True

#============ VALIDAR NÚM ENTERO ============

def validar_entero(numero):
    try:
        numero = int(numero) #Intentamos convertir el número a entero

        if numero <= 0: #Si es menor o igual a 0 devolvemos Falso
            print("(!) El dato ingresado no puede ser menor a 1.")
            return False
        return numero #Si no devolvemos el número
    except ValueError: #Si ocurre un error devolvemos Falso
        print("(!) Ingrese un número entero.")
        return False

#============ VALIDAR CONTINENTE ============

def validar_continente(continente):
    continente = quitar_tildes(continente) #Le quitamos las tildes al continente ingresado

    if continente.lower() not in ("america", "africa", "oceania", "europa", "asia"): #Si el continente no es igual a ningúno de estos devuelve Falso
        print("(!) El continente ingresado no existe.")
        return False
    return True #Si no, devuelve Verdadero

#============ MOSTRAR INFO ============

def mostrar_info(lista):
    for diccionario in lista: #Por cada diccionario mostramos sus datos
        print(f"País: {diccionario['nombre']} | Población: {diccionario['poblacion']} | Superficie: {diccionario['superficie']} | Continente: {diccionario['continente']}")

#============ DEVOLVER INFO ESPECÍFICA ============

#Funciones que devuelven un valor específico

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
    while True: #Con un While True solicitaremos datos hasta que sean válidos
        pais = input(">País: ").strip().title()

        if validar_nombre(pais, lista): #Si la función validar_nombre devuelve True rompemos el bucle y pasamos al siguiente
            break

    #Lo mismo hacemos con el resto de datos

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

    #Una vez que todos los datos sean correctos le añadimos el diccionario a la lista

    lista.append({'nombre': pais, 'poblacion': poblacion, 'superficie': superficie, 'continente': continente})
    print(">> País agregado con éxito!")
    actualizar_archivo(lista) #Y actualizamos el archivo csv

#=======================================
# 2. ACTUALIZAR DATOS
#=======================================

def actualizar_datos(lista):
    if validar_lista(lista): #Si la lista tiene cargado al menos un dato podemos continuar
        print(f"\n      「    ACTUALIZAR DATOS    」\n")

        #Solicitamos y buscamos el país

        pais_actualizar = input("Ingrese el país del que desea actualizar sus datos: ").strip().title()

        dicc_actualizar = buscar_pais(pais_actualizar, lista)

        if dicc_actualizar is not False: #Si el valor devuelto no es Falso continuamos

            while True:

                #Solicitamos y validamos hasta que el dato sea correcto

                poblacion_nueva = input(">Población actualizada: ").strip()

                poblacion_nueva = validar_entero(poblacion_nueva)

                if poblacion_nueva is not False: #Si el valor no es falso actualizamos los datos y salimos del bucle
                    dicc_actualizar['poblacion'] = poblacion_nueva
                    print(">> Población actualizada con éxito!")
                    break

            while True: #Hacemos lo mosmo con la superficie
                superficie_actualizar = input(">Superficie actualizada: ").strip()

                superficie_actualizar = validar_entero(superficie_actualizar)

                if superficie_actualizar is not False:
                    dicc_actualizar['superficie'] = superficie_actualizar
                    print(">> Superficie actualizada con éxito!")
                    break
            actualizar_archivo(lista) #Actualizamos el archivo
        else:
            print("(!) El país no se encuentra cargado en la lista.") #Si el país ingresado no se encontró

#=======================================
# 3. BÚSQUEDA
#=======================================

def busqueda(lista):
    if validar_lista(lista): #Si la lista esta cargada
        print(f"\n      「    BÚSQUEDA DE PAÍSES    」\n")

        coincidencias = [] #Creamos una lista para guardar las coincidencias

        encontrado = False #Y una bandera para poder comparar

        #Solicitamos y buscamos el país

        pais_buscar = input("Qué país está buscando? ").strip().title()

        dicc_buscado = buscar_pais(pais_buscar, lista)

        if dicc_buscado is not False: #Si se encontró la coincidencia exacta se imprimen los datos
            print(">>Se encontró 1 coincidencia:")
            print(f"País: {dicc_buscado['nombre']} | Población: {dicc_buscado['poblacion']} | Superficie: {dicc_buscado['superficie']} | Continente: {dicc_buscado['continente']}")
            encontrado = True #Y cambiamos la bandera

        else: #Si la coincidencia no fue exacta
            pais_buscar = quitar_tildes(pais_buscar) #Le quitamos las tildes al país para que quede limpio
            
            for d in lista: #Recorremos los diccionario de la lista y le sacamos las tildes al dato que este en nombre
                d_limpio = quitar_tildes(d['nombre'])
                if pais_buscar in d_limpio: #Si el país que buscamos se encuentra dentro del valor de 'nombre'
                    coincidencias.append(d) #Agregamos una coincidencia a la lista
                    encontrado = True #Y cambiamos la bandera

            if len(coincidencias) > 1: #Si hay más de una coincidencia para la busqueda parcial
                print("(!) Se encontró más de una coincidencia:")
                mostrar_info(coincidencias)
            elif len(coincidencias) == 1: #Si solo se encontró una coincidencia
                print(">>Se encontró 1 coincidencia:")
                mostrar_info(coincidencias)

        if not encontrado: #Si la bandera quedó en False
            print("(!) No se encontró el país en la lista.")

#============ MOSTRAR RESULTADO DEL FILTRADO ============

def mostrar_resultado_filtro(filtrados):
    
    if len(filtrados)==0: #Si la lista que almacena los países filtrados esta vacía imprimimos un mensaje
        print("(!) No se encontraron países con ese filtro.")
    else:
        print(f"\n>> Se encontraron {len(filtrados)} país(es):") #Si no, mostramos la información de la lista
        mostrar_info(filtrados)

#============ PEDIR RANGO DE POBL. Y SUP. ============

def pedir_rango(nombre_dato):

    while True: #Solicitamos el mínimo y lo validamos
        minimo= input(f"{nombre_dato} mínima: ").strip()

        minimo = validar_entero(minimo)

        if minimo is False:
            continue

        maximo= input(f"{nombre_dato} máxima: ").strip() #Y hacemos lo mismo con el máximo

        maximo = validar_entero(maximo)

        if maximo is False:
            continue

        if minimo > maximo: #Si el mínimo es mayor al máximo imprimimos un error
            print("(!) El mínimo no puede ser mayor que el máximo.")
        else:
            return minimo, maximo #Si no, devolvemos los valores de cada uno

#=======================================
# 4. FILTRAR PAÍSES
#=======================================

def filtrar_paises(lista):

    if validar_lista(lista): #Si la lista tiene datos
        print(f"\n      「    FILTRAR PAÍSES    」\n")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")

        opcion_filtro= input("Ingrese la opción que desea realizar, 1 | 2 | 3: ").strip()
        filtrados= [] #Creamos la lista que vamos a usar paralos países filtrados
        match opcion_filtro:

            #----- FILTRO 1: por continente -----
            case "1":

                while True: #Solicitamos el continente y lo validamos
                    continente= input(">Continente: ").strip().title()
                    if validar_continente(continente):
                        break

                for dicc in lista: #Recorremos los diccionarios y comparamos
                    if quitar_tildes(dicc['continente']) == quitar_tildes(continente):
                        filtrados.append(dicc) #Si coinciden agregamos el diccionario a la lista
                mostrar_resultado_filtro(filtrados) #Y mostramos los datos

            #----- FILTRO 2: por rango de población -----
            case "2":

                minimo, maximo = pedir_rango(">Población") #Pedimos el rango para filtrar

                for dicc in lista: #Comparamos los valores
                    if dicc['poblacion'] >= minimo and dicc ['poblacion'] <=maximo:
                        filtrados.append(dicc) #Si coinciden los agregamos a la lista de filtrados
                mostrar_resultado_filtro(filtrados) #Mostramos datos

            #----- FILTRO 3: por rango de superficie -----
            case "3": #Hacemos lo mismo para la superficie
                minimo, maximo = pedir_rango(">Superficie")

                for dicc in lista:
                    if dicc['superficie'] >= minimo and dicc['superficie'] <= maximo:
                        filtrados.append(dicc)
                mostrar_resultado_filtro(filtrados)

            case _: #Si el usuario ingresa una opción fuera del rango
                print ("(!) Debe ingresar una opción dentro del rango.")

#=======================================
# 5. ORDENAR PAÍSES
#=======================================

def ordenar_paises(lista):
    if validar_lista(lista): #Si la lista tiene datos cargados
        print (f"\n      「    ORDENAR PAÍSES    」\n")
        print("1. Por nombre")            
        print("2. Por población")          
        print("3. Por superficie")

        #Solicitamos la opción           

        opcion_ordenar= input("Ingrese la opción que desea realizar, 1 | 2 | 3: ").strip()

        if opcion_ordenar not in ("1", "2", "3"): #Si la opción ingresada no se encuentra en el rango
            print ("(!) Debe ingresar una opción dentro del rango.")
            return

        print("\n>De qué forma desea ordenarlos?")
        print ("1. Ascendente (de menor a mayor)")  
        print ("2. Descendente (de mayor a menor)")  

        opcion_sentido= input("Ingrese la opción que desea realizar, 1 | 2: ").strip()

        if opcion_sentido not in ("1", "2"): #Validamos la segunda opción
            print ("(!) Debe ingresar una opción dentro del rango.")
            return

        #Guardamos el sentido en una variable True/False.
        #Si eligió "2" (descendente) vale True. Si eligió "1" (ascendente) vale False.
        #reverse=True hace que sorted() ordene de mayor a menor.

        descendente = (opcion_sentido == "2")

        #key = la función que indica por qué dato ordenar.
        #Va sin paréntesis: sorted() la llama solo con cada diccionario.

        match opcion_ordenar: #Asociamos la opción elegida con la operación a realizar
            case "1":
                ordenados = sorted(lista, key=obtener_nombre, reverse= descendente)
            case "2":
                ordenados = sorted(lista, key=obtener_poblacion, reverse= descendente)
            case "3":
                ordenados = sorted(lista, key=obtener_superficie, reverse= descendente)

        print ("\n>> Países ordenados: ")        
        mostrar_info(ordenados) #Mostramos la información de los países en orden

#=======================================
# 6. ESTADÍSTICAS
#=======================================

def mostrar_estadisticas(lista):
    if validar_lista(lista): #Si la lista está cargada
        print(f"\n      「    ESTADÍSTICAS    」\n")

        #Almacenamos el país con mayor y menor población para poder comparar

        pais_mayor = lista[0]
        pais_menor = lista[0]
        
        suma_poblacion = 0          #acumulador para el promedio de población
        suma_superficie = 0         #acumulador para el promedio de superficie

        #Diccionario contador: la clave es el continente y el valor es cuántos países tiene.
        cantidad_por_continente = {}

        for dicc in lista: #Recorremos la lista

            if dicc['poblacion'] > pais_mayor['poblacion']:
                pais_mayor = dicc #Si el valor de la población del país en el que estamos es mayor al establecido lo cambiamos

            if dicc['poblacion'] < pais_menor['poblacion']:
                pais_menor = dicc #Hacemos lo mismo para la población

            #Le agregamos los valores a los respectivos acumuladores

            suma_poblacion += dicc['poblacion'] 
            suma_superficie += dicc['superficie']

            #Si el continente ya está en el diccionario, suma 1;
            #Si es la primera vez que aparece, lo crea con valor 1
            continente = quitar_tildes(dicc['continente']).title()
            if continente in cantidad_por_continente:
                cantidad_por_continente[continente] += 1
            else:
                cantidad_por_continente[continente] = 1

        #Sacamos promedios

        promedio_poblacion = suma_poblacion / len(lista)
        promedio_superficie = suma_superficie / len(lista)

        #Mostramos datos

        print(f"> País con mayor población: {pais_mayor['nombre']} ({pais_mayor['poblacion']})")
        print(f"> País con menor población: {pais_menor['nombre']} ({pais_menor['poblacion']})")
        print(f"> Promedio de población: {promedio_poblacion:.2f}")
        print(f"> Promedio de superficie: {promedio_superficie:.2f} km²")
        print("\n>> Cantidad de países por continente:")

        #Con un for mostramos los paises por continente

        for continente in cantidad_por_continente:
            print(f"- {continente}: {cantidad_por_continente[continente]}")

#COMIENZA EL PROGRAMA
#=================================================================================

#Dentro de un try-except englobamos el menú

try:
    crear_archivo(paises) #Intentamos crear o cargar el archivo, si no salta ningún error el programa sigue
    opcion = "" #Inicializamos la opción vacía

    #Con un While repetimos el menú hasta que el usuario eliga salir de él

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
        #Solicitamos la opción y la asociamos con la operación a realizar

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

#Si al intentar crear el archivo salta ValueError imprimimos el error y el programa se corta hasta que el usuario lo solucione

except ValueError as error:
    print(error)