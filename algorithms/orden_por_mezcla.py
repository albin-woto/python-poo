import random

def orden_mezcla(lista):
    if len(lista) > 1:
        # Esta parte tiene crecimiento logaritmico
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print('Izquierda', izquierda, '*' * 5,'Derecha', derecha)

        # Llamada recursiva en cada mitad
        orden_mezcla(izquierda)
        orden_mezcla(derecha)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k]= derecha[j]
            j += 1
            k += 1

        print(f'Izquierda {izquierda}, Derecha {derecha}')
        print(lista)
        print('-' * 20)

    return lista



if __name__ == '__main__':
    tamano_lista = int(input('De que tamaño será la lista?'))

    lista = [ random.randint(0, 100) for i in range(tamano_lista) ]
    print('Lista', lista)
    print('-' * 20)

    lista_ordenada = orden_mezcla(lista)
    print('Lista ordenada', lista_ordenada)