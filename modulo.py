'''Por consola se piden como máximo 5 números hasta que pulsas q
muestra la suma de los números introducidos.
algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos'''


def obtener_numero():
    while True:
        try:
            entrada = input("Introduce un número o presiona 'q' para salir: ")
            if entrada.lower() == 'q':
                return None
            numero = float(entrada)
            return numero
        except ValueError:
            print("Error: Ingresa un número válido.")


def sumar_numeros():
    suma = 0
    while True:
        numero = obtener_numero()
        if numero is None:
            break
        suma += numero
    return suma


if __name__ == "__main__":
    print("Introduce hasta 5 números para sumar. Presiona 'q' para salir.")

    try:
        resultado = sumar_numeros()
        print(f"La suma de los números introducidos es: {resultado}")
    except Exception as e:
        print(f"Error inesperado: {e}")


'''En consola se piden las unidades y el precio.
Estos datos permiten calcular el subtotal.
Si el día de hoy es anterior al 15 de cada mes, se aplica
un descuento del 5%
Muestra el resultado el total de la factura.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos'''
from datetime import datetime

def obtener_valor(mensaje):
    while True:
        try:
            entrada = input(mensaje)
            valor = float(entrada)
            return valor
        except ValueError:
            print("Error: Ingresa un valor numérico válido.")

def calcular_descuento(subtotal):
    hoy = datetime.now().day
    if hoy < 15:
        descuento = subtotal * 0.05
        return descuento
    else:
        return 0

def calcular_total(unidades, precio_unitario):
    subtotal = unidades * precio_unitario
    descuento = calcular_descuento(subtotal)
    total = subtotal - descuento
    return total

if __name__ == "__main__":
    try:
        unidades = obtener_valor("Ingresa la cantidad de unidades: ")
        precio_unitario = obtener_valor("Ingresa el precio unitario: ")

        total_factura = calcular_total(unidades, precio_unitario)

        print(f"\nSubtotal: ${unidades * precio_unitario}")
        print(f"Descuento: ${calcular_descuento(unidades * precio_unitario)}")
        print(f"Total: ${total_factura}")

    except Exception as e:
        print(f"Error inesperado: {e}")

'''Actividad 3
En consola pides número inicial.
En consola pides número final.
Muestra una lista con todos los números pares que hay entre 
estos dos números.

algoritmo funciona:5 puntos
algoritmo utiliza mejora en argumentos : 5 puntos
algoritmo controla errores y excepciones : 5 puntos
algoritmo aplica funciones anónimas o recursividad : 5 puntos
algoritmo resuelve una mejora de funcionalidad : 5 puntos'''
def obtener_numero(mensaje):
    while True:
        try:
            entrada = input(mensaje)
            numero = int(entrada)
            return numero
        except ValueError:
            print("Error: Ingresa un número entero válido.")

def obtener_numeros():
    numero_inicial = obtener_numero("Ingresa el número inicial: ")
    numero_final = obtener_numero("Ingresa el número final: ")
    return numero_inicial, numero_final

def listar_numeros_pares(inicial, final):
    numeros_pares = [num for num in range(inicial, final + 1) if num % 2 == 0]
    return numeros_pares

if __name__ == "__main__":
    try:
        inicial, final = obtener_numeros()

        if inicial > final:
            print("Error: El número inicial debe ser menor o igual al número final.")
        else:
            numeros_pares = listar_numeros_pares(inicial, final)

            if not numeros_pares:
                print(f"No hay números pares en el rango de {inicial} a {final}.")
            else:
                print(f"\nNúmeros pares entre {inicial} y {final}: {numeros_pares}")

    except Exception as e:
        print(f"Error inesperado: {e}")


