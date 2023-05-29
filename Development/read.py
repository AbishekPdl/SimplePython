def Read_Stocks():
  #opening stock.txt file and reading all the lines 
  file  = open('stock.txt','r')
  lines = file.readlines()

  data = []
# stripping and splitting the lines in txt file to store in a list
  for line in lines:
    line  =line.rstrip('\n') #end to end() 
    line  = line.split(", ")# to seprate()/any position replace (to remove) converted into list            
    data.append(line)
  
  # converting string into int and float   
  for m in range(len(data)):
    data[m][3] = int(data[m][3])
    data[m][2] = data[m][2].replace("$","")
    data[m][2] = float(data[m][2])
    
  file.close()
  return data


def show_stock():
  # storing above function in a variable
  stock = Read_Stocks()

#  table design  to show all the laptops stored in our gallery 
  print("*********************************************************************************************************************************************************************************")
  print("|                                                                           Available Laptops                                                                                   |")
  print("*********************************************************************************************************************************************************************************")
  print("")
  print("+------+------------------+-------------------------------+------------------+-------------------+---------------------------------+--------------------------------------------+")
  print("| S.N  |   Laptop Name    |            Brand              |     Price($)     |  Available Stock  |            Processor            |                 Graphics                   |")
  print("+------+------------------+-------------------------------+------------------+-------------------+---------------------------------+--------------------------------------------+")

# converting into string 
  for m in range(len(stock)):
    stock[m][3] = str(stock[m][3])
    stock[m][2] = str(stock[m][2])


#  making the table formate and giving the space in them
  count = 0
  for item in range (len(stock)):
    print("| ",count," ","|"," ",stock[item][0]," "*(13-len(stock[item][0])),"|",
      " "*5,stock[item][1]," "*(22-len(stock[item][1])),"|",
      " "*5,stock[item][2]," "*(9-(len(stock[item][2]))),"|",
      " "*5,stock[item][3]," "*(10-len(stock[item][3])),"|",
      " "*5,stock[item][4]," "*(24-len(stock[item][4])),"|",
      " "*5,stock[item][5]," "*(35-len(stock[item][5])),"|"
      )
    print("+------+------------------+-------------------------------+------------------+-------------------+---------------------------------+--------------------------------------------+")
    count+=1 
