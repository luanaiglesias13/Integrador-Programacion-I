# Integrador-Programacion-I
TPI Programación - Gestión de datos de Países

Bri te dejo una lista de las funciones que hay hechas en el código por si te sirve alguna. Agrega las que hagas así vemos si hay alguna que nos sirva en conjunto.

Funciones:
-Crear archivo
-Validar nombre
-Buscar país
-Validar número entero
-Validar continente
-Quitar tildes de palabras
-Actualizar archivo
-Mostrar info completa (osea todo lo que hay en el dicionario lo imprime pero más bonito)

Te dejo una explicacion de cada punto Lu, lo hago ahora poeque despues ni yo me entiendo. 

4. FILTRAR PAISES
---------------------------------------------------------
mostrar_resultado_filtro
Qué hace: muestra el resultado de cualquier filtro.
Recibe: la lista "filtrados" con los países que cumplieron.
Por qué existe: los 3 filtros (continente, población y
superficie) muestran el resultado igual, así no repetimos código.
---------------------------------------------------------
pedir_rango
Qué hace: pide un valor mínimo y uno máximo.
Recibe: el nombre del dato ("Poblacion" o "Superficie"), solo para mostrarlo en el mensaje.
Devuelve: los dos números juntos (minimo, maximo).
Por qué existe: población y superficie piden lo mismo,
entonces la usamos en los dos casos.
---------------------------------------------------------
filtrar_paises  (opción 4 del menú)
Qué hace: muestra solo los países que cumplen una condición.
Recibe: la lista de países.
Opciones: 1 continente, 2 rango de población, 3 rango de superficie.
Idea general: recorre la lista y guarda en "filtrados" solo
los diccionarios (países) que cumplen la condición.
---------------------------------------------------------

5. ORDENAR PAISES
---------------------------------------------------------
obtener_nombre / obtener_poblacion / obtener_superficie
Qué hacen: devuelven UN dato de un país (un diccionario).
Para qué sirven: sorted() no sabe por cuál de los 4 datos del
diccionario ordenar. Estas funciones se lo indican.
---------------------------------------------------------
ordenar_paises  (opción 5 del menú)
Qué hace: muestra los países ordenados por nombre, población
o superficie, de forma ascendente o descendente.
Importante: NO modifica la lista original; sorted() crea una
copia ordenada.
---------------------------------------------------------

6. ESTADÍSTICAS
---------------------------------------------------------
mostrar_estadisticas  (opción 6 del menú)
Qué hace: calcula y muestra datos generales de todos los países:
- país con mayor y menor población
- promedio de población y de superficie
- cantidad de países por continente
Idea general: un solo for recorre la lista una vez y va calculando todo a la vez.
---------------------------------------------------------

