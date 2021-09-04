'''
Diseño Lógico
Proyecto 1
Codigo Hamming
Clase Hamming
'''

from converter import *


# Clase con las funciones de Hamming
class Hamming:

    def __init__(self):

        # Instacia del Convertidor
        self.converter = Converter()


        # Informacion entrante del usuario en binario para codificar
        self.code_information = ""

        # Paridad por utilizar al codificar
        self.code_parity_type = -1

        # Cantidad de digitos de informacion por codificar
        self.code_n = -1

        # Cantidad de bits de paridad para codificar
        self.code_p = -1

        # Cantidad total de bits en la codificacion
        self.code_n_p = -1

        # Matriz con los calculos de paridad para la codificacion
        self.code_matrix = []

        # Codigo de Hamming saliente
        self.coded_information_output = ""


        # Codigo de Hamming entrante
        self.coded_information_input = ""

        # Paridad por utilizar al decodificar
        self.decode_parity_type = -1

        # Cantidad de digitos de informacion por decodificar
        self.decode_n = -1

        # Cantidad de bits de paridad para decodificar
        self.decode_p = -1

        # Cantidad total de bits en la decodificacion
        self.decode_n_p = -1

        # Matriz con los calculos de paridad para la decodificacion
        self.decode_matrix = []

        # Bit encontrado con un error en el codigo
        self.decode_bit_in_error = "-1"

        # Codigo de Hamming corregido
        self.coded_information_fixed = ""

        # Informacion saliente al usuario en binario ya decodificada
        self.decoded_information = ""


    ####################################################################################
    #                                                                                  #
    #                                     Coding                                       #
    #                                                                                  #
    ####################################################################################


    # Inicia el proceso de Codificacion de Hamming
    def code(self, information, parity_type):

        # 1.
        # Se obtienen y guardan los datos con la informacion por codificar, ademas
        # se guarda la preferencia de la paridad del codigo
        self.set_input(information, parity_type, "code")

        # 2.
        # Se calcula el tamano de la informacion (n), los bits de paridad necesarios (p) y
        # el tamano del codigo final (n + p)
        self.calculate_coding_initial_variables()

        # 3.
        # Se crea la tabla para mostrar el proceso de codificacion por Hamming
        # Se crea la fila de posiciones en binario (no sera mostrada), la fila de los
        # titulos de las paridades y datos, la fila con los datos de la informacion y
        # las filas correspondientes al calculo de todas las paridades
        self.create_table(self.code_information, self.code_n, self.code_p, self.code_n_p,
                          self.code_matrix, "code")

        # 4.
        # Se acomodan los valores de la informacion que se utilizaran en el calculo de los bits de paridad,
        # se genera el calculo dependiendo de la paridad escogida y se rellena la tabla con los valores
        # finales de cada bit de paridad.
        self.calculate_parities(self.code_parity_type, self.code_p, self.code_n_p, self.code_matrix, "code")

        # 5.
        # Se acomodan los valores finales obtenidos a traves de toda la tabla en la ultima fila,
        # para formar el codigo
        self.set_code()

        # Imprime la matriz completa actualizada
        self.print_table(self.code_matrix)

        # Retorna el codigo con la informacion codificada lista
        return self.coded_information_output




    ##########################################
    #                                        #
    #                Entrada                 #
    #                                        #
    ##########################################

    '''
    1. Obtencion de la entrada
        -> Se guarda la informacion por codificar
        -> Se guarda la opcion de paridad (par o impar) escogida
    '''
    def set_input(self, information, parity, type):

        if type == "code":

            # Guarda la informacion entrante del usuario por codificar
            self.code_information = information

            print("\nInformacion por codificar: " + self.code_information)

            # Guarda la paridad por utilizar al codificar
            self.code_parity_type = parity

            print("Tipo de paridad por utilizar: " + str(self.code_parity_type))

        elif type == "decode":

            # Guarda la informacion entrante del usuario por decodificar
            self.coded_information_input = information

            print("\nInformacion por decodificar: " + self.coded_information_input)

            # Guarda la paridad por utilizar al decodificar
            self.decode_parity_type = parity

            print("Tipo de paridad por utilizar: " + str(self.decode_parity_type))


    ##########################################
    #                                        #
    #          Variables Iniciales           #
    #                                        #
    ##########################################

    '''
    2.C. Calculo de Variables Iniciales para Codificar
        -> Se calcula n: la cantidad de digitos de informacion
        -> Se calcula p: la cantidad de bits de paridad necesarios en el codigo
        -> Se calcula n + p: la cantidad total de bits en el codigo al completar la codificacion
    '''
    def calculate_coding_initial_variables(self):

        # Guarda la cantidad de digitos de informacion (n)
        self.code_n = self.set_information_digits_quantity(self.code_information)

        # Imprime la cantidad de digitos de informacion por codificar
        print("n = " + str(self.code_n))

        # Define la cantidad de bits de paridad que necesitara (p)
        self.code_p = self.set_parity_bits_quantity(self.code_n)

        # Imprime la cantidad de bits de paridad
        print("p = " + str(self.code_p))

        # Define el total de digitos del codigo saliente
        self.code_n_p = self.set_total_quantity(self.code_n, self.code_p)

        print("H(" + str(self.code_n_p) + "," + str(self.code_n) + ")")

    # Obtiene el numero en binario como un string para obtener la cantidad de digitos que posee
    def set_information_digits_quantity(self, information):
        # Obtiene la cantidad de digitos de informacion
        return len(information)

    # Obtiene la cantidad de bits de paridad necesarios para codificar la informacion
    def set_parity_bits_quantity(self, n):
        # Cantidad de bits de paridad
        p_i = 0
        # Verifica que se cumpla la inecuacion para saber cuantos bits son necesarios
        while ((2 ** p_i) - 1) < n + p_i:
            # Se agrega un bit de paridad mas
            p_i += 1
        # Establece la cantidad fija de numeros de paridad
        return p_i

    # Obtiene el total de digitos del codigo
    def set_total_quantity(self, n, p):
        # Obtiene la cantidad total de digitos
        return n + p


    ##########################################
    #                                        #
    #           Creacion de Tabla            #
    #                                        #
    ##########################################

    '''
    3. Creacion y Armado de la Tabla
        -> Se crean los numeros de las posiciones en binario
        -> Se crea la fila de los titulos de las paridades, datos y calculo de errores en la decodificacion
        -> Se agregan los valores de la informacion en su respectiva columna, para la decodificacion
           se agrega todo el codigo por decodificar
        -> Se crean las filas correspondientes al calculo de todas las paridades
    '''
    def create_table(self, information, n, p, n_p, matrix, type):

        # Configura la matriz por utilizar para hacer el algoritmo
        # Matriz necesitara:
        # - Columnas: n + p + 1
        # - Filas: 2 + p

        # Agrega una fila de referencia con las posiciones en binario de la tabla
        matrix.append(self.get_binary_position(n_p, type))

        # Agrega la primera fila a la matriz:
        # La lista del orden de los digitos existentes
        matrix.append(self.get_titles(n_p, type))

        # Agrega la segunda fila con los datos de informacion en su respectiva posicion
        matrix.append(self.get_information_data(matrix[1], information, type))

        # Agrega las filas restantes para calcular la paridad y el resultado
        matrix = self.set_parity_rows(n, p, n_p, matrix, type)

        if type == "code":
            self.code_matrix = matrix
        elif type == "decode":
            self.decode_matrix = matrix
        else:
            print("create_table(self, information, n, p, n_p, matrix, type): Error")

    # Crea la fila de referencia con las posiciones en binario
    def get_binary_position(self, n_p, type):

        # Lista con las posiciones
        binary_positions_list = [" "]

        # Agregara el titulo por cada bit que habra en el codigo
        for i in range(1, n_p + 1):
            # Convierte el indice a binario en string
            bin = self.complete_dec_to_bin(i, n_p)

            # Agrega el valor en binario de la posicion
            binary_positions_list.append(bin)

        # Si se esta decodificando se agregan espacios para completar la matriz
        if type == "decode":
            binary_positions_list.append(" ")
            binary_positions_list.append(" ")

        # Imprime la lista
        # print(binary_positions_list)

        return binary_positions_list

    # Crea la fila con los titulos de los digitos
    # Retorna una lista con todos los titulos
    def get_titles(self, n_p, type):

        # Lista por retornar
        title_list = [" "]

        # Exponente por comparar
        exp = 0

        # Agregara el titulo por cada bit que habra en el codigo
        for i in range(1, n_p + 1):

            if 2 ** exp == i:
                # Agrega el titulo del bit de paridad correspondiente
                title_list.append("p" + str(exp + 1))

                # Se aumenta el exponente
                exp += 1
            else:
                # Agrega el titulo del digito de informacion correspondiente
                title_list.append("d" + str(i - exp))

        # Si se esta decodificando se agregan los titulos para las pruebas de paridad
        if type == "decode":
            title_list.append("Prueba de Paridad")
            title_list.append("Bit de Paridad")

        # Imprime la lista
        # print(title_list)

        return title_list

    # Crea la fila con los datos de informacion
    # Retorna una lista con los datos en su posicion especifica
    def get_information_data(self, title_list, information, type):

        # Lista
        information_list = ["Datos"]

        # Recorre la lista con los titulos de los digitos, sin contar el primero
        for title in title_list[1:]:

            if type == "code":
                if title[0] == "p":
                    information_list.append(" ")
                elif title[0] == "d":
                    # Obtiene el primer digito de informacion
                    # Se guarda en la lista de informacion
                    information_list.append(information[0])
                    # Se elimina el primer digito de informacion
                    information = information[1:]
                else:
                    # Se agregan espacios vacios bajo los titulos de "Prueba de Paridad" y "Bit de Paridad"
                    information_list.append(" ")

            elif type == "decode":

                # Si exiten datos en el codigo
                if len(information) > 0:
                    # Obtiene el primer digito de informacion
                    # Se guarda en la lista de informacion
                    information_list.append(information[0])
                    # Se elimina el primer digito de informacion
                    information = information[1:]
                else:
                    # Se agregan espacios vacios bajo los titulos de "Prueba de Paridad" y "Bit de Paridad"
                    information_list.append(" ")

            else:
                information_list.append("ERROR")

        # Imprime la lista
        # print(information_list)

        return information_list

    # Agrega las filas restantes a la matriz para calcular la paridad y su resultado
    def set_parity_rows(self, n, p, n_p, matrix, type):

        # Hara una iteracion por cada p existente
        for i in range(1, p + 1):
            # Se crea una lista para cada p con us respectivo indice
            pi = ["p" + str(i)]

            # Hara una iteracion por cada columna de la matriz
            for j in range(len(matrix[0]) - 1):
                # Agrega un espacio vacio en cada espacio
                pi.append(" ")

            # Agrega la fila de la paridad actual
            matrix.append(pi)

        if type == "code":

            # Crea la leyenda de Hamming
            result_row = ["H(" + str(n_p) + "," + str(n) + ")"]

            # Hara una iteracion por cada columna de la matriz
            for j in range(len(matrix[0]) - 1):
                # Agrega un espacio vacio en cada espacio
                result_row.append(" ")

            # Agrega la fila donde aparecera el resultado de la codificacion
            matrix.append(result_row)

        return matrix


    ##########################################
    #                                        #
    #          Calculo de Paridades          #
    #                                        #
    ##########################################

    '''
    4. Calculo de los Bits de Paridad
        -> Se acomodan los valores de la informacion que se utilizaran en el calculo
        -> Se hace el calculo de las paridades del codigo
        -> Se agregan los valores de los bits de paridad a la tabla
    '''
    def calculate_parities(self, parity_type, p, n_p, matrix, type):

        # Se actualiza la matriz con los valores en las filas correspondientes de las paridades
        # Se obtiene una lista parcial con los valores por calcular la paridad
        matrix_and_parity_list = self.set_parity_calculation_values(matrix, p, n_p, type)

        # Se guarda la matriz actualizada con los valores de paridad por calcular
        matrix_no_parities = matrix_and_parity_list[0]

        # Se terminan de calcular las paridades a la hora de codificar
        if type == "code":

            # Se guarda la lista con los valores de las paridades por calcular
            partial_parities_list = matrix_and_parity_list[1]

            # Se calculan los Bits de Paridad a partir de los valores de la lista parcial
            # y se obtiene una lista con el valor de cada uno ya calculado
            parity_bits_list = self.get_parities(partial_parities_list, parity_type)

            # Se asignan los bits de paridad en su respectiva fila en la matriz
            matrix = self.asign_parity_bits(matrix_no_parities, parity_bits_list)

            # Se asigna la matriz actualizada
            self.code_matrix = matrix

        # A la hora de decodificar solo se necesitan acomodar los valores en la tabla,
        # sin calcular con los datos entrantes las paridades
        elif type == "decode":
            self.decode_matrix = matrix_no_parities

        else:
            print("calculate_parities(self, parity_type, p, n_p, matrix, type): Error")

    # Obtiene los valores para cada fila donde se calculara una paridad en la tabla
    # Retorna una lista de dos valores: la matriz actualizada y
    # una lista parcial solo con los valores a los que se les calculara la paridad
    def set_parity_calculation_values(self, matrix, p, n_p, type):

        # Lista parcial de los valores para calcular las paridades
        partial_parities_list = []

        # Fila de las posiciones de la matriz en binario
        bin_positions_row = matrix[0]

        # Fila de los titulos de la tabla
        titles_row = matrix[1]

        # Fila de los datos de la informacion
        data_row = matrix[2]

        # Numero del indice de la fila actual de los datos de paridad
        # Inicia en -1 para que empiece a contar hasta que se recorra la matriz en 0
        matrix_parity_index = -1

        # Se hara una iteracion por cada paridad existente
        for p_i in range(p):

            # Posicion donde estara la columna del bit de paridad de la iteracion
            # No se cuenta el espacio inicial, esto es para calcular el valor binario
            pi_position = 2 ** p_i
            # Posicion del bit de paridad en binario
            pi_position_binary = self.complete_dec_to_bin(pi_position, n_p)
            # Titulo de la paridad actual
            actual_pi_title = "p" + str(p_i + 1)

            # Se agrega el espacio para el valor de la paridad por calcular
            partial_parities_list.append("")

            # Se recorren las filas de la matriz para obtener el indice de la fila de la paridad actual
            # donde se tienen que guardar los valores de los digitos de la informacion
            for row in matrix:

                # Guarda el indice de la fila de la iteracion actual
                matrix_parity_index += 1

                # Se verifica que el indice de la fila sea el de la paridad correcta
                if row[0] == actual_pi_title:

                    # Al encontrar la fila, se deja de iterar y queda guardado el indice
                    # en "matrix_parity_index"
                    break

            # Se recorre la fila de posiciones en binario de los valores de la informacion
            # para encontrar cuales se deben agregar a la fila de la paridad actual
            for pos in range(len(bin_positions_row)):

                # Se saltan los valores que estan vacios en la fila de las posiciones
                if bin_positions_row[pos] != " ":

                    # Se verifica que el unico 1 que tiene el valor de la posicion en binario
                    # de la paridad, se encuentre tambien en la misma posicion de las posiciones
                    # en binario de los datos de la informacion con los que se calculara la paridad.
                    # "-(p_i + 1)" es la posicion donde se tiene que buscar el 1 en la posicion en binario
                    if pi_position_binary[-(p_i + 1)] == bin_positions_row[pos][-(p_i + 1)]:


                        # Si se esta decodificando
                        # Si se llega a la columna donde esta el valor de la paridad
                        if titles_row[pos][0] == "p" and type == "decode":

                            # Agregar el valor a la lista

                            # Se agrega el valor de la paridad en la fila de la paridad actual
                            # en la posicion que corresponde
                            matrix[matrix_parity_index][pos] = data_row[pos]

                            # Se juntan los valores de la paridad actual en un solo valor binario
                            # para formar una lista solo con los valores por calcular la paridad
                            partial_parities_list[p_i] += data_row[pos]


                    # Se saltan las posiciones en las que se encuentran las paridades
                    if titles_row[pos][0] != "p":

                        # Se verifica que el unico 1 que tiene el valor de la posicion en binario
                        # de la paridad, se encuentre tambien en la misma posicion de las posiciones
                        # en binario de los datos de la informacion con los que se calculara la paridad.
                        # "-(p_i + 1)" es la posicion donde se tiene que buscar el 1 en la posicion en binario
                        if pi_position_binary[-(p_i + 1)] == bin_positions_row[pos][-(p_i + 1)]:

                            # Se verifica que se esta en la fila de la paridad actual en la matriz oficial
                            if matrix[matrix_parity_index][0] == actual_pi_title:

                                # Se agrega el valor del digito en la fila de la paridad actual
                                # en la posicion que corresponde
                                matrix[matrix_parity_index][pos] = data_row[pos]

                                # Se juntan los valores de la paridad actual en un solo valor binario
                                # para formar una lista solo con los valores por calcular la paridad
                                partial_parities_list[p_i] += data_row[pos]

            # Se reinicia el indice de la matriz para encontrar el de la fila de la paridad siguiente
            matrix_parity_index = -1

        # Retorna una lista de dos valores: la matriz actualizada y la lista con los valores de las
        # paridades por calcular
        return [matrix, partial_parities_list]

    # Recibe una lista con los valores que se utilizaran para calcular las paridades
    # Retorna una lista con todos los bits de paridad calculados
    def get_parities(self, parities_list, parity_type):

        # Lista que contendra los valores de los bits de paridad calculados
        parity_bits = []

        # Recorre cada uno de los valores en binario
        for bin in parities_list:
            # Se calculan los bits de paridad dependiendo del tipo de paridad
            parity_bits.append(self.set_parity(bin, parity_type))

        #print("Parity bits: ", parity_bits)

        # Retorna la lista con los bits de paridad
        return parity_bits

    # Se calcula la paridad de un valor en binario
    # -> Para una paridad PAR, el bit de paridad sera uno (1) si el valor en binario llevar una
    #    cantidad par de unos, si no es cero (0).
    # -> Para una paridad IMPAR, el bit de paridad es un uno (1) si el valor en binario lleva una
    #    cantidad impar de unos, si no es cero (0).
    def set_parity(self, bin, parity_type):

        # Valor final de la paridad
        parity_bit = -1

        # Cantidad de 1's en el valor en binario
        ones = 0

        # Recorre el valor en binario
        for digit in bin:
            # Si se encuentra un 1
            if digit == "1":
                # Se agrega uno a la cuenta
                ones += 1

        #print("unos(" + bin + "): " + str(ones))

        # Si la cantidad de 1's es par
        if ones % 2 == 0:
            # Si la paridad se escoge par (0)
            if parity_type == "0":
                # El bit de paridad es 1
                parity_bit = 1
                #print("El bit de paridad par es de: ", parity_bit)
            # Si la paridad se escoge impar (1)
            elif parity_type == "1":
                # El bit de paridad es 0
                parity_bit = 0
                #print("El bit de paridad impar es de: ", parity_bit)
        # Si la cantidad de 1's es impar
        else:
            # Si la paridad se escoge par (0)
            if parity_type == "0":
                # El bit de paridad es 0
                parity_bit = 0
                #print("El bit de paridad par es de: ", parity_bit)
            # Si la paridad se escoge impar (1)
            elif parity_type == "1":
                # El bit de paridad es 1
                parity_bit = 1
                #print("El bit de paridad impar es de: ", parity_bit)

        # Reorna el bit de paridad ya calculado
        return parity_bit

    # Se agregan los bits de paridad ya calculados a las filas de la matriz que pertenecen
    def asign_parity_bits(self, matrix, parity_list):

        # Fila de los titulos de la tabla
        titles_row = matrix[1]

        # Indice de la fila en la que se encuentra
        row_index = -1

        # Se recorren las filas de la matriz
        for row in matrix:

            # Se asigna el indice de la fila actual
            row_index += 1

            # Al encontrar una fila perteneciente a una paridad
            if row[0][0] == "p":

                # Indice de la columna en la que se debe ingresar el bit de paridad
                parity_column_index = -1

                # Se itera la fila de los titulos
                for title in titles_row:

                    # Se asigna el indice de columna actual
                    parity_column_index += 1

                    # Se verifica si el titulo actual es igual al de la fila de la paridad
                    if title == row[0]:
                        # Se agrega a la amtriz el valor del bit de paridad como un string
                        matrix[row_index][parity_column_index] = str(parity_list.pop(0))

        # Retorna la matriz actualizada
        return matrix


    ##########################################
    #                                        #
    #         Informacion Codificada         #
    #                                        #
    ##########################################

    '''
    5. Codificacion Completa
        -> Se completa la tabla con el codigo completo finalizado
    '''
    def set_code(self):

        # Completa la matrix con el codigo completo y se obtiene el codigo listo
        self.coded_information_output = self.complete_code(self.code_matrix, self.code_n_p)

    # Ingresa los valores del codigo repartidos por la tabla en la ultima fila de la matriz
    def complete_code(self, matrix, n_p):

        # Codigo completo
        code = ""

        # Cantidad de filas de la matriz
        rows = len(matrix)

        # Iterara atraves de las columnas
        for col_i in range(1, n_p + 1):

            # Indice de las filas, empezando desde la ultima
            row_i = rows - 1

            # Se recorreran las filas de abajo hacia arriba buscando el primer valor que se encuentre
            # en cada columna que incluya un digito del codigo
            while row_i >= 0:

                # Se salta todos los valores de esa columna que esten vacios de abajo hacia arriba
                if matrix[row_i][col_i] != " ":
                    # Cuando logra obtener un valor, ese es el que tiene que ingresarse en la ultima fila
                    matrix[-1][col_i] = matrix[row_i][col_i]

                    # Agrega el valor a la variable del codigo
                    code += matrix[row_i][col_i]

                    # Sale del while para continuar con la siguiente columna
                    break
                else:
                    # Pasa a la siguiente fila hacia arriba
                    row_i -= 1

        # Completa la matrix con el codigo completo
        self.code_matrix = matrix

        # Retorna el codigo completo
        return code




    ####################################################################################
    #                                                                                  #
    #                                    Decoding                                      #
    #                                                                                  #
    ####################################################################################


    # Inicia el proceso de Decodificacion de Hamming y su Verificacion de Errores
    def decode(self, information, parity_type):

        # 1.
        # Se obtienen y guardan los datos con la informacion por codificar, ademas
        # se guarda la preferencia de la paridad del codigo
        self.set_input(information, parity_type, "decode")

        # 2.
        # Se calcula el tamano de la informacion (n), los bits de paridad necesarios (p) y
        # el tamano del codigo final (n + p)
        self.calculate_decoding_initial_variables()

        # 3.
        # Se crea la tabla para mostrar el proceso de codificacion por Hamming
        # Se crea la fila de posiciones en binario (no sera mostrada), la fila de los
        # titulos de las paridades y datos, la fila con los datos de la informacion y
        # las filas correspondientes al calculo de todas las paridades
        self.create_table(self.coded_information_input, self.decode_n, self.decode_p,
                          self.decode_n_p, self.decode_matrix, "decode")

        # 4.
        # Se acomodan los valores de la informacion que se utilizaran en el calculo de los bits de paridad,
        # se genera el calculo dependiendo de la paridad escogida y se rellena la tabla con los valores
        # finales de cada bit de paridad.
        self.calculate_parities(self.decode_parity_type, self.decode_p, self.decode_n_p,
                                self.decode_matrix, "decode")

        # 5.
        # Se calculan las paridades existentes en el codigo para que, a partir de estas,
        # se analice si algun bit del codigo ha sido comprometido. Se actualiza la tabla
        # con los valores correspondientes y los estados de los bits de paridad.
        self.check_for_error(self.decode_p, self.decode_matrix, self.decode_parity_type)

        # 6.
        # Se verifica si existe un error, si es asi, se busca el valor erroneo en la tabla,
        # a partir de la posicion recibida, y se cambia por su contrario, dejando el codigo
        # de forma correcta.
        self.fix_error(self.decode_bit_in_error, self.decode_matrix)

        # 7.
        # Se decodifica la informacion del codigo, al saber que este se encuentra
        # libre de errores.
        self.decode_information(self.coded_information_fixed, self.decode_n_p)

        # Imprime la matriz completa actualizada
        self.print_table(self.decode_matrix)

        # Retorna la informacion decodificada
        return self.decoded_information


    ##########################################
    #                                        #
    #          Variables Iniciales           #
    #                                        #
    ##########################################

    '''
    2.D. Calculo de Variables Iniciales para Decodificar
        -> Se calcula n + p: la cantidad total de bits en el codigo por decodificar
        -> Se calcula p: la cantidad de bits de paridad en el codigo
        -> Se calcula n: la cantidad de digitos de informacion por decodificar
    '''
    def calculate_decoding_initial_variables(self):

        # Obtiene el total de digitos del codigo entrante por decodificar
        self.decode_n_p = self.get_total_quantity(self.coded_information_input)

        # Define la cantidad de bits de paridad existentes (p)
        self.decode_p = self.get_parity_bits_quantity(self.decode_n_p)

        # Imprime la cantidad de bits de paridad
        print("p = " + str(self.decode_p))

        # Guarda la cantidad de digitos de informacion en el codigo (n)
        self.decode_n = self.get_information_digits_quantity(self.decode_n_p, self.decode_p)

        # Imprime la cantidad de digitos de informacion por decodificar
        print("n = " + str(self.decode_n))

        print("H(" + str(self.decode_n_p) + "," + str(self.decode_n) + ")")

    # Obtiene el total de digitos del codigo por decodificar
    def get_total_quantity(self, code):
        # Obtiene la cantidad total de digitos del codigo
        return len(code)

    # Obtiene la cantidad de bits de paridad existentes para decodificar
    def get_parity_bits_quantity(self, n_p):
        # Cantidad de bits de paridad
        p_i = 0

        # Verifica que se cumpla la inecuacion para saber cuantos bits existen
        while ((2 ** p_i) - 1) < n_p:
            # Se agrega un bit de paridad mas
            p_i += 1

        # Establece la cantidad fija de numeros de paridad
        return p_i

    # Obtiene la cantidad de digitos que posee solo la informacion del codigo, in los bits de paridad
    def get_information_digits_quantity(self, n_p, p):
        # Obtiene la cantidad de digitos de informacion
        return n_p - p



    ##########################################
    #                                        #
    #          Revision de Codigo            #
    #                                        #
    ##########################################


    '''
    5.D. Revision de Codigo
        -> Se calculan las paridades existentes en el codigo.
        -> A partir de las paridades encontradas, se analiza si algun bit
           del codigo se encuentra comprometido y se actualiza la tabla.
    '''
    def check_for_error(self, p, matrix, parity_type):

        # Se calculan las paridades del codigo
        # Se agregan sus valores a la matriz
        # Se retorna una lista con los valores de las paridades calculadas
        error_parity_list = self.get_error_parity_list(p, matrix, parity_type)

        # Se analizan cuales bits estan incorrectos
        # Se agrega su estado a la matriz (tabla queda completa)
        # Se obtiene la posicion en binario del bit que esta incorrecto, si no
        # existe un error, se obtiene un "0"
        bit_to_fix = self.check_error_parity_list(p, error_parity_list, matrix, parity_type)

        # Se guarda la posicion en binario que esta con un error
        self.decode_bit_in_error = bit_to_fix

        print("Posicion del Bit en Error:", self.decode_bit_in_error)


    # Se calculan las paridades del codigo
    # Se agregan sus valores a la matriz
    # Se retorna una lista con los valores de las paridades calculadas

    # Se calculan las paridades de cada fila de la matrix, se agregan estos valores a
    # su respectiva columna y se retornan estos valores en una lista
    def get_error_parity_list(self, p, matrix, parity_type):

        # Lista con las paridades calculadas para verificar el error
        error_parity_list = []

        # Lista con los valores en binario de cada fila
        complete_parity_binaries_list = []

        # Indice de la paridad de la iteracion
        p_i = 1

        # Recorre las filas de la matrix
        for row in matrix:

            # Si todavia se tienen que encontrar paridades
            if p_i <= p:

                # Titulo de la paridad actual
                actual_parity = "p" + str(p_i)

                # Valor en binario de la fila de la paridad
                actual_parity_bin = ""

                # Si se encuentra la fila con la paridad que se buscaba
                if row[0] == actual_parity:

                    # Se recorre toda la fila
                    for value in row:

                        # Se verifica que sea un "0" o un "1"
                        if value == "0" or value == "1":

                            # Se agrega el valor a la variable
                            actual_parity_bin += value

                    # Se agrega el valor en binario de esta paridad a la lista
                    complete_parity_binaries_list.append(actual_parity_bin)

                    # Se pasaria al siguiente bit de paridad
                    p_i += 1

        #print("complete_parity_binaries_list: ", complete_parity_binaries_list)

        # Se calculan las paridades para verificar el error
        error_parity_list = self.get_parities(complete_parity_binaries_list, parity_type)

        #print("error_parity_list", error_parity_list)

        # Retorna la lista de paridades con error
        return error_parity_list


    # Se analizan cuales bits estan incorrectos
    # Se agrega su estado a la matriz (tabla queda completa)
    # Se obtiene la posicion en binario del bit que esta incorrecto, si no
    # existe un error, se obtiene un "0"
    # Para que se obtenga el valor binario correcto, se debe invertir el orden.
    # El primer digito de la posicion es el ultimo de la tabla
    def check_error_parity_list(self, p, parity_list, matrix, parity_type):

        # Posicion en binario del bit que se encuentra en error
        bit_to_fix = ""

        # Flag para saber si hay error
        error_is_present = False

        # Fila con los titulos de la matriz
        titles_row = matrix[1]

        # Titulo de la columna donde estaran los estados
        state_column_title = "Prueba de Paridad"

        # Indice de la columna donde estaran los estados
        state_column_index = -1

        # Titulo de la columna donde estaran los valores de las paridades calculadas
        parity_column_title = "Bit de Paridad"

        # Indice de la columna donde estaran los valores de las paridades calculadas
        parity_column_index = -1

        # Indice de la paridad de la iteracion
        p_i = 1

        # Indice de la fila actual en la iteracion
        row_i = -1

        # Para obtener el indice de la posicion de state_column_title
        for title in titles_row:
            state_column_index += 1
            if title == state_column_title:
                break

        # Para obtener el indice de la posicion de parity_column_title
        for title in titles_row:
            parity_column_index += 1
            if title == parity_column_title:
                break

        # Recorre las filas de la matrix
        for row in matrix:

            # Aumenta el indice actual de la fila
            row_i += 1

            # Si todavia se tienen que verificar los estados de las paridades
            if p_i <= p:

                # Titulo de la paridad actual
                actual_parity = "p" + str(p_i)

                # Si se encuentra la fila con la paridad que se buscaba
                if row[0] == actual_parity:

                    # Se obtiene el valor de la paridad actual
                    actual_parity_value = str(parity_list.pop(0))

                    # Se agrega el valor del bit de paridad a la matriz
                    matrix[row_i][parity_column_index] = actual_parity_value

                    # Se agrega el valor del bit de paridad al string para encontrar la posicion
                    # del bit que se debera arreglar.
                    # Para que se obtenga el valor binario correcto, se debe invertir el orden.
                    # El primer digito de la posicion es el ultimo de la tabla
                    bit_to_fix = actual_parity_value + bit_to_fix

                    # Si la paridad es "0", no hay error
                    if actual_parity_value == "0":
                        # Se agrega a la tabla "Correcto"
                        matrix[row_i][state_column_index] = "Correcto"

                    # Si la paridad es "1", se encuentra un error
                    elif actual_parity_value == "1":
                        # Se agrega a la tabla "Error"
                        matrix[row_i][state_column_index] = "Error"

                        # Como se encontro un error, se cambia el flag
                        error_is_present = True

                    # Si hay un error en el codigo
                    else:
                        matrix[row_i][state_column_index] = "NULL"

                    # Se pasaria al siguiente bit de paridad
                    p_i += 1

        # Actualiza la matriz con los valores para verificar el error
        self.decode_matrix = matrix

        # Se verifica si no hubo algun error presente
        if not error_is_present:
            # Se cambia bit_to_fix a solamente "0"
            bit_to_fix = "0"

        return bit_to_fix



    ##########################################
    #                                        #
    #          Correcion de Error            #
    #                                        #
    ##########################################

    '''
    6. Correcion del bit en error
        -> Se verifica si existe un error.
        -> Si el error existe, se busca el valor erroneo en la tabla, a partir de la posicion recibida,
           y se cambia por su contrario, dejando el codigo de forma correcta.
    '''
    def fix_error(self, bit_in_error, matrix):

        # Si se encuentra un bit en error en el codigo
        if bit_in_error == "0":
            print("El código no tiene errores")

            self.coded_information_fixed = self.coded_information_input

        # Si hay un error al encontrar el bit en error y no se cambia la variable
        elif bit_in_error == "-1":
            print("Error encontrando el bit en error del codigo")

        else:
            # Se corrige el error en el codigo y se cambia al correcto
            self.coded_information_fixed = self.fix_bit_in_error(bit_in_error, matrix)

            #print("self.coded_information_fixed:", self.coded_information_fixed)


    # Se busca el bit en error en el codigo existente y se cambia por el correcto
    def fix_bit_in_error(self, bit_in_error, matrix):

        # Codigo corregido
        fixed_code = ""

        # Fila de posiciones en binario
        bin_positions_row = matrix[0]

        # Fila de los valores de los datos
        data_row = matrix[2]

        # Indice de los datos
        data_index = -1

        # Indice del bit por cambiar
        bit_index = -1

        # Itera a traves de las posiciones en binario
        for pos in bin_positions_row:

            # Aumenta el indice del bit por cambiar
            bit_index += 1

            # Si la posicion es igual a la posicion por cambiar el bit
            if pos == bit_in_error:
                # Sale del for para mantener el indice
                break

        # Se itera a traves de los datos
        for data in data_row:

            # Aumenta el indice de los datos
            data_index += 1

            # Se buscan solamente los datos en la fila
            if data == "1" or data == "0":

                # Si se encuentra el bit en error
                if data_index == bit_index:

                    # Si el bit en error es un "0"
                    if data == "0":
                        # Se cambia su valor por un "1" en el codigo corregido
                        fixed_code += "1"

                    # Si el bit en error es un "1"
                    elif data == "1":
                        # Se cambia su valor por un "0" en el codigo corregido
                        fixed_code += "0"

                    else:
                        print("Error al encontrar al cambiar el bit en error")

                # Si no es el bit en error
                else:
                    # Se agrega el dato existente al string con el codigo corregido
                    fixed_code += data

        # Se actualiza el codigo
        return fixed_code



    ##########################################
    #                                        #
    #            Decodificacion              #
    #                                        #
    ##########################################


    '''
    7. Decodificacion del codigo
        -> Se decodifica la informacion del codigo, al saber que este se encuentra
           libre de errores.
    '''
    def decode_information(self, code, n_p):

        # Informacion decodificada
        information = ""

        # Exponente por comparar
        exp = 0

        # Iterara a traves del codigo
        for i in range(1, n_p+1):

            # Si es una posicion de un bit de paridad
            if 2 ** exp == i:
                # Se elimina el bit de paridad
                code = code[1:]
                # Se aumenta el exponente
                exp += 1
            else:
                # Se agrega el bit que pertenece a la informacion
                information += code[0]
                # Se elimina el bit recien agregado
                code = code[1:]

        # Se asigna el valor de la informacion proveniente del codigo
        self.decoded_information = information

        #print("\nself.decoded_information:", self.decoded_information)




    ####################################################################################
    #                                                                                  #
    #                                 Conversiones                                     #
    #                                                                                  #
    ####################################################################################

    # Completa el binario con la cantidad de digitos del valor mayor necesario
    def complete_dec_to_bin(self, dec, biggest):

        # Convierte el indice a binario en string
        raw_bin = str(self.converter.dec_to_bin(dec))

        # Verifica que todos los binarios tengan el mismo largo
        while len(raw_bin) != len(self.converter.dec_to_bin(biggest)):
            # Se le agrega un "0" a la izquierda para aumentar su tamano
            raw_bin = "0" + raw_bin

        # Retorna el binario completo
        return raw_bin



    ####################################################################################
    #                                                                                  #
    #                                  Impresion                                       #
    #                                                                                  #
    ####################################################################################


    # Imprime la tabla a partir de la matrix utilizada para codificar
    def print_table(self, matrix):

        print("")

        # Recorre cada fila de la matriz
        for row in matrix:

            # Imprime la fila
            print(row)
