print("===========================")
print ("Conversor")
print("=========================== \n")

print("*Menu de Opciones*: \n")
print("Presiona 1 para convertir de numero a palabra. ")
print("Presiona 2 para convertir de palabra a numero. \n")

opcion = int(input("Cual es tu opcion deseada?: "))   

if opcion == 1:
    print("\n conversor de numero a palabra \n")

    opcion_uno = int(input("Cual es el numero que desea convertir a palabra?: "))

    if opcion_uno == 1:
        print("El numero es UNO")

    elif opcion_uno == 2:
        print("El numero es DOS")
    elif opcion_uno == 3:
        print("El numero es TRES")
    elif opcion_uno == 4:
        print("El numero es CUATRO")
    elif opcion_uno == 5:
        print("El numero es CINCO")
    else:
        print("El nunmero seleccionado no esta disponible ")   
            

elif opcion == 2:
    print("\n conversor de palabra a numero \n")

    opcion_dos  = input("Cual es la palabra que desea convertir a numero?: ")

    if opcion_dos == "uno":
        print("El numero es 1")

    elif opcion_dos == "dos":
        print("El numero es 2")

    elif opcion_dos == "tres":
        print("El numero es 3")

    elif opcion_dos == "cuatro":
        print("El numero es 4")

    elif opcion_dos == "cinco":
        print("El numero es 5")    
            
    else:
        print("El numero selccionado no esta disponible")

else:
    print("Opcion no Disponible.")   

print("Fin.")                 