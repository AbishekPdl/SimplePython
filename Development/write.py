def selling_bill(name,Date, Time, address,contact, sold_Laptops):
    invoice_name = name+"_Selling_Bill"
    A_Total=0
    file = open(invoice_name,"w")
    file.write("              __________________________________________________________________________________________________________________________________________________\n")
    file.write("                                     ________________________________AUTUMN__LAPTOP__GALLERY______________________________________\n\n")
    file.write("                                      -------------------------------------------------------------------------------------------   \n")
    file.write("                                      |  Pokhara   |   Gharipatan-07 |   Contact: 98********    |      Email-abishek@gmai     |         \n")
    file.write("                                      ----------------------------------------------------------------------------------------\n")
    file.write("                                       |                                      Selling Bill                                   |\n")
    file.write("                                     ------------------------------------------------------------------------------------------\n")
    file.write("                                                                                             sold Date : "+Date+"            \n")
    file.write("                                                                                             sold Time : "+Time+"            \n")
    file.write("                                      Customer Name       : "+name+"                                                           \n")
    file.write("                                      Customer Address    : "+address+"                                                       \n")
    file.write("                                      Customer Contact    : "+str(contact)+"                                                  \n")
    file.write("                                      ---------------------------------------------------------------------------------------\n\n")

    for items in range(len(sold_Laptops)):
        file.write("                                     Laptop name           :      "+str(sold_Laptops[items][0])+"                                \n")
        file.write("                                     Brand                  :      "+str(sold_Laptops[items][1])+"                                  \n")
        file.write("                                     Price                  :      "+"$"+str(sold_Laptops[items][2])+"                                 \n")
        file.write("                                     Processor              :      "+str(sold_Laptops[items][4])+"                                     \n")
        file.write("                                     Graphics               :      "+str(sold_Laptops[items][5])+"                                     \n")
        file.write("                                     Sold Quantity          :      "+str(sold_Laptops[items][6])+"                                      \n")
        Cost = ((sold_Laptops[items][2])*int(sold_Laptops[items][6]))
        file.write("\n                                                  ------>Total Cost : $"+str(Cost)+"<-----                                               \n")
        file.write("                                ----------------------------------------->laptop sold sucessfully>------------------------------- \n\n")
        A_Total+=Cost
    shipping_charge=20
    file.write("                                                          Fixed Shipping Charge :$"+str(shipping_charge)+"                                      \n")  
    Grand_Total=int(A_Total)+int(shipping_charge)
    file.write("                                   ------------------------------> Grand Total(including shipping) : $"+str(Grand_Total)+" <----------------------------------------\n\n")
    file.write("              __________________________________________________________________________________________________________________________________________________\n")
    file.close()

    #showing invoice in the shell
    file=open (invoice_name,"r")   
    print(file.read()) 
    file.close





def buying_bill(name,Date, Time, address,contact, buying_laptops):
    invoice_name = name+"_Purchase_Bill"
    a_Total=0
    file = open(invoice_name,"w")
    file.write("                          _________________________________________________________________________________________________________________\n")
    file.write("                                     ________________________________AUTUMN__LAPTOP__GALLERY___________________________________\n\n")
    file.write("                                      -------------------------------------------------------------------------------------------   \n")
    file.write("                                      |  Pokhara   |   Gharipatan-07 |   Contact: 98********    |      Email-abishek@gmai     |         \n")
    file.write("                                      --------------------------------------------------------------------------------------\n")
    file.write("                                       |                                      Purchase Bill                                 |\n")
    file.write("                                     ----------------------------------------------------------------------------------------\n")
    file.write("                                                                                             Purchase Date : "+Date+"            \n")
    file.write("                                                                                             Purchase Time : "+Time+"            \n")
    file.write("                                      Customer Name       : "+name+"                                                           \n")
    file.write("                                      Customer Address    : "+address+"                                                       \n")
    file.write("                                      Customer Contact    : "+str(contact)+"                                                  \n")
    file.write("                                      -------------------------------------------------------------------------------------\n\n")

    for items in range(len(buying_laptops)):
        file.write("                                     Laptop name            :      "+str(buying_laptops[items][0])+"                                     \n")
        file.write("                                     Brand                  :      "+str(buying_laptops[items][1])+"                                     \n")
        file.write("                                     Price                  :  "+"$"+str(buying_laptops[items][2])+"                                 \n")
        file.write("                                     Processor              :      "+str(buying_laptops[items][4])+"                                     \n")
        file.write("                                     Graphics               :      "+str(buying_laptops[items][5])+"                                     \n")
        file.write("                                     Purchase Quantity      :      "+str(buying_laptops[items][6])+"                                      \n")

        file.write("                                ----------------------------------------->laptop sold sucessfully>--------------------------- \n\n")
        Cost = ((buying_laptops[items][2])*int(buying_laptops[items][6]))
        file.write("\n                                                      ------>Total Cost : $"+str(Cost)+"<-----                                               \n")
        a_Total +=Cost
    vat =0.13
    Grand_Total= float(a_Total + (vat*a_Total))
    file.write("                                             ------------------> Total: $"+str(a_Total)+" <-----------------------\n\n")
    file.write("                                                               13% VAT Amount            \n")
    file.write("                                  -------------------> Grand Total(including VAT ) : $"+str(Grand_Total)+" <---------------------\n\n")
    file.write("              ________________________________________________________________________________________________________________________________\n")
    file.close()

    #showing invoice in the shell
    file= open (invoice_name,"r")
    print(file.read())
    file.close()
