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
...


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

def generar_valores (lista):
    """
    Genera una lista de números enteros al azar de 1, 3 y 5 dígitos.
    Recibe: lista (list) -> La lista original.
    Devuelve: list -> La nueva lista con los valores generados.
    """
    print("\n[Opción 1] Se seleccionó: Generar valores (Desarrollo pendiente por completar)")
    return lista

def mostrar_valores (lista, titulo):
    """
    Muestra los valores de la lista en un formato de tabla encolumnada.
    Recibe: 
        lista (list) -> La lista a mostrar.
        titulo (str) -> El título variable de la tabla, ya que cambiará según quién lo llame.    
    Devuelve:
        None: Esta función solo imprime en pantalla y no retorna ningún valor.
    """
    print(f"\n[Opción 2] Se seleccionó: Mostrar valores - {titulo} (Desarrollo pendiente por completar)")

def eliminar_repetidos (lista):
    """
    Elimina los números repetidos de la lista sin cambiar el orden original.
    Recibe: lista (list) -> La lista original con posibles valores repetidos.
    Devuelve: list -> La nueva lista sin valores repetidos, manteniendo el orden original.
    """
    print("\n[Opción 3] Se seleccionó: Eliminar repetidos (Desarrollo pendiente por completar)")
    return lista

def filtrar_valores (lista):
    """
    Filtra los números de la lista según diferentes criterios (mayores, menores, pares, impares o en rango).
    Recibe: lista (list) -> La lista original a filtrar.
    Devuelve: list -> La nueva lista con los valores que cumplen el criterio de filtrado seleccionado por el usuario.
    """
    print("\n[Opción 4] Se seleccionó: Filtrar valores (Desarrollo pendiente por completar)")

def desdoblar_lista (lista):
    """
    Desdobla la lista original en varias listas según diferentes criterios (por ejemplo, por cantidad de dígitos).
    Recibe: lista (list) -> La lista original a desdoblar.
    Devuelve: dict -> Un diccionario con las nuevas listas desdobladas, donde cada clave representa el criterio de desdoblamiento.
    """
    print("\n[Opción 5] Se seleccionó: Desdoblar lista (Desarrollo pendiente por completar)")

def valores_top_n (lista):
    """
    Muestra un ranking con los "N" valores más altos de la lista.
    Recibe: lista (list) -> La lista original de la cual se extraerán los valores más altos.
    Devuelve: list -> Una nueva lista con los "N" valores más altos, ordenados de mayor a menor.
    """
    print("\n[Opción 6] Se seleccionó: Valores Top N (Desarrollo pendiente por completar)")

def mostrar_max_min (lista):
    """
    Busca el máximo y el mínimo de la lista y los muestra destacados en la tabla.
    Recibe: lista (list) -> La lista original de la cual se buscarán el máximo y el mínimo.
    Devuelve:
      None: Esta función solo muestra los valores destacados en pantalla.
    """
    print("\n[Opción 7] Se seleccionó: Mostrar máximo y mínimo (Desarrollo pendiente por completar)")



#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    


    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        while True:
            opciones = 4
            print()
            print("---------------------------")
            print("MENÚ DEL PROGRAMA           ")
            print("---------------------------")
            print("[1] Opción 1")
            print("[2] Opción 2")
            print("[3] Opción 3")
            print("[4] Opción 4")
            print("---------------------------")
            print("[0] Salir del programa")
            print("---------------------------")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones + 1)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":   # Opción 1
            ...
        elif opcion == "2":   # Opción 2
            ...
        elif opcion == "3":   # Opción 3
            ...
        elif opcion == "4":   # Opción 4
            ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()