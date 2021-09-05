'''
Diseño Lógico
Proyecto 1
Codigo Hamming
Clase NRZI
'''

from matplotlib import pyplot as plt


# Clase con las funciones de NRZI
class NRZI:

    def graph(self, binario):

        y = [-1, -1]
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        avance = 0

        for i in binario:  # recorre cada caracter del codigo de 12 bits

            if ((i == "0" and y[avance + 1] == 1) or (i == "1" and y[avance + 1] == -1)):
                # si es uno, realiza un cambio de estado, si es cero, se mantiene
                y.append(1)

            if ((i == "0" and y[avance + 1] == -1) or (i == "1" and y[avance + 1] == 1)):
                y.append(-1)

            avance = avance + 1

        plt.step(x, y)
        plt.show()  # muestra grafico
