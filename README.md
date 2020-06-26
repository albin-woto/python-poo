## README que contiene la teoría del curso

### Tipos de datos abstractos
En python todo es un objeto y tiene un tipo
  * Representación de Datos y formas de interactuar con ellos
Formas de interactuar con un objeto:
  * Creación
  * Manipulación
  * Destrucción (En python el garbage collector elimina las instancias no utilizadas, pero se puede ser explícito con del)

Ventajas:
  * Decomposición en objetos más pequeños
  * Abstracción
  * Encapsulación de datos que no necesita conocer el usuario

#### Ejemplo básico de estructura de una clase

> self es la referencia a la instancia que estoy creando

```python
class <nombre_de_la_clase>(<super_clase>):
    def __init__(self, <params>):
        <expresion>

    def <nombre_del_metodo>(self, <params>):
        <expresion>
```

* Mientras que la clase es un molde, a los objetos creados se los conoce como instancias.
* Cuando se crea una instancia, se ejecuta el método \_\_init__, llamado constructor
* Todos los métodos de una clase reciben implícitamente como primer parámetro self

#### Instancias
Los atributos de clase nos permiten :
  * Representar datos
  * Procedimientos para interactuar con los mismos (métodos)
  * Mecanismos para esconder la representación interna

Se accede a los atributos con la notación de punto.  
`instancia.metodo()`  
Puede tener atributos privados. Por convención comienzan con _

#### Decomposición
* Partir un problema en problemas más pequeños.
* Las clases permiten crear mayores abstracciones en formas de componentes.
* Cada clase se encarga de una parte del problema y el programa se vuelve más fácil de mantener

#### Abstracción
* Enfocarnos en la información relevante
* Separar la información central de los detalles secundarios
* Podemos usar variables y métodos(privados o públicos)

#### Encapsulación
Es parte de la programación defensiva, para controlar cuándo y como se modifica una clase, se usan gracias a los decoradores.
* Permite agrupar datos y su comportamiento
* Controla el acceso a dichos datos
* Previene modificaciones no autorizadas
Sintaxis:
```python
class CasillaDeVotación:
    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    # Creo un getter a través del decorador @property
    @property
    def region(self):
        return self._region

    # Creo el setter a traves de otro decorator @nombre_propiedad.setter, puede contener logica como en este caso
    @region.setter
    def set_region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La region {region} no es valida en {self._pais}')

```

#### Herencia
* Permite modelar una jerarquía de clases
* Permite compartir un comportamiento común en la jerarquía
* Al padre se le conoce como superclase y al hijo como subclase

Sintaxis
```python
# Creo superclase
class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
#Creo subclase que hereda de superclase
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        # Importo las propiedades de la superclase
        super().__init__(lado, lado)
```

#### Polimorfismo
* Es la habilidad de tomar varias formas
* En python, nos permite cambiar el comportamiento de una superclase para adaptarlo a la subclase, por ej cambiando métodos

### Complejidad algorítmica
* Se analiza la complejidad temporal vs complejidad espacial
* A la complejidad temporal podemos definirla como T(n)  
Como lo mido? Mediante aproximaciones:
* Cronometrar el tiempo en el que corre un algoritmo(hay que tener en cuenta que esta limitada por el hardware que use)
* Contar los pasos con una medida abstracta de operación
* Contar los pasos conforme nos aproximamos al infinito

#### Notación asintótica (Big O notation)
* No importan variaciones pequeñas.
* El enfoque se centra en lo que pasa conforme el tamaño del problema se acerca al infinito
* Mejor de los casos, promedio, peor de los casos
* Big O
* Nada mas importa el término de mayor tamaño
###### Ley de la suma
```python
# Suponiendo una funcion lineal
def f(n):
    for i in range(n):
        print(i)
    for i in range(n):
        print(i)
```
`O(n) + O(n) = O(n + n) = O(2n) = O(n)`
```python
# Suponiendo una funcion lineal
def f(n):
    for i in range(n):
        print(i)
    for i in range(n * n):
        print(i)
```
`O(n) + O(n * n) = O(n + n^2) = O(n^2)`
###### Ley de la multiplicacion
```python
def f(n):
# Tengo un loop dentro de otro
    for i in range(n):
        print(i)
        for j in range(n):
            print(i, j)
```
`O(n) * O(n) = O(n * n) = O(n^2)`
###### Recursividad múltiple
```python
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```
Por cada llamada de fibonacci, retorno 2 llamadas y cada vez crece mas
`O(2^n)`

#### Orden Big O notation
* O(1) Constante
* O(log(log(n))) SubLogarítmica
* O(log(n)) Logarítmica
* O(n) Lineal
* O(n log(n)) Logarítmica lineal (puede llegar a servir, pero una contante n no se puede evitar)
* O(n^2) Polinomial (puede servir si no es exesivamente grande, no recomendables)
* O(2^n) Exponencial
* O(n!) Factorial
* O(n^n) Potencial exponencial

### Algoritmos de búsqueda y ordenación

#### Búsqueda lineal
Busca en todos los elementos de manera secuencial
Tiene O(n), ya que en el peor de los casos demora n veces en llegar al valor buscado

#### Búsqueda binaria
* La lista debe estar ordenada. Si no lo está y sólo necesito buscar una vez conviene búsqueda lineal, si no es mejor ordenar y ejecutar la búsqueda binaria mas de una vez
* Divide and conquer
* El problema se divide en 2 en cada iteración
* ¿Cúal es el peor caso? O(log n)

#### Ordenamiento de burbuja (Bubble sort)
El ordenamiento de burbuja es un algoritmo que recorre repetidamente una lista que necesita ordenarse. Compara elementos adyacentes y los intercambia si estan en el orden incorrecto: Este procedimiento se repite hasta que no se requieren mas intercambios, lo que indica que la lista se encuentra ordenada.  
Luego de la primera ronda, el algoritmo nos asegura que el número más grande lo llevará al final(útil si busco un max).  
Tiene O(n^2) por lo que no es bueno para grandes listas.
