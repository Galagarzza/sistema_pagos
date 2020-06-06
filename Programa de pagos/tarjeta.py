#Marcos

import os

class PaymentGateway():


    def __init__(self):

        os.system('cls')

        print ("\t\t <<  PAGO CON TARJETA  >>")

        monto = float(input("\ningrese el monto a pagar: $"))
        
        while monto< 1 or monto> 150000:
             
             print("error: ingrese un valor entre 1 y 150000")
             monto = int(input("Ingrese el monto a pagar:")) 


    def segundaparte(self): 

        print("\n¿Qué tipo de transacción es?")
        print("\na) auth\nb) capture\nc) sale")
        
        tran = input("\ningresa la opcion:-")

        while tran != "a" and tran != "b" and tran != "c":
          print ("error:701,mensaje: Esta no es una transaccion permitida")
          
          tran = input("ingrese opcion:")

    
    def terceraparte(self):
        
        os.system('cls')

        print ("\t\t <<  PAGO CON TARJETA  >>")

        print ("\nElija tipo de tarjeta:") 

        tipo_tarjeta = (input("\na) Visa \nb) Master Card \nc) American Express \n=> "))


        if tipo_tarjeta == "a":
            tipo_tarjeta = "Visa"

        elif tipo_tarjeta == "b":
            tipo_tarjeta = "Master Card" 
        
        elif tipo_tarjeta == "c":
            tipo_tarjeta = "American Express"       
 

        tar = int(input("\nIngrese el número de la tarjeta: #"))

        os.system('cls')
        

        print ("\t\t<<  Tarjeta de Crédito  >>")

        print (
            "\n=> Transacción: 13",
            "\n=> Tarjeta", tipo_tarjeta,
            "\n=> Nº", tar,
            )
        
    
        
                
       

         
            
