#Edward

import os

class recibo():

    def __init__(self):

        os.system('cls')

        print("\n\t\t>>> Comprobante de Recibo <<<")
        print("\t\t  Ferreteria El Gran Almacén")
        print("\nNombre del Cliente: ")

        Cliente = input()

        print("El cliente es",Cliente)
        print("\nNúmero de telefono:")

        Telefono = input()

        print("Número Telefonico",Telefono)
        print("\nTipo de producto:")

        Producto = input()

        print("Descripción del producto:",Producto)

        print("\nCantidad de artículos")
        cantidad = int(input())
        print("\nTotal Pagado")
        precio = float(input())

  