age = input("Insert your age: ")
suma_edad = 5
new_age = int(age) + int(suma_edad)
felicitacion = "Si hoy tienes {} años, dentro de {} años tendras {}"
print("Tu edad en 5 años sera {}".format(new_age))
print(f"En 5 años tendras {new_age} años")
print(felicitacion.format(age, suma_edad, new_age))