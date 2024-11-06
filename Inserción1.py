import random

numeros = [random.randint(1, 100) for _ in range(6)]

print("Números antes de ordenar:")
print(numeros)

def metodo_insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        print(f"Clave actual: {clave}")
        while j >= 0 and clave < lista[j]:
            print(f"Moviendo {lista[j]} a la posición {j + 1}")
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
        print("Estado de la lista:", lista)
    return lista

numeros_ordenados = metodo_insercion(numeros)

print("Números ordenados de menor a mayor:")
print(numeros_ordenados)
