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

N = int(input("Ingrese la cantidad de letras que desea ordenar: "))

letras = []
for _ in range(N):
    letra = input("Ingrese una letra: ")
    letras.append(letra)

print("Letras antes de ordenar:")
print(letras)

letras_ordenadas = metodo_insercion(letras)

print("Letras ordenadas de la A a la Z:")
print(letras_ordenadas)
