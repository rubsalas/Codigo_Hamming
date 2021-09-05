'''
Diseño Lógico
Proyecto 1
Codigo Hamming
Clase Converter
'''


# Clase con las funciones de Converter
class Converter:

    def __init__(self):
        var = True

    # Funcion principal que se encarga de realizar la conversión de cada una de las cifras en octal a binario
    def octal_to_binary(self, number):
        string = str(number)
        binario = ""

        for c in string:
            true_value = self.obtener_caracter_binario(int(c))
            binario = binario + true_value

        bina = binario + " |  Base 2 "
        print("|{:>23}|".format(bina))

        return binario

    # Funcion secundaria que recibe un valor de entrada y retorna su respectiva conversión a binario
    def obtener_caracter_binario(self, valor):

        valor = str(valor)
        equivalencias = {
            "0": "000",
            "1": "001",
            "2": "010",
            "3": "011",
            "4": "100",
            "5": "101",
            "6": "110",
            "7": "111",
        }
        if valor in equivalencias:
            return equivalencias[valor]
        else:
            return valor

    # Funcion principal que se encarga de realizar la conversión de cada una de las cifras en octal a decimal
    def octal_to_decimal(self, number):
        octal = str(number)
        decimal = 0
        posicion = 0
        octal = octal[::-1]

        for digito in octal:
            valor_entero = int(digito)
            numero_elevado = int(8 ** posicion)
            equivalencia = int(numero_elevado * valor_entero)
            decimal += equivalencia
            posicion += 1

        deci = str(decimal) + " | Base 10 "
        print("|{:>23}|".format(deci))

    # Funcion principal que se encarga de realizar la conversión de cada una de las cifras en octal a hexadecima
    def octal_to_hexa(self, number):
        octal = str(number)
        decimal = 0
        posicion = 0
        octal = octal[::-1]

        for digito in octal:
            valor_entero = int(digito)
            numero_elevado = int(8 ** posicion)
            equivalencia = int(numero_elevado * valor_entero)
            decimal += equivalencia
            posicion += 1

        hexadecimal = ""

        while decimal > 0:
            residuo = decimal % 16
            true_value = self.obtener_caracter_hexadecimal(residuo)
            hexadecimal = true_value + hexadecimal
            decimal = int(decimal / 16)

        hexa = hexadecimal + " | Base 16 "

        print("|{:>23}|".format(hexa))

    # Funcion secundaria que recibe un valor de entrada y retorna su respectiva conversión a hexadecimal
    def obtener_caracter_hexadecimal(self, valor):
        valor = str(valor)
        equivalencias = {
            "10": "A",
            "11": "B",
            "12": "C",
            "13": "D",
            "14": "E",
            "15": "F",
        }

        if valor in equivalencias:
            return equivalencias[valor]
        else:
            return valor




















    def dec_to_bin(self, decimal):
        if decimal <= 0:
            return "0"
        binario = ""
        while decimal > 0:
            residuo = int(decimal % 2)
            decimal = int(decimal / 2)
            binario = str(residuo) + binario
        return binario
