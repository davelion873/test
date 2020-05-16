# Definir tuple opcion 1
x = (1, 2, 3)
# Definir tuple opcion 2
y = tuple((1, 2, 3))
# Tuple con un solo valor forma correcta
z = (1,)
# Tuple con un solo valor forma INCORRECTA pues lo detecta como un solo elemento
a = (1)

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
print(a)
print(type(a))
print(dir(x))
