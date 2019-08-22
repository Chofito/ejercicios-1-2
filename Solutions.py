def task_1(a_sacar):
    pass # Creo que era mas sencillo el del archivo de texto triangle.txt xD

def calcular_5(cantidad):
    return ["5C" for i in range(int(cantidad * 20))]

def calcular_10(cantidad):
    cantidad_10 = ["10C" for i in range(int(cantidad * 10))]
    sobrante = cantidad % 0.1
    return [cantidad, sobrante]

def calcular_25():
    cantidad_25 = ["25C" for i in range(int(cantidad * 4))]
    sobrante = cantidad % 0.25
    return [cantidad_25, sobrante]

def calcular_50():
    cantidad_50 = ["50C" for i in range(int(cantidad * 2))]
    sobrante = cantidad % 0.5
    return [cantidad_50, sobrante]

# 1 Quetzal
def calcular_100():
    cantidad_100 = ["100" for i in range(int(cantidad))]
    sobrante = cantidad % 1
    return [cantidad_100, sobrante]

def task_2():
    lista_machete = []
    for i in range(10000):
        num = i
        reversed_num = str(i)[::-1]
        for j in range(51):
            result = num + int(reversed_num)
            txt = str(result)
            n = len(txt)
            count = 0
            for x in range(0,n-1):
                if txt[x] == txt[n-x-1]:
                    count += 1
            
            if count == n:
                break
            else:
                num = result
                reversed_num = str(result)[::-1]

        else:
            lista_machete.append(i)

    return lista_machete

if __name__ == '__main__':
    print(task_2())
    print(calcular_5(100))
