from read import show_stock
from sold_laptops import Sold_Laptops
from buying_laptops import Buying_Laptops




# welcome Message
def welcome():
    print("                                  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄    ")
    print("                                  █░▄▄▀█░██░█▄░▄█░██░█░▄▀▄░█░▄▄▀███░██░▄▄▀█▀▄▄▀█▄░▄█▀▄▄▀█▀▄▄▀████░▄▄░█░▄▄▀█░██░██░▄▄█░▄▄▀█░██░    ")
    print("                                  █░▀▀░█░██░██░██░██░█░█▄█░█░██░███░██░▀▀░█░▀▀░██░██░██░█░▀▀░████░█▀▀█░▀▀░█░██░██░▄▄█░▀▀▄█░▀▀░    ")
    print("                                  █░██░██▄▄▄██▄███▄▄▄█▄███▄█▄██▄███▄▄█▄██▄█░█████▄███▄▄██░███████░▀▀▄█▄██▄█▄▄█▄▄█▄▄▄█▄█▄▄█▀▀▀▄    ")
    print("                                  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀    ")
    print("                                      |  Pokhara | Gharipatan-07 | Contact: 98******** |  Email-abishek@gmail.com  |         ")

    print("                                      |                      \\\                        =o)                         |")
    print("                                  / \                          (o>                       /\\\                                ")
    print("                                 /   \-------------------------(()__Welcome To Gallery___\_V-----------------------,")
    print("                                 \__,|                         //                         \\\                      | ")
    print("                                     |             ***************************************************            |")
    print("                                     |              Please Choose One Of The Option Below To Proceed              |")
    print("                                     |             ***************************************************            |")
    print("                                     |                                                                            | ") 
    print("                                     |                  Enter 1 --> Display The Laptops Available.                |")
    print("                                     |                  Enter 2 --> For Selling Laptops.                          | ")
    print("                                     |                  Enter 3 --> Purchase laptops from the vendor.             |")
    print("                                     |                  Enter 99 --> Exit.                                        | ")
    print("                                     |                                                                            |")
    print("                                     |  ,-------------------------------------------------------------------------------")
    print("                                     \   /                                                                         /")
    print("                                      \_/_________________________________________________________________________/ ")

welcome()

def Begin():
    while True:
        try:
            option = int(input("\nEnter your option:-->"))
            if option == 1:
                #importing show_stock function from read.py
                show_stock()
            elif option == 2:
                #importing sold_laptops function from sold_laptops.py
                Sold_Laptops()
            elif option ==3:
                #importing Buying_Laptops function from buying_laptops.py
                Buying_Laptops()
    
            elif option ==99:
                #Thanks message 
                                                                                                                           
                print(""" \n\n   

                                                                                 
                                    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                                    █▄░▄█░████░▄▄▀█░▄▄▀█░█▀███░██░█▀▄▄▀█░██░███░▄▄█▀▄▄▀█░▄▄▀███░██░█▀▄▄▀█░██░█░▄▄▀███▄░▄██▄██░▄▀▄░█░▄▄
                                    ██░██░▄▄░█░▀▀░█░██░█░▄▀███░▀▀░█░██░█░██░███░▄██░██░█░▀▀▄███░▀▀░█░██░█░██░█░▀▀▄████░███░▄█░█▄█░█░▄▄
                                    ██▄██▄██▄█▄██▄█▄██▄█▄█▄███▀▀▀▄██▄▄███▄▄▄███▄████▄▄██▄█▄▄███▀▀▀▄██▄▄███▄▄▄█▄█▄▄████▄██▄▄▄█▄███▄█▄▄▄
                                    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀


                                    
                                                                                                                                    \n\n """)
                #breaking the loop to exit or stop the program 
                break
            else:
                welcome()
                print("----------------------------[Please enter the options from 1 to 3 & for Exit press 99.]--------------------------------\n")
        except:
            welcome()
            # informing user to input numeric value to proceed to next step
            print("----------------------------[Please enter numeric value only]--------------------------------\n")
            
Begin()

