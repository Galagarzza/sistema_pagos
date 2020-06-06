#Jorge  

import os
import cotizacion
import factura
import comprobante
import tarjeta


while True:

    os.system('cls') 

    str = ("\n\t\t<<< Ferretería El Gran Almacén >>>")
    print (str.center(80))
  
    print ("\n\t\t\t TIENDA VIRTUAL")
    print (input("\n\t\t Precione  >Enter<  para entrar"))

    os.system('cls') 

    cotiza = cotizacion.Cotizar()
    cotiza.diccionario()
    cotiza.compra()

    os.system('cls')

    print ("\t\t< TIPO DE PAGO >")
    print ("\nPago en la tienda [1]  /  Pago Online  [0]") 

    tipo = int(input("\n=>  "))


    if tipo == 1:

        os.system('cls') 

        print ("\t\t< MÉTODO DE PAGO >")
        print ("\n1) Efectivo \n2) Cheque \n3) Tarjeta de crédito")
        
        metodo = int(input("\n=> "))


        if metodo == 1 or metodo == 2:

            factura.Facturacion()
            comprobante.recibo()
        
        elif metodo == 3:

            p1 = tarjeta.PaymentGateway()
            p1.segundaparte()
            p1.terceraparte()

            paga = int(input("\nPAGAR [1]  /  SALIR [0] \n=> "))

            if paga == 1:
                
                factura.Facturacion()
                comprobante.recibo()


    if tipo == 0:

        p1 = tarjeta.PaymentGateway()
        p1.segundaparte()
        p1.terceraparte()

        pagar = int(input("\nPAGAR [1]  /  SALIR [0] \n=> "))

        if pagar == 1:
            
            factura.Facturacion()
            comprobante.recibo()


    print (input("\t\t\n>>>¡VUELVA PRONTO!<<<"))
    
    
    






         

         
                    