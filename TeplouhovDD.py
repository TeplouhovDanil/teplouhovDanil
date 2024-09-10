import math

def number18(weight, pages, string, symbols):
    weight_bite = weight * 8
    k = pages * string * symbols
    i =  weight_bite / k
    N = 2**i
    return N

def number19(n1, n2):
    in1 = math.log2(n1)
    in2 = math.log2(n2)
    Difference = in1 / in2
    return Difference


def number20(N,I):
    i = math.log2(N)
    k = I / i
    return k

def number192(H):
    N = 2**H
    return N

def number202(H):
    N = 2**H
    return N

def number7(i, K):
    N = 2**i * K
    WB = 8 + 8
    Brown = N - WB
    return Brown
    








if __name__ == "__main__":
    # номер 18(Кибернетика)
    # number18_1 = int(input("Ввод общего объёма в байтах ")) 
    # number18_2 = int(input("Ввод общего колличества страниц "))
    # number18_3 = int(input("Ввод количества строк "))
    # number18_4 = int(input("Ввод количества символов в строке "))
    # print( "мощность алфавита равна ", number18(number18_1, number18_2, number18_3, number18_4)
    
    # номер 19(Кибернетика)
    # inp19_1 = int(input("Ввод мощности првого алфавита "))
    # inp19_2 = int(input("Ввод мощность второго алфавита "))
    # print("Мощность алфавитов отличается", number19(inp19_1, inp19_2))

    # номер 20(Кибернетика)
    # inp20_1 = int(input("Ввод мощности алфавита "))
    # inp20_2 = int(input("Ввод общего ввида текста "))
    # print("Количество символов в данном сообщении составляет: ", number20(inp20_1, inp20_2))

    # номер 19(разновёрстное)
    # inp192_1 = int(input("Ввод веса информации "))
    # print("Колличество этажей в доме составляет:", number192(inp192_1))
    
    # номер 20(Равновероятностные)
    # inp202_1 = int(input("Ввод веса информации: "))
    # print("Количество подъездов в доме составляет: ", number202(inp202_1))

    # номер 7(на разновероятностные события)
    # inp7_1 = int(input("Ввод веса 1 банки белой краски: "))
    # inp7_2 = int(input("Ввод количества банок синей краски: "))
    # print("Количество банок коричневой краски: ", number7(inp7_1, inp7_2))