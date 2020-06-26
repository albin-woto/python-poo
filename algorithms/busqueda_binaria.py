import random

def busqueda_bin(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_bin(lista, medio + 1, final, objetivo)
    else:
        return busqueda_bin(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
    tamano_lista = int(input('De qué tamaño será la lista? '))
    objetivo = int(input('Cuál número quieres econtrar?'))

    # Ordeno la lista
    lista = sorted([ random.randint(0, 100) for i in range(tamano_lista) ])

    # Lista, indice donde empieza, indice donde termina
    encontrado = busqueda_bin(lista, 0, len(lista), objetivo)

    print('Lista', lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
