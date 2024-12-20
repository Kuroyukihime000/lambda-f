print("Введите число ")
def sumdigits(b):  #Функция нахождения суммы цифр числа
    bb=list(b)
    for i in range (0, len(bb)):
        bb[i]=int(bb[i])
    sum=0
    for i in bb:
        sum=sum+i
    return sum


lol=input()
sum=sumdigits(lol) #Использование функции
print("Сумма цифр ", sum)     