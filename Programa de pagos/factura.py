#Abdiel

import os

class Facturacion():

    def __init__(self):

        cod = 100
        num = 0
        doc = ('FA')

        while True:

            os.system('cls')

            print ('\n\t{}\n\t{}>>> FORMULARIO DE FACTURACIÓN <<<'.format(85*'=',28*' '))  

            
            cod += 1
            num += 1 
            
            day = int(input('\n\tDÍA: '))
            mont = int(input('\tMES (NÚMERO): '))
            year = int(input('\tAÑO: '))
            date = [str(day)+'/'+str(mont)+'/'+str(year)]

            
            print ('\n\t{}\n\t|\t DATOS DE LA COMPRA \t\t||\n\t{}'.format(42*'_', 60*'-'))
            
            
            emp = "El Gran Almacén"
            ruc = "45160001"
            phone = "251-3572"

            customer = str(input('\n\tNOMBRE DEL CLIENTE: '))
            
            #---------------------PRODUCTO----------------------------------------
            
            tipe = str(input('\n\t//  PRODUCTOS  //\n\tDESPCRIPCIÓN DE LA COMPRA (TIPO): '))
            price = float(input('\tCOSTE TOTAL: '))
            amount = int(input('\tARTÍCULOS COMPRADOS: '))
            
            s = price
            subtotal = round(s, 2)
            
            #---------------------DESCUENTO---------------------------------------

            if subtotal>=100 and subtotal<=200:
                desc = 0.10*subtotal
                round(desc, 2)
                total = subtotal-desc
                round(total, 2)
            
            elif subtotal>200 and subtotal<600:
                desc = 0.15*subtotal
                round(desc, 2)
                total = subtotal-desc
                round(total, 2)
            
            else:
                desc = 'NO APLICA'
                total = subtotal
                    
            os.system('cls')

            print ('\t{}\n\t{}>>> FACTURA <<<'.format(85*'=', 35*' '))
            print ('\t{}\n\n\tFERRETERÍA\n\tEL GRAN ALMACEN\n\t{}'.format(85*'_', 85*'-'))
            print ('\n\t FECHA: {} \tTIPO DE DOCUMENTO: {}  \tFACTURA N°{}  \tCÓDIGO: {}'.format(date[0:5], doc, num, cod))
            print ('\n\t{}\n\t|\t DATOS DEL CLIENTE \t\t||\n\t{}'.format(42*'_', 85*'-'))
            print ('\t CLIENTE:{}\t\t EMPRESA: {}\t\tTEL.: {}\n\t RUC: {}'.format(customer.upper(),emp.upper(), phone, ruc))
            print ('\n\t{}\n\t|\t DESCRIPCIÓN DEL PRODUCTO \t\t||\n\t{}'.format(50*'_', 85*'-'))
            print ('\tTIPO: {}\n\tPRECIO: B/.{}\n\tCANTIDAD: {}'.format(tipe, price, amount))
            print ('\n\tSUBTOTAL: B/.{}\n\tDESCUENTO: B/.{}\n\tTOTAL: B/.{}'.format(subtotal, desc, total))
            
            op = int(input('\n\t===>>> CREAR OTRA  [1]  /  REALIZAR COMPRA  [0] \n=> '))

            if op == 1:
                continue
            
            elif op == 2:
                break
                


