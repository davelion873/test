# h = "texto 1"
# a = "texto 2"
# b = "texto 3"
# A = "texto 4"
# n = "texto 5"
# o = "texto 6"
# s = "texto 7"

# letra = input("Teclea una letra de la palabra: ")
# if letra == "h":
#     print(h)
# elif letra == "a":
#     print(a)
# elif letra == "b":
#     print(b)
# elif letra == "A":
#     print(A)
# elif letra == "n":
#     print(n)
# elif letra == "o":
#     print(o)
# elif letra == "s":
#     print(s)

nombre = input("Teclea tu nombre letra por letra (mariAná) y da enter entre cada letra: ")
while nombre != 'Gabriel':
    nombre = input()
    if nombre != 'Gabriel':
        print('Ingrese su nombre nuevamente: ')
        continue
    print('Su nombre es Gabriel')
print('Se ha salido del bucle')