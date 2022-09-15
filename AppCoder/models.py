from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=40) #nombre va a ser de tipo Charfield entonces para darle el tipo debemos ingresarle la libreria la cual seria model.Charfield se usa para definicir la longitud de cadenas cortas.
    camada = models.IntegerField() #camada es un tipo entero. Entonces seria model.intergerfield haciendo referencia a que camada va a ser de tipo entero.
                                   # Charfield es como se llama a un string dentro de una base de datos. La cual si os e se le tiene que dar la longitud maxima.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField() #emailfield es para que la base de datos valide si se trata de un correo electronico o no.Si el usuario ingresa algo sin el @ lo toma como erroneo y detiene la app.


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField() #Datefield es para darle a saber a la base de datos que lo que ingrese el usuario va a ser de tipo fecha.
    entregado = models.BooleanField() #Si es entregado va a ser True y si no es entregado va a ser False. Por eso es de tipo bool.

#Cada class es el nombre de una tabla y toddo lo de abajo son los campos que va a tener esa tabla en la base de datos.
