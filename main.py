'''
Diseño Lógico
Proyecto 1
Codigo Hamming
Main
'''

from hamming import *

# Crea una instancia de Hamming
hamming = Hamming()

binario = "10110100"


# Codificacion

# Dato en binario del usuario por codificar
information_to_code = "0110101" + "10111"

# Paridad escogida por el usuario
# 0 -> par , 1 -> impar
parity_to_code = "0"

# Inicia la codificacion de Hamming al dato del usuario
hamming_code = hamming.code(information_to_code, parity_to_code)
print("\nHamming code:", hamming_code)

# Decodificacion

# Dato por decodificar
code_to_decode_1 = "10001100101"
code_to_decode_0 = "01011101101"
code_to_decode_r = "101010101010"

# Paridad utilizada al codificar
# 0 -> par , 1 -> impar
decoding_parity = "1"

# Inicia la decodificacion de Hamming al codigo recibido
informacion = hamming.decode(hamming_code, parity_to_code)

print("\nInformacion decodificada:", informacion)