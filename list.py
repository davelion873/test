demo_list = [1, "Hello", 1.34, True, [1, 2, 3]]
colors = ["red", "green", "blue"]

numbers_list = list((1, 2, 3, 4))
#print(numbers_list)
#print(type(numbers_list))

r = range(1, 101)
s = list(range(1, 101))
t = [range(20, 30)]
#print(r)
#print(s)
#print(t)

#print(colors)
#print(type(colors))
#print(dir(colors))

fruits = ["orange", "apple", "watermelon", [1, 2, 3]]
# print(fruits)
# print(len(fruits))
# print(fruits[2])
# print("apple" in fruits)

colores_esp = ["rojo", "morado", "azul"]
#print(colores_esp)
#colores_esp[1] = "dorado"
#print(colores_esp)
colores_esp.append("verde")
#print(colores_esp)
# ESTO NO FUNCIONA CON APPEND colores_esp.append("violeta", "amarillo")
colores_esp.extend(["violeta", "amarillo"])
#print(colores_esp)

compras = ["papel", "aceite", "mayonesa"]
compras.insert(1, "arroz")
#print(compras)
#print(len(compras))
compras.insert(len(compras), "jabon")
#print(compras)

supermercado = ["papel", "aceite", "mayonesa", "cloro", "crema", "leche"]
#print(supermercado)
supermercado.pop(1)
#print(supermercado)
supermercado.remove("crema")
#print(supermercado)

insumos = ["papel", "aceite", "mayonesa", "cloro", "crema", "leche", "cloro"]
print(insumos)
insumos.sort()
print(insumos)
insumos.sort(reverse=True)
print(insumos)
print(insumos.index("mayonesa"))
print(insumos.count("cloro"))
print(insumos.index("cloro"))