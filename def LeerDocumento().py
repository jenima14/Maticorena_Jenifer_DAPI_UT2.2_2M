def LeerDocumento()
    '''Esta función leerá la información del fichero y la
    guardará en una variable tipo lista.

    Parámetros:

    Salida:
    tendremos una lista con los datos del fichero

    '''
lista = int(input("Escribe lo que necesitas de la lista"))
LeerDocumento = open("PAGADO.txt", "r")

with open(LeerDocumento, 'r') as file:
    lista = file.readlines()
    if len(lista)