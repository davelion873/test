#CON EL SIMBOLO "#" AGREAMOS COMENTARIOS PARA
#DAR DETALLES DEL CODIGO

#Strings
print("Hello world")
print('Hello world')
print("""Hello world""")
print('''Hello world''')
print("123456 los numeros tambien pueden ser string")

#probando que al colocar type no se imprime por defecto,
#hay que introducir type dentro de print
type("Hello world")
print(type("Hello world"))

#el tipo de dato que imprime es INT
print(type(25))

#el tipo de ete dato es FLOAT
print(type(25.8))

#concatenando strings
print("Que" + "Pedo")




#NUMBERS
# 30 ES DE TIPO INTeger
# 30.5 ES DE TIPO FLOAT

#BOOLEAN (Define tipos de estado) 
True
False

# AGRUPACION DE DATOS "LIST, TUPLES, DICCIONARIOS OTRA LOSET

# List
# puede contener distintos tipos de datos ya que en python
# pueden convivir distintos tipos de datos
[12, 50, 36, 24]
["Juan", "Jose", "Maria"]
[10, "Hello", True, 15.6]
[]

print(type([12, True, "Hello World"]))

#TUPLE (Lista que no puede cambiar osea es inmutable)
(10, 20, 30, 50)
()

# DICCIONARIOS (Class DICT (agrupan datos que pertenecen a una misma entidad)
# deben separarse por comas ya que son distintos tipos de datos
{
    "Nombre" : "David",
    "Apodo" : "Dave Lion",
    "Nombramiento" : "Majestad"
}
# los diccionarios estan formados por "KEY" : "VALUE"


# Dato None
# es de type NoneType y sirve para indicar que lo que
# vamos autilizar no esta definido aun por un tipo de dato