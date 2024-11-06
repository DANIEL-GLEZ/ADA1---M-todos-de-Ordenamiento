import random

numeros = [random.randint(1, 100) for _ in range(10)]

print("Números antes de ordenar:")
print(numeros)

def metodo_seleccion(lista):
    n = len(lista)
    for i in range(n):
        minimo = i
        for j in range(i+1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        print(f"Intercambiando {lista[i]} con {lista[minimo]}")
        lista[i], lista[minimo] = lista[minimo], lista[i]
        print("Estado de la lista:", lista)
    return lista

numeros_ordenados = metodo_seleccion(numeros)

print("Números ordenados de menor a mayor:")
print(numeros_ordenados)
