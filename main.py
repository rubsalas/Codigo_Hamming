'''
Diseño Lógico
Proyecto 1
Codigo Hamming
Main
'''

from hamming import *
from converter import *
from nrzi import *


# Instacia de Converter
converter = Converter()

# Instancia de NRZI
nrzi = NRZI()


# Funcion para correr el programa
def run():

    # Opcion que escogra el usuario a partir del menu por mostrar
    opcion = 0

    while opcion != 2:

        # Instancia de Hamming
        hamming = Hamming()

        opcion = input("\nSeleccione una de las siguientes opciones: \n" +
                           "-----------------------------------------------\n" +
                           "| MENÚ                                        |\n" +
                           "| 1) Ingresar un numero                       |\n" +
                           "| 2) Salir                                    |\n" +
                           "-----------------------------------------------\nSu opcion es: ")

        # Si se escoge la opcion de "Ingresar un numero"
        if opcion == "1":

            octal_input = input("\nIngrese un numero en octal: \n")

            if len(octal_input) == 4 and is_octal(octal_input):

                ######## Fase de conversión del numero ########

                print("\n1) Tabla de conversiones:\n\n" +
                      "-------------------------\n" +
                      "| Conversion  |   Base  |\n" +
                      "-------------------------")

                dato_binario = converter.octal_to_binary(octal_input)
                converter.octal_to_decimal(octal_input)
                converter.octal_to_hexa(octal_input)

                print("-------------------------\n")
                ############ Fin de la fase #############


                ######## Fase de la gráfica NRZI ########
                print("2) Gráfica de codificación NRZI: \n")

                nrzi.graph(dato_binario)

                print("Se presenta en la ventana aparte.\n")
                #############Fin de la fase##############


                ###### Fase de codificación Hamming #####

                print("3) Aplicación de la codificación Hamming: \n")

                # Paridad por utilizar en Hamming, se dejara la impar asignada antes de que el usuario la escoja
                paridad = "1"

                # Flag para revisar la paridad
                is_paridad_correct = False

                # Para revisar que se ingrese una paridad aceptable
                while not is_paridad_correct:

                    # Se pide la paridad en un input con sus respectivas opciones
                    paridad = input("Para iniciar la codificación, indique el tipo de paridad que desea utilizar: \n" +
                                    "-----------------------------------------------\n" +
                                    "| Opciones:                                   |\n" +
                                    "| '0' Si desea utilizar paridad par           |\n" +
                                    "| '1' Si desea utilizar paridad impar         |\n" +
                                    "-----------------------------------------------\nSu opcion es: ")

                    # Verifica que la paridad sea "1" o "0"
                    if paridad == "1" or paridad == "0":
                        is_paridad_correct = True
                    else:
                        print("Paridad invalida, intentelo de nuevo")

                # Se llama la funcion de Hamming para codificar el numero binario
                Dato_Codificado = hamming.code(dato_binario, paridad)

                # Funcion para provocar el error en un bit del codigo de Hamming calculado
                Dato_modificado = cambiar_bit(Dato_Codificado)

                #print("Así queda el dato modificado: " + Dato_modificado)

                dato_decodificado = hamming.decode(Dato_modificado, paridad)

                print("Se decodifica el valor en binario inicial:", dato_decodificado)

            #############Fin de la fase##############

            else:
                print("El numero ingresado no es de 4 digitos, no está en base 8 o el valor ingresado es inválido. "
                      "Por favor ingrese el numero de nuevo.")

        # Si se escoge la opcion de "Salir"
        elif opcion == "2":
            print("Finalizado")
            break

        # Si la opcion escogida es invalida00
        else:
            print("Opción invalida, intentelo de nuevo")


# Revisa que el numero entrante sea octal
def is_octal(input):

    # Con el try intenta convertir el input en un int
    try:
        # Se verifica que sea int
        if isinstance(int(input), int):

            # Recorre cada valor del input
            for ch in input:
                # Convierte el valor actual del input a int y revisa que sea menor a 7
                if int(ch) > 7:
                    # Si es mayor, no es una opcion aceptable como numero octal
                    return False

            # Si todos son menores a 8, se acepta el input
            return True

        else:
            return False

    # El except agarra el ValueError si el input no es un int
    except ValueError:
        # No es una opcion aceptable como numero octal
        return False


# Funcion que recibe el dato ya codificado con Hamming y le permite al usuario modificar
# alguno de los bits del dato para luego retornar el dato ya modificado
def cambiar_bit(Dato_codificado):

    # Se inicia la posicion del primer bit en 1
    position_index = 1

    print("\n Posición | bit")

    # Se itera sobre el codigo
    for bit in Dato_codificado:
        print("    " + str(position_index) + "        " + bit)

        # Se inicia en la posicion 1
        position_index += 1

    # Flag para ver si la posicion es correcta
    is_position_correct = False

    # Se verifica que el input ingresado sea correcto
    while not is_position_correct:

        # Input
        posicion_input = input("\nDe acuerdo a la tabla anterior.\nIngrese la posicion del bit que desea modificar: \n")

        # Con el try intenta convertir el input en un int
        try:
            # Se verifica que sea int
            if isinstance(int(posicion_input), int) and 0 < int(posicion_input) <= len(Dato_codificado):

                # Se actualiza la posicion para poder encontrar el valor que es
                posicion = int(posicion_input) - 1

                cont = 0
                Dato_cambiado = ""
                while cont < len(Dato_codificado):
                    if cont == posicion:
                        if Dato_codificado[posicion] == '1':
                            Dato_cambiado = Dato_cambiado + "0"
                            cont += 1
                        else:
                            Dato_cambiado = Dato_cambiado + "1"
                            cont += 1
                    else:
                        Dato_cambiado = Dato_cambiado + Dato_codificado[cont]
                        cont += 1
                return Dato_cambiado

            else:

                is_position_correct = False
                print("Error, por favor intente de nuevo.")

        # El except agarra el ValueError si el input no es un int
        except ValueError:

            is_position_correct = False
            print("Error, por favor intente de nuevo.")



'''
Empieza el programa
'''
run()
