## README

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

#### Ordenamiento por inserción (Insertion sort)
El ordenamiento por inserción es uno de los algoritmos más comunes que estudian
los Científicos del Cómputo. Es intuitivo y fácil de implementar, pero es muy
ineficiente para listas de gran tamaño. Una de las características del ordenamiento por inserción es que ordena en “su
lugar.” Es decir, no requiere memoria adicional para realizar el ordenamiento
ya que simplemente modifican los valores en memoria.  
La definición es simple:

Una lista es dividida entre una sublista ordenada y otra sublista desordenada.
Al principio, la sublista ordenada contiene un solo elemento, por lo que por
definición se encuentra ordenada.

A continuación se evalua el primer elemento dentro la sublista desordenada para
que podamos insertarlo en el lugar correcto dentro de la lista ordenada.

La inserción se realiza al mover todos los elementos mayores al elemento que
se está evauluando un lugar a la derecha.

Continua el proceso hasta que la sublista desordenada quede vacia y, por lo
tanto, la lista se encontrará ordenada.
En el peor de los casos es O(n^2)

#### Ordenamiento por mezcla (Merge sort)
Es una mezcla de algoritmo de divide y conquista. Primero divide una lista en partes iguales hasta que quedan sublistas de 1 o 0 elementos. Luego las recombina en forma ordenada. Es un algoritmo de O(n log(n)).

### Ambientes virtuales
* Permite aislar el ambiente para poder instalar diversas veriones de paquetes
* A partir de python 3 se invluye en la librería estándar en el módulo venv
* Ningún profesional de python trabaja sin ellos

Para crearlo puedo usar venv o virtualenv, env es el nombre del entorno, generalmente se usa env, venv  
`python3.8 -m venv env`  
Para activar el ambiente en linux o unix  
`source env/bin/activate`  
Para activarlo en windows  
`source env/scripts/activate`  
Para desactivarlo  
`deactivate`

#### Pip
* Permite descargar paquetes de terceros para utilizar en nuestro programa
* Permite compartir nuestros paquetes con terceros
* Permite especificar la versión del paquete que necesitamos

Tener en cuenta que si instalo de forma directa sin ingresar a un ambiente virtual, instalará el paquete de forma global, así no puedo manejar más de una versión a la vez. Por lo que si quiero probar una versión en particular de un paquete en un proyecto, primero debo inicializar el ambiente y luego instalar el paquete con:  
`pip3 install bokeh`  
Si quiero ver que tengo instalado en el ambiente:  
`pip freeze`  
Cuando me pasan o descargo un proyecto, generalmente viene un archivo llamado requirements.txt con los paquetes que necesita. Los instalo de la siguiente  forma:  
`pip install -r requirements.txt`  
Puedo crear este archivo en mi proyecto, luego de instalar todos los paquetes necesarios, de la siguiente forma:  
`pip freeze > requirements.txt`  

### ¿Por qué graficar?
* Reconocimiento de patrones
* Predicción de una serie
* Simplifica una interpretación y las conclusiones acerca de los datos

> Tener cuidado de no ver patrones por todos lados, primero evaluar los números o funciones, ver si puede haber un posible patrón y allí buscarlo. No encasillarse en ver si hay un patrón si o si.

#### Graficado simple
Existen muchas librerías para esto como matplotlib, pylab, bokeh, etc. Depende el caso de uso es lo que voy a implementar.
* Bokeh permite construir graficas complejas de manera rápida y con comandos simples
* Permite exportar a varios formatos como html, notebooks, imágenes, etc.
* Bokeh se puede utilizar en el servidor con Flask Y Django

> Tener siempre en cuenta que la representación gráfica tenga significado y se pueda entender, no sirve hacer cualquier gráfica porque sí.


### Introducción a la optimización
* El concepto de optimizacion permite resolver muchos problemas de manera computacional
* Una función objetivo que debemos maximizar o minimizar
* Una serie de limitantes que debemos respetar
Por ejemplo en algoritmos de rutas más rápidas para ir de un punto a otro(waze)