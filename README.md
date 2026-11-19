# Gestión de datos de países en Python

**Trabajo Práctico Integrador - Programación I**
Tecnicatura Universitaria en Programación - UTN Facultad Regional Mendoza

Integrantes: Iglesias Luana, Garro Brisa.

-----------------------------------------------------------------------------------------
## Descripción del programa

Este programa permite gestionar información de países desde la consola. Cada país tiene cuatro datos: **nombre**, **población**, **superficie** (en km²) y **continente**.

Al iniciar, el programa lee los países desde un archivo CSV y los guarda en una **lista de diccionarios**. Cada país es un diccionario, por ejemplo:

`````````````````````````````````````````````````````````````````````````````````
{'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'}
`````````````````````````````````````````````````````````````````````````````````
Con un menú de opciones se pueden agregar y actualizar países, buscarlos, filtrarlos, ordenarlos y ver estadísticas. Los cambios se guardan en el archivo CSV.

-----------------------------------------------------------------------------------------
## Archivos del repositorio

- `gestion-de-datos-de-paises.py`: código fuente del programa.
- `dataset de paises.csv`: dataset base con los países.
- `README.md`: este archivo.
- Informe en PDF: documentación del trabajo (marco teórico, diagrama de flujo, capturas, conclusiones y bibliografía).

-----------------------------------------------------------------------------------------
## Instrucciones de uso

1. Tener instalado Python 3.10 o superior (el programa usa `match/case`).
2. Dejar el archivo `.py` y el archivo `.csv` en la misma carpeta.
3. Abrir una terminal en esa carpeta y ejecutar:

```````````````````````````````````````````````````````````````````````````````
gestion-de-datos-de-paises.py
```````````````````````````````````````````````````````````````````````````````

Si el archivo CSV no existe, el programa lo crea vacío con los encabezados `nombre,poblacion,superficie,continente`.

-----------------------------------------------------------------------------------------
## Menú de opciones

1. Agregar país
2. Actualizar Población y Superficie
3. Buscar país
4. Filtrar países
5. Ordenar países
6. Mostrar estadísticas
7. SALIR

Cada opción se explica más abajo, con su ejemplo de uso. Los ejemplos usan el dataset base del repositorio (Argentina, Japón, Brasil, Alemania, Australia y Argelia).

-----------------------------------------------------------------------------------------
## Funciones de ayuda

Estas funciones no son una opción del menú, pero las usan varias de las opciones. Cada una se encarga de una sola tarea.

**Manejo del archivo**
- `crear_archivo`: lee el CSV y carga los países en la lista. Convierte la población y la superficie a números enteros. Si encuentra un dato que no es un número, muestra un mensaje de error y el programa se detiene. Si el archivo no existe, lo crea.
- `actualizar_archivo`: guarda la lista completa en el CSV.

**Validaciones**
- `validar_lista`: avisa si no hay países cargados.
- `validar_nombre`: controla que el nombre tenga solo letras y que el país no esté repetido.
- `validar_entero`: controla que el dato sea un número entero mayor a 0.
- `validar_continente`: controla que el continente sea uno de los cinco válidos: América, África, Oceanía, Europa o Asia.

**Búsqueda y presentación**
- `quitar_tildes`: pasa el texto a minúsculas y sin tildes, para que "América", "america" y "AMERICA" se consideren iguales.
- `buscar_pais`: busca un país por su nombre exacto. Devuelve el país si lo encuentra y `False` si no.
- `mostrar_info`: imprime los países en pantalla, con todos sus datos.

**Ayuda para ordenar**
- `obtener_nombre`, `obtener_poblacion` y `obtener_superficie`: devuelven un solo dato de un país. `sorted()` no sabe por cuál de los cuatro datos del diccionario ordenar, y estas funciones se lo indican.

-----------------------------------------------------------------------------------------

## 1. Agregar país

**Qué hace:** agrega un país nuevo a la lista y lo guarda en el CSV. No se permiten campos vacíos.

**Cómo funciona:**
1. Pide el nombre y lo controla con `validar_nombre`. Si es inválido o ya existe, vuelve a pedirlo.
2. Pide la población y la superficie, y las controla con `validar_entero`.
3. Pide el continente y lo controla con `validar_continente`.
4. Cuando todos los datos son válidos, arma el diccionario del país y lo agrega a la lista.
5. Llama a `actualizar_archivo` para guardar el cambio en el CSV.

**Ejemplo.** El programa sigue pidiendo cada dato hasta que sea válido:

````````````````````````````````````````````````````````````````````````````````
>País: 1234
(!) Ingrese un nombre válido.
>País: Paises Bajos
>Población: 17938500
>Superficie en km²: abc
(!) Ingrese un número entero.
>Superficie en km²: 41543
>Continente: Europa
>> País agregado con éxito!
>>ARCHIVO ACTUALIZADO<<
````````````````````````````````````````````````````````````````````````````````

