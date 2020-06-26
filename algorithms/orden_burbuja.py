import random

def orden_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):

            if lista[j] > lista [j + 1]:
                lista[j], lista [j + 1] = lista [j + 1], lista[j]

    return lista


if __name__ == '__main__':
    tamano_lista = int(input('De qué tamaño será la lista? '))

    lista = [ random.randint(0, 100) for i in range(tamano_lista) ]
    print('Lista', lista)

    lista_ordenada = orden_burbuja(lista)
    print('Lista ordenada', lista_ordenada)