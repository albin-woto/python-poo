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