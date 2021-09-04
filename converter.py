'''
Diseño Lógico
Proyecto 1
Codigo Hamming
Clase Converter
'''


# Clase con las funciones de Hamming
class Converter:

    def __init__(self):
        var = True

    def dec_to_bin(self, decimal):
        if decimal <= 0:
            return "0"
        binario = ""
        while decimal > 0:
            residuo = int(decimal % 2)
            decimal = int(decimal / 2)
            binario = str(residuo) + binario
        return binario
