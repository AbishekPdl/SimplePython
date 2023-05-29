from read import Read_Stocks
from dateTime import *
from write import selling_bill

# this function ask which laptops to sold and also quantity to sold.
#  after selling successfully it subtracts the quantity solded from the original stock 
# lastly, show the invoice in the shell and creates a sold  bill of the tiems.


def Sold_Laptops():
    sold_Laptops=[]
    laptops= Read_Stocks()

    while True:
         #asking name and running loop until name is a valid
        try:
            name=(input("Enter your Name(alphabets only)-->"))
            break
        except:
            print("----------------Input as instructed--------------")
    
    address= str(input("Enter your Address-->"))
    
    while True:
     #asking contact and running loop until contact is a valid
        try:
            contact=int(input("Enter your Contact(number only)-->"))
            check=str(contact)
            if (len(check)>10 )or(len(check)<10):
                print("--------------Contact number should be of 10 numbers--------------")
            else:
                break
        except:
            print("--------------Input as instructed---------------")

    # displaying laptops the customer can buy 
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

    Grand_Total=0
    count=0
    while True:
        try:
            #asking S.N and running loop until S.N is a valid'
            while True:
                laptops_Number=int(input("\nEnter The Laptops S.N you want to Buy-->" ))
                # Laptop number should be above 0 and less than given S.N
                if laptops_Number<0 or laptops_Number>(len(laptops)-1):
                    print("\n______________Enter correct S.N for the Laptop_________________\n")
                # cannot rent if the stock is zero
                elif(laptops[laptops_Number][3]==0):   
                    print("\n-----No stock available for this laptop---------")
                    print("")
                    print("---------Please choose another-------------")

                else:
                    break
        except:
            print("----------------------Please enter valid S.N--------------------------")
            count+=1


        if laptops_Number<0 or laptops_Number>(len(laptops)-1):
            print("\n______________Enter correct S.N for the laptop_________________\n")
        else:
            # adding the laptop selected by the user to the list
            selling_laptops=laptops[laptops_Number]
            sold_Laptops.append(selling_laptops)
    
            #storing laptops information to their respective variable
            laptops_name= laptops[laptops_Number][0]
            laptops_Brand= laptops[laptops_Number][1]
            laptops_Price= laptops[laptops_Number][2]
            available_laptops= laptops[laptops_Number][3]
            laptops_Processor= laptops[laptops_Number][4]
            laptops_Graphics= laptops[laptops_Number][5]
            print("")
            print("")
            print("Laptop you choosed is : ",laptops_name)
            print("Available number of stock for ",laptops_name," : ",available_laptops)
            print("Laptop Brand : ",laptops_Brand)
            print("Laptop Processor : ",laptops_Processor)
            print("Laptop Graphics : ",laptops_Graphics)
            print("\nCost price for 1 ",laptops_name," with discount of the day is: $",laptops_Price)
        

            while True:
                try:
                    # asking user the number of laptops to buy
                    no_Of_Laptops= int(input("\nHow many of this would you like to buy?-->"))
                    #selling number cannnot be 0
                    if no_Of_Laptops < 0:
                        print("-----------------------------(Please enter valid value.)------------------------------------")
                    # cannot sell laptops more than the available laptops
                    elif no_Of_Laptops > available_laptops:
                        print("\nCannot sell the laptop.\n")
                        print("\nIt exceeds the available stock number for ",laptops_name," that is availabe stock with us : ",available_laptops,".")
                    else:
                        sold_Laptops[count].append(no_Of_Laptops)
                        break
                except:
                    print("------------------------------------Invalid Input--------------------------------------------")
          
           #calculating the cost of the customer
            amount= int(laptops_Price) *int(no_Of_Laptops)
            print("\n Laptop Sold Successful : The total cost for ",laptops_name,": $",amount,"\n")
            available_laptops=int(laptops[laptops_Number][3])-int(no_Of_Laptops)


            # replacing quantity from stock file
            # Open file for reading
            file= open ("stock.txt","r")
            # Read file content
            quantity =file.read()
            # Replace string
            quantity= quantity.replace(str(laptops[laptops_Number][3]),str(available_laptops))
            # Close file
            file.close()

            # Open file for writing
            file= open("stock.txt","w")
            # Write updated content
            file.write(quantity)
            # Close file
            file.close()

            print("\n\nDo you want to look for Another Laptops??")
            try:
                confirm= input("Enter (Y/y) for yes or (N/n) for no-->")
                
                if(confirm == "y") or (confirm == "Y"):
                    count+=1
                
                elif (confirm == "n") or (confirm == "N"):
                    break
                else:
                    print("-----------Input is Invalid--------")

            except:
                print("-----------Please input as instructed--------")

    while True:
        print ("\n\nDo you want me to print the invoice bill  ??\n")

        try:
                bill=input("Enter (Y/y) for yes or (N/n) for no-->")
                if (bill=="Y")or(bill=="y"):
                    # Generatring rent invoice
                    Date = date()
                    Time = time()
                    selling_bill(name,Date, Time, address,contact, sold_Laptops)
                    break

                elif(bill=="N")or(bill=="n"):
                     print("Printing bill is necessary, So please print the bill")
                else:
                    print("-----------Please Input  as Valid--------")
        except:
                print("-----------Please input  Instructed--------")
    

       





