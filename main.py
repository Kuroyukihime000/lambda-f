# Azarenko
# Main file of the project
# All rights are reserved
# =====================================

# Import all nessesary libs and modules
import circle as rad
import is_even as num
import temperrature as temper


# The main function of project
def main():
    user_choise = input("Choose"
                            "the function you want to use: ")
    if user_choise.lower() == 'temperrature':
        user_temp = float(input("Input temperature in calcium" 
                            "you wont to caonvert: "))
        print("Temperation in Forengeits: ", temper.temp(user_temp))
    elif user_choise.lower() == 'circle':
        user_radius = float(input("Input your radius: "))
        print("Your area and length of a circle: ", rad.dl(user_radius), rad.pl(user_radius))
    elif user_choise.lower() == 'is_even':
         user_number = int(input('Input your number: '))
         res = num.even(user_number)
         if res==0 : print("true")
         else:
             print("folse")

if __name__ == "__main__":
    main()

         


        




        

    