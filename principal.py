"""
-----------------------------------------------------------------------------------------------
Título: TP N° 1 - Entrega1.py

Fecha: Mayo 2026 

Autor: 
Lázaro Martina - Legajo: 1238503
Mastronardi Milena - Legajo: 1233930
Lacava Giuliana - Legajo: 1239334
Cebreiros Juana - Legajo: 1238673
Bianciotto Sofía - Legajo: 1241171

Descripción:
Este programa permite cargar y trabajar con una lista de números enteros.
A través de un menú de opciones, el usuario puede:
   1. Generar números al azar de 1, 3 y 5 dígitos.
   2. Mostrar los datos en una tabla ordenada de 10 columnas.
   3. Eliminar los números repetidos sin cambiar el orden original.
   4. Filtrar los números (mayores, menores, pares, impares o en rango).
   5. Desdoblar la lista en varias listas según diferentes criterios.
   6. Ver un ranking con los "N" valores más altos.
   7. Buscar el máximo y el mínimo y mostrarlos destacados en la tabla.

 Todo el código está hecho usando funciones separadas y respetando las
 reglas de la cátedra (sin usar funciones automáticas como max, min o sort).

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------
import random
import time

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def pedir_entero (mensaje):
    """
    Solicita un número entero al usuario por teclado y lo valida.
    Asegura que la entrada esté compuesta únicamente por dígitos utilizando 
    el método .isdigit(), repitiendo el pedido en caso de error.
    Recibe:
        mensaje (str): El texto explicativo que se le muestra al usuario para pedir el dato.   
    Devuelve:
        int: El número entero ingresado por el usuario, una vez comprobado que es válido.
    """
    while True:
        cadena = input(mensaje)
        if cadena.isdigit():
            return int(cadena)
        else:
            print("Error: Debe ingresar un número entero válido (solo digitos). Intente nuevamente.")

def generar_valores(listas_datos):
   """
    Genera una lista de números enteros al azar de 1, 3 y 5 dígitos.
    Recibe: lista (list) -> La lista original.
    Devuelve: list -> La nueva lista con los valores generados.
    """
   cantidad = pedir_entero("Ingrese la cantidad de valores que desea generar: ")
   
   while cantidad < 2:
       print("Error: La cantidad debe ser al menos 2. Intente nuevamente.")
       cantidad = pedir_entero("Ingrese la cantidad de valores que desea generar: ")
       
   lista = []
   for i in range (0 , cantidad):
        opcion = random.randint(1 , 3)
        
        if opcion == 1:
            elemento = (random.randint(0,9))
        elif opcion == 2:
            elemento = (random.randint(100 , 999))   
        else:
            elemento = (random.randint(10000 , 99999))   
        lista.append(elemento)  
   return lista
   
def mostrar_valores (listas_datos, titulo):
    """
    Muestra los valores de la lista en un formato de tabla encolumnada.
    Recibe: 
        lista (list) -> La lista a mostrar.
        titulo (str) -> El título variable de la tabla, ya que cambiará según quién lo llame.    
    Devuelve:
        None: Esta función solo imprime en pantalla y no retorna ningún valor.
    """
    if len(listas_datos) == 0:
        print("No hay valores generados.")
        return
    
    asteriscos = "*" * 90
    print(asteriscos)
    print(titulo)
    print(asteriscos)
    
    letras_columnas = ("A".center(9) + "B".center(9) + "C".center(9) + "D".center(9) + "E".center(9) + "F".center(9) + "G".center(9) + "H".center(9) + "I".center(9) + "J".center(9))
    print(letras_columnas)

    separador = (("=" * 7).center(9)) * 10
    print(separador)
    print() # Salto de línea para separar el encabezado de la tabla del resto de los datos

    fila_actual = ""
    contador_columna = 0
    for i in range (len(listas_datos)):
        fila_actual += str(listas_datos[i]).center(9)
        contador_columna += 1
        if contador_columna == 10:
            print(fila_actual)
            print() # Salto de línea para separar cada fila de la tabla
            fila_actual = ""
            contador_columna = 0
    if contador_columna > 0:
        print(fila_actual)
        print() # Salto de línea para separar la última fila de la tabla del mensaje final
    
    fecha_hora = time.strftime("FIN DEL LISTADO ( %d-%m-%Y %H:%M:%S)")
    total_caracteres_fecha_hora = len(fecha_hora)
    resto_de_caracteres = 90 - total_caracteres_fecha_hora

    print(fecha_hora + resto_de_caracteres * "*") 

def eliminar_repetidos (listas_datos):
     """
    Elimina los números repetidos de la lista sin cambiar el orden original.
    Recibe: lista (list) -> La lista original con posibles valores repetidos.
    Devuelve: list -> La nueva lista sin valores repetidos, manteniendo el orden original.
    """
     copiaListaConRepetidos = listas_datos[:]
     listaSinRepetidos = []
     for elemento in copiaListaConRepetidos:
        if elemento not in listaSinRepetidos:
            listaSinRepetidos.append(elemento)

     elementosEliminados = len(copiaListaConRepetidos) - len(listaSinRepetidos)
     print(f"\n[Opción 3] Se seleccionó: Eliminar repetidos. Se eliminaron {elementosEliminados} elementos repetidos.")       
     return listaSinRepetidos

def filtrar_valores (lista):
    """
    Filtra los números de la lista según diferentes criterios (mayores, menores, pares, impares o en rango).
    Recibe: lista (list) -> La lista original a filtrar.
    Devuelve: None
    """
    print("\n[Opción 4] Se seleccionó: Filtrar valores")
    
    lista_trabajo = lista[:]
    lista_filtrada = []
    
    criterio = input("\nIngrese el criterio de filtrado [M=Mayores que | E=Menores que | R=En rango | P=Pares | I=Impares]: ").upper()
    
    while criterio not in ("M", "E", "R", "P", "I"):
        criterio = input("\nERROR - Ingrese el criterio de filtrado [M=Mayores que | E=Menores que | R=En rango | P=Pares | I=Impares]: ").upper()
        
    if criterio == "M":
        
        umbral = pedir_entero("Ingrese el valor umbral: ")
        
        for numero in lista_trabajo:
            if numero > umbral:
                lista_filtrada.append(numero)
                
    elif criterio == "E":
        
        umbral = pedir_entero("Ingrese el valor umbral: ")
        
        for numero in lista_trabajo:
            if numero < umbral:
                lista_filtrada.append(numero)
                
    elif criterio == "R":
        
        limite_inferior = pedir_entero("Ingrese el limite inferior: ")
        limite_superior = pedir_entero("Ingrese el limite superior: ")
        
        while limite_inferior > limite_superior:
            print("Error: El limite inferior no puede ser mayor al limite superior.")
            limite_inferior = pedir_entero("Ingrese el limite inferior: ")
            limite_superior = pedir_entero("Ingrese el limite superior: ")
            
            for numero in lista_trabajo:
                if numero >= limite_inferior and numero <= limite_superior:
                    lista_filtrada.append(numero)
                    
    elif criterio == "P":
        for numero in lista_trabajo:
            if numero % 2 == 0:
                lista_filtrada.append(numero)
                
    else:
        for numero in lista_trabajo:
            if numero % 2 != 0:
                lista_filtrada.append(numero)
                
    mostrar_valores(lista_filtrada, "Valores del juego de datos (DATOS FILTRADOS)")
    
    return

def desdoblar_lista (lista):
    """
    Desdobla la lista original en varias listas según diferentes criterios (por ejemplo, por cantidad de dígitos).
    Recibe: lista (list) -> La lista original a desdoblar.
    Devuelve: None (Las listas resultantes se muestran en formato de tabla con la función mostrar_tabla)
    """
    print("\n[Opción 5] Se seleccionó: Desdoblar lista")

    lista_trabajo = lista.copy()
    base_titulo = "VALORES DEL JUEGO DE DATOS (DATOS DESDOBLADOS) -"

    criterio = input("\nIngrese el criterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]\t").upper()

    while (criterio != 'P') and (criterio != 'C') and (criterio != 'U'):
        criterio = input("\nERROR - Ingrese el criterio de desdoblamiento [P=Pares/Impares | C=Por cantidad de cifras | U=Por valor umbral]\t").upper()

    if criterio == 'P':
        pares = []
        impares = []

        for n in lista_trabajo:

            if n % 2 == 0:
                pares.append(n)
            
            else:
                impares.append(n)
        
        mostrar_valores(pares, f"{base_titulo} PARES")
        mostrar_valores(impares, f"{base_titulo} IMPARES")
    
    elif criterio == 'C':
        una_cifra = []
        tres_cifras = []
        cinco_cifras = []

        for i in range(len(lista_trabajo)):
            cifras = len(str(lista_trabajo[i]))

            if cifras == 1:
                una_cifra.append(lista_trabajo[i])

            elif cifras == 3:
                tres_cifras.append(lista_trabajo[i])

            elif cifras == 5:
                cinco_cifras.append(lista_trabajo[i])

        mostrar_valores(una_cifra, f"{base_titulo} UNA CIFRA")
        mostrar_valores(tres_cifras, f"{base_titulo} TRES CIFRAS")
        mostrar_valores(cinco_cifras, f"{base_titulo} CINCO CIFRAS")

    else:
        hasta_umbral = []
        encima_umbral = []

        u = pedir_entero("\n Ingrese el numero umbral: ")

        for n in lista_trabajo:
        
            if n <= u:
                hasta_umbral.append(n)
        
            else:
                encima_umbral.append(n)
        
        mostrar_valores(hasta_umbral, f"{base_titulo} HASTA {u}")
        mostrar_valores(encima_umbral, f"{base_titulo} ENCIMA DE {u}")
    return

def valores_top_n (lista):
    """
    Muestra un ranking con los "N" valores más altos de la lista.
    Recibe: lista (list) -> La lista original de la cual se extraerán los valores más altos.
    Devuelve: None (La lista generada top_n se muestra llamando a la funcion mostrar_valores)
    """
    print("\n[Opción 6] Se seleccionó: Valores Top N")

    lista_copia = lista.copy()
    lista_trabajo = []
    top_n = []

    for elemento in lista_copia:
        if elemento not in lista_trabajo:
            lista_trabajo.append(elemento)
    
    n = pedir_entero("\nIngrese la cantidad de valores mas altos de la lista que desea mostrar:\t")

    if n > len(lista_trabajo):
        print(f"ERROR - Se solicito mostrar {n} pero solo existen {len(lista_trabajo)} valores")
        n = len(lista_trabajo)

    for k in range(0,n):
        maximo = lista_trabajo[0]
        pos = 0

        for i, num in enumerate(lista_trabajo):

            if num > maximo:
                maximo = num
                pos = i

        top_n.append(maximo)
        del lista_trabajo[pos]
    
    print("\n"+ "*"*50)
    print(f"VALORES DEL JUEGO DE DATOS (DATOS TOP {n})")
    print("*"*50)

    for i, j in enumerate(top_n):
        print(f"{i+1}- {j}")
    return

def buscar_max_min (lista):
    """
    Busca el máximo y el mínimo de la lista y los muestra destacados en la tabla.
    Recibe: lista (list) -> La lista original de la cual se buscarán el máximo y el mínimo.
    Devuelve: None (Esta función solo muestra los valores destacados en pantalla.)
    """
    print("\n[Opción 7] Se seleccionó: Mostrar máximo y mínimo.")

    lista_trabajo = lista.copy()
    maximo = lista_trabajo[0]
    minimo = lista_trabajo[0]

    for elemento in lista_trabajo:
        
        if elemento >= maximo:
            maximo = elemento
        if elemento <= minimo:
            minimo = elemento
    
    for i,elemento in enumerate(lista_trabajo):
        if (elemento == maximo) and (elemento == minimo):
            lista_trabajo[i] = f"<{elemento}>"
        elif elemento == maximo:
            lista_trabajo[i] = f"[{elemento}]"
        elif elemento == minimo:
            lista_trabajo[i] = f"({elemento})"
        else:
            lista_trabajo[i] = (str(elemento))
    
    mostrar_valores(lista_trabajo, "VALORES DEL JUEGO DE DATOS (DATOS MÁXIMOS Y MÍNIMOS [máx] (mín) <máx/mín>)")
    
    return


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    listas_datos = [] # Lista principal donde se almacenarán los números enteros generados y manipulados a lo largo del programa.
    

    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True: #bucle general del programa, se repetirá hasta que el usuario elija salir (opción 0)
        while True: #bucle interno para validar la opción del menú, se repetirá hasta que el usuario ingrese una opción válida
            opciones = 7 # Cantidad de opciones del menú (sin contar la opción de salir)
            print()
            print("---------------------------")
            print("MENÚ DEL PROGRAMA           ")
            print("---------------------------")
            print("[1] Opción 1")
            print("[2] Opción 2")
            print("[3] Opción 3")
            print("[4] Opción 4")
            print("[5] Opción 5")
            print("[6] Opción 6")
            print("[7] Opción 7")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcion_numero = pedir_entero ("Ingrese el número de la opción que desea seleccionar: ")
            opcion = str(opcion_numero)
            if opcion in [str(i) for i in range(0, opciones + 1)]:  # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            print("Saliendo del programa.")
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys
        elif opcion == "1":   # Opción 1
            if listas_datos:  # Si la lista ya tiene datos, se le pregunta al usuario si desea reemplazarlos o mantenerlos
                print("Ya existen valores generados en la lista.")
                confirmacion = input("¿Desea reemplazar los valores existentes? (S/N): ").strip().upper()
                if confirmacion != "S":
                    print("Manteniendo los valores existentes. No se generarán nuevos valores.")
                    input("Presione ENTER para volver al menú.")
                else:
                    listas_datos = generar_valores (listas_datos)
                    print("generación de valores completada.")
            else:
                listas_datos = generar_valores (listas_datos)
                print("generación de valores completada.")
        elif opcion == "2":   # Opción 2
            if not listas_datos:  # Si la lista está vacía, no se puede mostrar nada
                print("La lista está vacía. No hay datos para mostrar. Debe generar valores primero (Opción 1).")
            else:
                mostrar_valores (listas_datos, "Lista Principal")
        elif opcion == "3":   # Opción 3
            if not listas_datos:  # Si la lista está vacía, no se puede eliminar nada
                print("La lista está vacía. No hay datos para eliminar. Debe generar valores primero (Opción 1).")
            else:
                listas_datos = eliminar_repetidos (listas_datos)
                mostrar_valores (listas_datos, "VALORES DEL JUEGO DE DATOS (DATOS SIN REPETIDOS)")
        elif opcion == "4":   # Opción 4
            if not listas_datos:  # Si la lista está vacía, no se pueden filtrar valores
                print("La lista está vacía. No hay datos para filtrar. Debe generar valores primero (Opción 1).")
            else:
                filtrar_valores (listas_datos) 
        elif opcion == "5":   # Opción 5
            if not listas_datos:  # Si la lista está vacía, no se puede desdoblar
                print("La lista está vacía. No hay datos para desdoblar. Debe generar valores primero (Opción 1).")
            else: 
                desdoblar_lista (listas_datos) 
        elif opcion == "6":   # Opción 6
            if not listas_datos:  # Si la lista está vacía, no se pueden mostrar los valores top N
                print("La lista está vacía. No hay datos para mostrar. Debe generar valores primero (Opción 1).")
            else:
                valores_top_n (listas_datos)
        elif opcion == "7":   # Opción 7
            if not listas_datos:  # Si la lista está vacía, no se pueden mostrar el máximo y mínimo
                print("La lista está vacía. No hay datos para mostrar. Debe generar valores primero (Opción 1).")
            else:
                buscar_max_min (listas_datos)
        input("\nPresione ENTER para volver al menú.")
        print("\n\n")

# Punto de entrada al programa
main()