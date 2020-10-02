print("Sistema paracaulcular el promedio de un alumno.")

nombre = input("para comenzar , cual es tu nombre:?  ")

matematicas = float(input(nombre + "cual es tu calificacion en matematicas:? "))
quimica = float(input(nombre + "cual es tu calificacion en quimica:?  "))
biologia = float(input(nombre + "cual es tu calificacion en biologia:?  "))

promedio = (matematicas + quimica + biologia) / 3 
promedio = int(promedio)

if promedio >= 6:
    print(' felicidades ' + nombre + '"Aprobaste" con un promedio de: ' , promedio )

else:  
     print(nombre , "No has aprobado" )

 

print("fin")
    
