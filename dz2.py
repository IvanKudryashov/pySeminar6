# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def zadacha2():
    spisok = list(map(int,input("Задайте список чисел через пробел:  ").split()))
    print(spisok)
    rez = [spisok[i]*spisok[-(i+1)] for i in range ((len(spisok)+1)//2)]
    print(rez)    
zadacha2()