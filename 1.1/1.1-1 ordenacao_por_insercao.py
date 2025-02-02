def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

# Exemplo de uso
lista_desordenada = [31, 41, 59, 26, 41, 58]
print("Lista desordenada:", lista_desordenada)
lista_ordenada = insertion_sort(lista_desordenada)
print("Lista ordenada:", lista_ordenada)