## 2. Actualizar Población y Superficie

**Qué hace:** cambia la población y la superficie de un país que ya está cargado.

**Cómo funciona:**
1. Controla que haya países cargados con `validar_lista`.
2. Pide el nombre del país y lo busca con `buscar_pais`.
3. Si lo encuentra, pide la nueva población y la nueva superficie, y las controla con `validar_entero`.
4. Cambia los datos del país en la lista y llama a `actualizar_archivo` para guardarlos.
5. Si no lo encuentra, avisa con un mensaje.

**Ejemplo:**

```
Ingrese el país del que desea actualizar sus datos: chile
(!) El país no se encuentra cargado en la lista.

Ingrese el país del que desea actualizar sus datos: argentina
>Población actualizada: abc
(!) Ingrese un número entero.
>Población actualizada: 46000000
>> Población actualizada con éxito!
>Superficie actualizada: 0
(!) El dato ingresado no puede ser menor a 1.
>Superficie actualizada: 2780400
>> Superficie actualizada con éxito!
>>ARCHIVO ACTUALIZADO<<
```

## 3. Buscar país

**Qué hace:** busca un país por su nombre. Puede ser una coincidencia exacta o parcial.

**Cómo funciona:**
1. Primero busca el nombre exacto con `buscar_pais`. Si lo encuentra, muestra ese único país.
2. Si no hay coincidencia exacta, recorre la lista y guarda los países que contienen el texto escrito dentro de su nombre.
3. Si hay uno solo, lo muestra. Si hay más de uno, los muestra todos. Si no hay ninguno, avisa.
4. Siempre compara sin tildes y sin importar mayúsculas, con `quitar_tildes`.

**Ejemplos:**

````````````````````````````````````````````````````````````````````````````````
Qué país está buscando? argentina
>>Se encontró 1 coincidencia:
País: Argentina | Población: 45376763 | Superficie: 2780400 | Continente: América
````````````````````````````````````````````````````````````````````````````````

````````````````````````````````````````````````````````````````````````````````
Qué país está buscando? arg
(!) Se encontró más de una coincidencia:
País: Argentina | Población: 45376763 | Superficie: 2780400 | Continente: América
País: Argelia | Población: 46810000 | Superficie: 2381740 | Continente: África
````````````````````````````````````````````````````````````````````````````````

````````````````````````````````````````````````````````````````````````````````
Qué país está buscando? china
(!) No se encontró el país en la lista.
````````````````````````````````````````````````````````````````````````````````

## 4. Filtrar países

**Qué hace:** muestra solo los países que cumplen una condición. Se puede filtrar por continente, por rango de población o por rango de superficie.

**Funciones que usa:**
- `filtrar_paises`: es la función de la opción. Muestra el submenú y hace el filtro elegido.
- `pedir_rango`: pide un valor mínimo y uno máximo. Sirve para población y para superficie, porque los dos piden lo mismo. Si el mínimo es mayor que el máximo, vuelve a pedirlos.
- `mostrar_resultado_filtro`: muestra los países encontrados, o avisa si no se encontró ninguno. Los tres filtros muestran el resultado igual, por eso está en una función aparte.

**Cómo funciona:**
1. Controla que haya países cargados con `validar_lista`.
2. Muestra el submenú: 1 continente, 2 rango de población, 3 rango de superficie.
3. Crea una lista vacía llamada `filtrados`.
4. Recorre todos los países y, si uno cumple la condición, lo agrega a `filtrados`.
5. Muestra el resultado con `mostrar_resultado_filtro`.

**Ejemplo de filtro por continente.** Acepta mayúsculas y palabras sin tilde:

````````````````````````````````````````````````````````````````````````````````
Ingrese la opción que desea realizar, 1 | 2 | 3: 1
>Continente: AMERICA

>> Se encontraron 2 país(es):
País: Argentina | Población: 45376763 | Superficie: 2780400 | Continente: América
País: Brasil | Población: 213993437 | Superficie: 8515767 | Continente: América
````````````````````````````````````````````````````````````````````````````````

**Ejemplo de filtro por rango de población.** Si el mínimo es mayor que el máximo, vuelve a pedir los datos:

````````````````````````````````````````````````````````````````````````````````
Ingrese la opción que desea realizar, 1 | 2 | 3: 2
>Población mínima: 50000000
>Población máxima: 20000000
(!) El mínimo no puede ser mayor que el máximo.
>Población mínima: 20000000
>Población máxima: 100000000

>> Se encontraron 4 país(es):
País: Argentina | Población: 45376763 | Superficie: 2780400 | Continente: América
País: Alemania | Población: 83149300 | Superficie: 357022 | Continente: Europa
País: Australia | Población: 27724744 | Superficie: 7741220 | Continente: Oceanía
País: Argelia | Población: 46810000 | Superficie: 2381740 | Continente: África
````````````````````````````````````````````````````````````````````````````````

