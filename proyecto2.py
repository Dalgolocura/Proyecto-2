#                ඞ mondongos

from timeit import default_timer as timer
from sys import stdin


def lectura():
    start = timer()
    nCasos = int(stdin.readline())
    # print(nCasos)
    while nCasos != 0:

        linea = stdin.readline().replace('\n', '')
        lista = linea.split(" ")
        # print("lista", lista)
        procesar(lista)

        nCasos -= 1

    elapsed_time = timer() - start
    print("Time: %.10f" % elapsed_time)


def procesar(lista):
    encontrados = {}
    componentes = 0
    for n in range(0, len(lista)):
        n1 = int(lista[n])
        if n1 not in encontrados:
            repetido = False
            encontrados[n1] = 0
            for i in range(n+1, len(lista)):
                n2 = int(lista[i])
                if repetido and (n1 > n2) and n2 not in encontrados:
                    encontrados[n2] = 0
                if (not(repetido)) and (n1 > n2):
                    if n2 in encontrados:
                        repetido = True
                    if n2 not in encontrados:
                        encontrados[n2] = 0
            if repetido == False:
                componentes += 1
    print(componentes)


lectura()

# procesar([2,5,8,1,4,3,6,7])
# procesar([2,1,4,3,5])
# procesar(["7", "1", "5", "6", "4", "3", "2"])
