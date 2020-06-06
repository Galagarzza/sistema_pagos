#Lia

import os
import sys

class Cotizar():


    def __init__ (self):
      
        print ("\nNUESTROS PRODUCTOS")
        print ("\n1. Clavos: $10.25\n2. Cemento: $39.99\n3. Madera: $12.00\n4. Guantes de construcción: $20.99\n5. Sierra Eléctrica: $105.54")
    

    def diccionario (self):
        
        global productos   #Variable global para poder utilizarla en todo el programa  
        productos = {
            "clavos": 10.25,
            "cemento": 39.99,
            "madera": 12.00,
            "guantes de construccion": 20.99,
            "sierra eléctrica": 105.54           
        }
        return "_______________________________________"

    
    def compra (self):


        eleccion = []
        valores = []

        while True:

            op = int(input("\nElija un producto: "))

            eleccion.append(list(productos.items())[op-1])
            valores.append(list(productos.items())[op-1][1])

            salir = input("\nElegir otro producto [1]  /  Continuar[0]: ")
           
            if salir == "0":
                break

        os.system('cls')

        print ("\n\t\t>> Productos seleccionados <<")
        print ("\t\t    | CO  - Cotización |\n")

        for listado in eleccion:
            print (listado)


        subtotal = sum(valores)

        itbms = subtotal * 0.07

        total = subtotal + itbms


        print (
            "\nNº de articulos:", (len(eleccion)),  
            "\nSubtotal: {:.2f}".format(subtotal),
            "\nItbms: {:.2f}".format(itbms)
            )

        print ("\ntotal: {:.2f}".format(total))

        el = int(input("\nCOMPRAR [1]  /  IMPRIMIR COTIZACIÓN [0] \n => "))
 
        os.system('cls')


        if el == 0:

            if total >= 100 and total <= 199:

                des = total * 0.10
                totalOfficial = total - des 

                print ("* Si compra ahora, recibirá un descuento de 10% *")

                print (
                    "\nSu descuento: {:.2f}".format(des),
                    "\nNuevo Total: {:.2f}".format(totalOfficial)
                    )
                
                imprimir = int(input("\nCOMPRAR [1]  /  IMPRIMIR [0] \n=> "))

                if imprimir == 0:
                
                    os.system('cls')

                    print (input("¡Documento impreso!"))

                    sys.exit() 
                            

            elif total >= 200 and total <= 600:
                des = total * 0.15
                totalOfficial = total - des

                print ("* Si compra ahora, recibirá un descuento de 15% *")

                print (
                    "\nSu descuento: {:.2f}".format(des),
                    "\nNuevo Total: {:.2f}".format(totalOfficial)
                    )

                impr = int(input("\nCOMPRAR [1]  /  IMPRIMIR [0] \n=> "))

                if impr == 0:
                
                    os.system('cls')

                    print (input("¡Documento impreso!"))

                    sys.exit()                    
            
            elif total <= 99:
                
                    os.system('cls')

                    print (input("¡Documento impreso!"))
                    
                    sys.exit()

                    
        
productos = None






