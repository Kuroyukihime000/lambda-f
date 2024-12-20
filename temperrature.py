#Azarenko
#take temperature in cakcium from user
#and convert it ti farenheit
#=====================================

#Convertiation function
def temp(a):
    lol = a * 1.8 + 32
    return lol

#Main function
def main():
    user_temp = float(input("Input temperature in calcium" 
                            "you wont to caonvert: "))
    res_temp = temp(user_temp)
    print("Temperation in Forengeits: ", res_temp)


if __name__ == '__main__':
    main()