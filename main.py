from time import localtime, sleep, time
import os
import math


def main():
    print('Iniciando relogio, aguarde alguns instantes...')
    while localtime().tm_sec%2 != 0:
        continue
    while True:
        relogio = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "\033[1;36m1\033[m", "\033[1;36m2\033[m", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", "1", "1", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", "1", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "1", "0", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", "2", "", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", "\033[1;36m9\033[m", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "\033[7;36m \033[m", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", "\033[1;36m3\033[m", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", "8", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", "4", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", "7", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", "5", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", "\033[1;36m6\033[m", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
]

        #definindo o horario
        time1 = time()
        horario = localtime()
        h,m,s = horario.tm_hour, horario.tm_min, horario.tm_sec        
        relogio = ponteiros(relogio, (h,m,s))
        mostrar(relogio)
        sleep(1-(time()-time1))
        

def ponteiros(relogio: list, hor: tuple):
    centro_j = 13
    centro_i = 13
    def hastes(relogio:list,angulo:float, tam:int, cor:str = '0') -> list:
        
        for x in range(1,tam+1):
            d_i = round(centro_i - x * math.cos(angulo))
            d_j = round(centro_j + x * math.sin(angulo))
            
            relogio[d_i][d_j] = f'\033[7;{cor}m \033[m'
        
        return relogio
        
    h, m, s = hor
    
    # Coordenadas do centro do relógio
    
    # Calculando as coordenadas para os ponteiros
    # Ponteiro das horas
    angulo_h = math.radians(30 * (h % 12 + m / 60+ s / 3600))  # Adiciona os minutos como fração das horas
    relogio = hastes(relogio, angulo_h, 6, cor = '33')
    i_h = round(centro_i - 6 * math.cos(angulo_h))
    j_h = round(centro_j + 6 * math.sin(angulo_h))
    relogio[i_h][j_h] = '\033[33mH\033[m'
    
    # Ponteiro dos minutos
    angulo_m = math.radians(6 * m)
    relogio = hastes(relogio, angulo_m, 8, cor = '32')
    i_m = round(centro_i - 8 * math.cos(angulo_m))
    j_m = round(centro_j + 8 * math.sin(angulo_m))
    relogio[i_m][j_m] = '\033[32mM\033[m'
    
    # Ponteiro dos segundos
    angulo_s = math.radians(6 * s)
    relogio = hastes(relogio, angulo_s, 10,cor = '31')
    i_s = round(centro_i - 10 * math.cos(angulo_s))
    j_s = round(centro_j + 10 * math.sin(angulo_s))
    relogio[i_s][j_s] = '\033[31mS\033[m'
    
    return relogio
    
def round(num:float)->int:
    def modulo(num:float) -> float:
        return num if num >= 0 else -num
    def aprox(num:float) -> int:
        if modulo(num - int(num)) >= 0.5:
            return int(num) + 1 if num > 0 else int(num) - 1
        return int(num)

    lendec = len(str(modulo(num-int(num))))
    num = int(num*10**lendec)

    for _ in range(lendec):
        num /= 10
        num = aprox(num)

    return num


def mostrar(relogio:list)->None:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'                      \033[33m{'0'*(2-len(str(localtime().tm_hour)))}{int(localtime().tm_hour)}\033[m', ':', f'\033[32m{'0'*(2-len(str(localtime().tm_min)))}{int(localtime().tm_min)}\033[m', ':', f'\033[31m{'0'*(2-len(str(localtime().tm_sec)))}{int(localtime().tm_sec)}\033[m')
    for linha in relogio:
        print(linha:=' '.join(linha))

if __name__ == '__main__':
    main()
