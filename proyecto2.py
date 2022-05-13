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
    mayor= None
    menortemporal = None
    menortotal = min(lista)
    inicio = None
    componentes = 0
    igual= False
    for n in range(0, len(lista)):
            num = int(lista[n])
            if mayor == None:
                inicio = num
                menortemporal = num
                mayor = num
                componentes+=1

            elif num> mayor:
                menortemporal = mayor
                mayor = num
                componentes+=1

            elif num <  menortemporal:
                if mayor == menortemporal:
                    menortemporal= num
                elif componentes > 1:
                    componentes-=1
            if menortemporal == menortotal:
                igual = True
    if menortotal == inicio or igual:
        componentes = componentes+1
    print(componentes)


lectura()

# procesar([2,5,8,1,4,3,6,7])
# procesar([2,1,4,3,5])
# procesar(["7", "1", "5", "6", "4", "3", "2"])
