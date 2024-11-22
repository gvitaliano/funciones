# Crear una funcion que calcule el promedio de N notas
def promedio_calificaciones():
    valores = []
    while True:
        try:
            valor = int(input("Calificación: "))
            if valor == 0:
                break
            valores.append(valor)
        except ValueError:
            print("Inserta un número.")
    print("Promedio: ", sum(valores)/len(valores))

promedio_calificaciones()


"""Crear una funcion que determine si un color es primario o no se debe imprimir por pantalla la leyenda
"el color X es primario o el color X no es primario#
"""

def es_color_primario(color):
    colores_primarios = ['rojo', 'amarillo', 'azul']  # Para el modelo aditivo (luz)
    
    # Convertimos el color a minúsculas para evitar problemas con mayúsculas
    if color.lower() in colores_primarios:
        print(f"El color {color} es primario.")
    else:
        print(f"El color {color} no es primario.")

color = input("Ingrese el nombre de un color: ")
es_color_primario(color)

#Crear una funcion que determine que un numero de una serie de N numeros es mayor
def numero_mayor():
    # Pedir al usuario la cantidad de números
    n = int(input("¿Cuántos números deseas ingresar? "))
    
    # Inicializamos una lista para almacenar los números
    numeros = []
    
    # Pedimos los números al usuario
    for i in range(n):
        num = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)
    
    # Encontramos el número mayor
    mayor = max(numeros)  # Alternativamente, podríamos hacer esto manualmente con un bucle
    
    # Imprimir el resultado
    print(f"El número mayor de la serie es: {mayor}")

numero_mayor()

#Crear una funcion que dibuje un rectangulon de X filas y X columnas determinadas por el usuario
def dibujar_rectangulon(filas, columnas):
    for i in range(filas):
        print('*' * columnas)

# Aca dimensionamos el rectángulo
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))

dibujar_rectangulon(filas, columnas)

# Crear una funcion que calcule el factorial de un numero positivo
def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1  # El factorial de 0 o 1 es 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = int(input("Ingrese un número positivo mayor a 0: "))
if numero >= 0:
    print(f"El factorial de {numero} es: {calcular_factorial(numero)}")
else:
    print("Ingrese un número positivo mayor a 0.")