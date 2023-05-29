from read import Read_Stocks
from dateTime import *
from write import buying_bill


# this function ask which Laptop to purchae and also quantity to purchase 
# after purchasing successfully it adds the quantity  to the original stock 
# lastly, show the invoice in the shell and creates a purchase bill

def Buying_Laptops():
    laptops = Read_Stocks()
    buying_laptops=[]
    while True:
        try:
             #asking name and running loop until name is a valid
            name= (input("Enter your store name(alphabets only)-->"))
            break
        except:
            print("----------------Input as instructed--------------")

    address=str(input("Enter your address-->"))
    while True:
        try:
             #asking contact and running loop until contact is a valid
            contact= int(input("Enter your contact(numbers only)-->"))
            check=str(contact)
            if (len(check)>10 )or(len(check)<10):
                print("Contact number should be of 10 numbers")
            else:
                break
        except:
            print("--------------Input as instructed---------------")

    # displaying Laptops that can purchase 
    print("\n\n Avaliable Laptops (choose any you want)")
    print("+------+---------------------------------------+")
    print("| S.N  |             Laptops Name              |")
    print("+------+---------------------------------------+")
    count=0
    for items in range(len(laptops)):
        print("| ",count," ","|"," "*5,laptops[items][0]," "*(30-len(laptops[items][0])),"|")
        print("+------+---------------------------------------+")
        count+=1
    print("")

    count=0
    while True:
        while True:
            try:
                #asking S.N and running loop until S.N is a valid
                SN = int(input("\nEnter S.N for purchasing Laptop here-->"))
                if SN<0 or SN>(len(laptops)-1):
                    print("------------Invalid serial number-----------")
                else:
                    buying_laptops.append(laptops[SN])
                    break
            except:
                 print("----Invalid SN number------")
        print("\nHow many of",laptops[SN][0],"do you want to purchase?")
        while True:
            try:
                # running loop until number entered is valid 
                No_of_laptops = int(input("Enter number here-->"))
                if No_of_laptops <0:
                    print("-----------------------------(Please enter value from 1.)------------------------------------")
                else:
                    buying_laptops[count].append(No_of_laptops)
                    break
            except:
                print("------------------------------------Invalid Input--------------------------------------------")        
 # storing new number of stock
        available_laptops = int(buying_laptops[count][3]) + int((No_of_laptops))

        # replacing quantity from stock file
        # Open file for reading
        file = open("stock.txt", "r")
        # Read file content
        quality = file.read()
        # Replace string
        quality = quality.replace(str(laptops[SN][3]), str(available_laptops))
        # Close file
        file.close()
        # Open file for writing
        file = open("stock.txt", "w")
        # Write updated content
        file.write(quality)
        # Close file
        file.close()


        print("Do you want purchase another laptop?")
        try:
            confirm = input("Enter (Y) for yes or (N) for no-->")
            if (confirm == "y") or (confirm == "Y"):
                count+=1
            elif (confirm == "n") or (confirm == "N"):
                    break
            else:
                    print("-----------Please input as Invalid--------")

        except:
                print("-----------Please input as instructed--------")

    while True:
        print ("\n\nDo you want me to print the invoice purcahse bill  ??\n")
        try:
                bill=input("\nEnter (Y/y) for yes or (N/n) for no-->")
                if (bill=="Y")or(bill=="y"):
                    # Generatring rent invoice
                    Date = date()
                    Time = time()
                    buying_bill(name,Date, Time, address,contact, buying_laptops)
                    break

                elif(bill=="N")or(bill=="n"):
                     print("Printing bill is necessary, So please print the bill")
                else:
                    print("-----------Please Input  as Invalid--------")
        except:
                print("-----------Please input  Instructed--------")
    