## 5. Ordenar países

**Qué hace:** muestra los países ordenados por nombre, población o superficie, de forma ascendente o descendente.

**Funciones que usa:**
- `ordenar_paises`: es la función de la opción.
- `obtener_nombre`, `obtener_poblacion` y `obtener_superficie`: le indican a `sorted()` por cuál dato ordenar.

**Cómo funciona:**
1. Controla que haya países cargados con `validar_lista`.
2. Pide por qué dato ordenar: 1 nombre, 2 población, 3 superficie.
3. Pide el sentido: 1 ascendente (de menor a mayor) o 2 descendente (de mayor a menor).
4. Si eligió descendente, guarda `True` en una variable. Ese valor se usa en el parámetro `reverse` de `sorted()`.
5. Ordena con `sorted()`, usando como `key` la función que corresponde. La función se pasa sin paréntesis, porque `sorted()` es quien la llama con cada país.
6. Muestra la lista ordenada.

La lista original no se modifica: `sorted()` crea una copia ordenada.

**Ejemplo, ordenando por nombre de forma ascendente:**

````````````````````````````````````````````````````````````````````````````````
Ingrese la opción que desea realizar, 1 | 2 | 3: 1

>De qué forma desea ordenarlos?
1. Ascendente (de menor a mayor)
2. Descendente (de mayor a menor)
Ingrese la opción que desea realizar, 1 | 2: 1

>> Países ordenados:
País: Alemania | Población: 83149300 | Superficie: 357022 | Continente: Europa
País: Argelia | Población: 46810000 | Superficie: 2381740 | Continente: África
País: Argentina | Población: 45376763 | Superficie: 2780400 | Continente: América
País: Australia | Población: 27724744 | Superficie: 7741220 | Continente: Oceanía
País: Brasil | Población: 213993437 | Superficie: 8515767 | Continente: América
País: Japón | Población: 125800000 | Superficie: 377975 | Continente: Asia
````````````````````````````````````````````````````````````````````````````````

## 6. Mostrar estadísticas

**Qué hace:** calcula y muestra datos generales de todos los países:
- El país con mayor y menor población.
- El promedio de población y de superficie.
- La cantidad de países por continente.

**Cómo funciona:** un solo `for` recorre la lista una vez y va calculando todo.
1. Controla que haya países cargados con `validar_lista`.
2. Toma el primer país como punto de partida para el mayor y el menor.
3. En cada vuelta, compara la población del país con el mayor y el menor actuales, y los reemplaza si corresponde.
4. También suma la población y la superficie, para calcular los promedios al final.
5. Usa un diccionario como contador: la clave es el continente y el valor es cuántos países tiene. Si el continente ya está, suma 1; si es la primera vez que aparece, lo crea con valor 1.
6. Al terminar, divide cada suma por la cantidad de países y muestra los resultados.

**Ejemplo:**

````````````````````````````````````````````````````````````````````````````````
> País con mayor población: Brasil (213993437)
> País con menor población: Australia (27724744)
> Promedio de población: 90475707.33
> Promedio de superficie: 3692354.00 km²

>> Cantidad de países por continente:
- America: 2
- Asia: 1
- Europa: 1
- Oceania: 1
- Africa: 1
````````````````````````````````````````````````````````````````````````````````

## 7. SALIR

**Qué hace:** guarda los cambios en el archivo CSV y termina el programa.

````````````````````````````````````````````````````````````````````````````````
>>ARCHIVO ACTUALIZADO<<
Saliendo del programa...
````````````````````````````````````````````````````````````````````````````````

-----------------------------------------------------------------------------------------

## Validaciones y manejo de errores

- No se permiten campos vacíos al agregar un país, y tampoco países repetidos.
- La población y la superficie deben ser números enteros mayores a 0.
- El continente debe ser uno de los cinco válidos: América, África, Oceanía, Europa o Asia.
- Si se ingresa una opción que no existe en un menú, se muestra un aviso y se vuelve a empezar.
- Si una búsqueda o un filtro no encuentra resultados, se muestra un mensaje claro y el programa sigue funcionando.
- Los mensajes de error empiezan con `(!)` y los de éxito con `>>`, para distinguirlos fácilmente.

**Archivo CSV con un dato incorrecto.** Si en la columna de población o superficie hay algo que no es un número, el programa se detiene y avisa. Para esto se usa un bloque `try-except` al convertir los datos a número entero:

````````````````````````````````````````````````````````````````````````````````
(!!!) Hay un error en el archivo, compruebe que todos los datos sean correctos antes de continuar.
````````````````````````````````````````````````````````````````````````````````

## Participación de los integrantes

- **Iglesias Luana:** lectura del CSV, validaciones, y las opciones de agregar, actualizar y buscar países.
- **Garro Brisa:** las opciones de filtrar, ordenar y mostrar estadísticas.

Ambas participamos en las pruebas del programa y la documentación.