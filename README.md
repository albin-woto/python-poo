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

