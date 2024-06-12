import csv
lista=[]
diccionario={}

def imprimir_lista(dicc):
    for i in dicc:
        print("ID :",i["id"],"NOMBRE :",i["nombre"],"PRECIO :",i["precio"])
        
while True:
    print("")
    print("-.-.-.-.-.-M E N U -.-.-.-.--.-")
    print("")
    print("1.- agregar producto")
    print("2.- listar todos los productos")
    print("3.- eliminar un producto por id")
    print("4.- generar achivo CSV")
    print("5.- Cargar archivo csv")
    print("6.- estadísticas")
    print("0- salir")
    print("")
    op=int(input("ingrese una opcion :\n"))
    if op==1:
        print("")
        print("-----A G R E G A R  P R O D U C T O -------")
        print("")
        id=input("ingrese id :\n")
        nombre=input("ingrese su nombre:\n")
        precio=input("ingrese precio:\n")
        diccionario={"id":id,"nombre":nombre,"precio":precio}
        lista.append(diccionario)
        print("")
        print("Producto agregado correctamente..")
    elif op==2:
        print("")
        print("------P R O D U C T O S--------")
        print("")
        imprimir_lista(lista)
    elif op==3:
        print("")
        print("")
        id_busc=input("ingrese su id :\n")
        for i in lista:
            if id_busc==i["id"]:
                print("id encontrado")
                print("")
                lista.remove(i)
                print ("Producto eliminado")
               
                break

    elif op==4:
        print("")
        print("G E N E R A R  A R C H I V O")
    elif op==5:
        print("")
    elif op==6:
        print("")
    elif op==0:
        print("Saliendo......")
        print("Adios.")
        break
    else:
        print("")
        print("ingrese una opcion valida ")
    
