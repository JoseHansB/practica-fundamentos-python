nombre = input("introduce tu nombre: ")
print(f"Hola {nombre}")

#entero
edad = 30
# flotante  - decimal
altura = 1.74
#convertir flotante
edadString = str(edad)
print(edad + edad)
print(edadString + edadString)

print(type(edad))

tuEdad = input("introduce tu edad: ")
tuEdad = int(tuEdad)

#estructura de control if

if tuEdad >= 18 and tuEdad < 100:
    print ("Eres mayor de edad")
elif tuEdad >= 100:
    print("eres inmortal?")
elif tuEdad == 0:
    print("no existes")
else:
    print("eres menor de edad")


# for

for i in range (0, 10):
    print(i)

#switch no existe
