print("sistema para calcular el promedio de un estudiante.")

cedula = int(input("Ingrese su cedula de identidad:? "))
nombre = input(" Ingrese su nombre?: ")
apellido = input(" Ingrese su apellido?: ")


matematicas = int(input( nombre + " cual es tu calificacion en matematicas?: " ))
quimica = int(input(nombre + " cual es tu calificacion en quimica?: " ))
biologia = int(input(nombre + " cual es tu calificacion en biologia?: " ))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)


if promedio  >= 6:
    print(' felicidades ' + nombre , apellido , str(cedula) + '"Aprobaste" con un promedio de: ' , promedio)

else:
     print(nombre , apellido , "No has aprobado" )

 
#print(nombre , apellido , "No has aprobado")

print("fin")
