"""CS-77 Spring Lab 1
    Group 6 members: Louis Nguyen, Thuan Thanh Lam, Ian Ramin
    The purpose of this program is to take an value(String) in the format of either Binary or Decimal(specified), value check, and then translate it to the other 3 formats
    
"""

def isValid(value: str, type: str)-> bool:
    #Decimal is 0-9, Bin is 0-1
    if type not in "BD":
        return False
    if type == "D":
        for i in value:
            if i not in "0123456789":
                return False
    elif type == "B":
        for i in value:
            if i not in "01":
                return False
    else:
        return True           
    
def decToBin(value: str)-> str:
    pass
    
def binToDec(value: str)-> str:
    pass

def binToHex(value: str)-> str:
    #Translate Hex/Bin table
    pass
    
def binToOct(value: str)-> str:
    #Translate Oct/Bin table
    pass

def main():
    """"
    The logic in here will be to take a String value, ask which form it is in(Decimal/Binary), error check, and translate to the other three formats
    If not in the right format, loop until it is. 
    """""
    while True:
        valid = False
        while valid == False:
            value = input("Please enter a string: ")
            valueType = input("Please specify [D]ecimal or [B]inary: ").upper() #Do we need to add error checking for here?
            print("Checking for validity")
            valid = isValid(value, valueType)
            if not valid:
                print("Not valid input. Try again")
        
        if valueType == "D":
        #The Decimal -> BHO flow goes here. We want to use Dec to Bin then the other functions.
            bin = decToBin(value)
            print(bin)
            print(binToHex(bin))
            print(binToOct(bin))
        else:
        #The Binary -> DHO flow goes here
            print(binToDec(value))
            print(binToHex(value))
            print(binToOct(value))
        
        #Ask for a loop
        repeat = value("Do you want to continue? Y/N: ")
        if repeat == "N":
            break


main()
    