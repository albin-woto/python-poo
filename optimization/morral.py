'''
Debo tratar de llevar la mayor cantidad de dinero en una mochila
'''

def morral(tamano_morral, pesos, valores, n):
    # Print para ver como va variando el tamaño del morral al probar distintos valores
    print(tamano_morral)
    if n == 0 or tamano_morral == 0:
        return 0

    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
        morral(tamano_morral, pesos, valores, n - 1))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10 , 20 , 30]
    tamano_morral = 30
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print('Valor max en mochila:',resultado)