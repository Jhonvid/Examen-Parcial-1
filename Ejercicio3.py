import random
import time

lista = [random.randint(1, 1000) for _ in range(500)]
print("Lista de 500 números:")
print(lista)

numero_a_buscar = int(input("Ingrese el número que desea buscar: "))

def busqueda_lineal(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            return i
    return -1

def busqueda_binaria(lista, numero):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == numero:
            return medio
        elif lista[medio] < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

inicio_lineal = time.time()
resultado_lineal = busqueda_lineal(lista, numero_a_buscar)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal

lista.sort()

inicio_binaria = time.time()
resultado_binaria = busqueda_binaria(lista, numero_a_buscar)
fin_binaria = time.time()
tiempo_binaria = fin_binaria - inicio_binaria

print(f"\nResultado de la búsqueda lineal: {'Encontrado en índice ' + str(resultado_lineal) if resultado_lineal != -1 else 'No encontrado'}")
print(f"Tiempo de ejecución de la búsqueda lineal: {tiempo_lineal:.6f} segundos")

print(f"\nResultado de la búsqueda binaria: {'Encontrado en índice ' + str(resultado_binaria) if resultado_binaria != -1 else 'No encontrado'}")
print(f"Tiempo de ejecución de la búsqueda binaria: {tiempo_binaria:.6f} segundos")
