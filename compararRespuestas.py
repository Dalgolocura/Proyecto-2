file1 = open("Proyecto-2/ou.out", "r")
file2 = open("Proyecto-2/P2_cases_students.out", "r")
fileSalida = open("Proyecto-2/compararResultados.txt", "w")
diferentes = 0
caso = 1


linea1 = file1.readline().replace("\n", "")
linea2 = file2.readline().replace("\n", "")
fileSalida.write("Casos mal:\n")

while linea1 != "" or linea2 != "":
    if linea1 != linea2:
        diferentes += 1
        lineaSalida = "Caso " + str(caso) + ": Nuestro " + linea1 + " Profe " + linea2
        try:
            lineaSalida += " Diferencia: " + str(int(linea1) - int(linea2))
        except:
            pass
        lineaSalida += "\n"
        fileSalida.write(lineaSalida)
    linea1 = file1.readline().replace("\n", "")
    linea2 = file2.readline().replace("\n", "")
    caso += 1

fileSalida.write("Casos diferentes:" + str(diferentes) + "\n")
file1.close()
file2.close()
fileSalida.close()
