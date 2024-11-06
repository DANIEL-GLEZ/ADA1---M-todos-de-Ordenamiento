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

N = int(input("Ingrese la cantidad de letras que desea ordenar: "))

letras = []
for _ in range(N):
    letra = input("Ingrese una letra: ")
    letras.append(letra)

print("Letras antes de ordenar:")
print(letras)

letras_ordenadas = metodo_seleccion(letras)

print("Letras ordenadas de la A a la Z:")
print(letras_ordenadas)
