myStr = "Hello World"

# print(dir(myStr))

# Upper cambia todo a mayusculas
print(myStr.upper())

# Lower cambia todo a minusculas
print(myStr.lower())

# Primera letra en minuscula y luego mayuscula y minuscula sucesivamente
print(myStr.swapcase())

# Primera letra de cada string individual a mayuscula independiente
# de que el string contenga varias palabras
print(myStr.capitalize())

# Reemplazar partes del string
print(myStr.replace("Hello", "Bye"))

# Linea 11 Ejemplo metodos encadenados, metodo va detras de otro
# sustituye hello por bye y posteriormente convierte todo en mayusculas
print(myStr.replace("Hello","Bye").upper())

# Cuenta en myStr cuantas letras "o" existen
print(myStr.count("o"))

# Nos dice si el string inicia con una letra o cadena de letras con
# un resultado True or False
print(myStr.startswith("Hello"))

# Valida si myStr termina en ld
print(myStr.endswith("ld"))

# Divide un string en distintas palabras a partir de un caracter 
# en blanco pero tambien podemos dividirlo por "," o por un caracter
# definido previamente colocado entre parentesis. Una vez divididos
# forman parte de una lista y se muestran en corchetes
print(myStr.split())

# Indice y longitud de un string
cadena = "longitud"
print(len(cadena))
print(cadena.find("d"))

name = "David"
# Distintas formas de concatenar str
print("My name is " + name)
print(f"My name is {name}")
print("My name is {0}".format(name))


