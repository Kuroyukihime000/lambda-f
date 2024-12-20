# Azarenko
# Calculating the area and length of a circle
# =====================================

def pl(a):       # Функция поиска площади
    pl=a*a*3.14  
    return pl
 
def dl(a):        # Функция поиска длины
    dl=2*a*3.14
    return dl

def main():
    user_radius = float(input("Input your radius: "))
    res_dl = dl(user_radius)
    res_pl = pl(user_radius)
    print("Your area and length of a circle: ", res_dl, res_pl)

if __name__ == '__main__':
    main()