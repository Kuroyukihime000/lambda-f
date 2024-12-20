# Azarenko
# Checking your number for evenness
# =====================================

def even(a):  #Функция проверки на четность
    if a%2==0 : return 0
    elif a%2==1 : return 1
def main():
    user_number = int(input('Input your number: '))
    res = even(user_number)
    if res==0 : res = print("true")
    elif res==1 : res = print("folse")

if __name__ == '__main__':
    main()
