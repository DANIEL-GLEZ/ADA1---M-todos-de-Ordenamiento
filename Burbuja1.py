import random

numeros = [random.randint(1, 100) for _ in range(6)]

print("Números antes de ordenar:")
print(numeros)

def metodo_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                print(f"Intercambiando {lista[j]} y {lista[j+1]}")
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print("Estado de la lista:", lista)
    return lista

numeros_ordenados = metodo_burbuja(numeros)

print("Números ordenados de menor a mayor:")
print(numeros_ordenados)

