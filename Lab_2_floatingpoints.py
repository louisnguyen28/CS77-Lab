"""""
This program converts floating point numbers into the simplified IEEE 754 format. 
This program is by: Louis Nguyen, Thuan Tham lam, Ian Ramin
Using the simple model, MSB is sign, 5 bits for exponenent, 8 bits for significand. This means bias is 15 or 2^(n-1)-1
Run this with a positive nad negative
Make sure to check for errors. Input will be a string representing a floating point number
"""
import Lab_1_conversion

BIAS = 15

def getInput()-> str:
    return input("Please enter in a floating point number: ")


def isValid(value)-> bool:    
    #check for only one period, check for only one -
    #make sure no alphabetical letters
    print("Checking validity...")
    period = 0
    dash = 0
    for i in value:
        if i == '.':
            period += 1
        elif i == '-':
            dash += 1
        if i not in "-.1234567890":
            return False
    #WE ARE EXPECTING FLOATING POINT INPUT 5 IS NOT A FLOATING POINT 5. IS AND 5.0 IS FLOATING POINT

    return period == 1 and dash <= 1

def getSign(value)-> str:
    if value[0] == '-':
        return '1'
    else:
        return '0'
    
def toBin(value: str) -> int:
    return Lab_1_conversion.hexToBin(Lab_1_conversion.decToHex(value))

def countExponent(binary: str)-> int:
    return binary.index('.')+BIAS

def getExponent(binary: str)-> str:
    exponent = str(countExponent(binary)) + '.0'
    exponentBin = toBin(exponent)
    #print(exponentBin)
    return exponentBin
        
def sizeCheckAndCorrect(bin: str, size: int):
    if len(bin)<size:
        bin = "0"*(size-len(bin)) + bin
    return bin
    
def toSimple(value, sign):
    if sign == '0':
        #POSITIVE WORKFLOW
        bin = toBin(value)
        exponentBin = getExponent(bin).replace(".", "")
        bin = bin.rstrip("0").replace(".", "")
        exponentBin = exponentBin.rstrip("0")
        exponentBin = sizeCheckAndCorrect(exponentBin, 5)
        bin = sizeCheckAndCorrect(bin, 8)
    elif sign == '1':
        value = value[1:]
        bin = toBin(value)
        exponentBin = getExponent(bin).replace(".", "")
        bin = bin.rstrip("0").replace(".", "")
        exponentBin = exponentBin.rstrip("0")
        exponentBin = sizeCheckAndCorrect(exponentBin, 5)
        bin = sizeCheckAndCorrect(bin, 8)
        
    #CHANGE THE RETURN TO MAKE SENSE LATER
    print( sign + " is the sign bit " + exponentBin.replace(".","") +" is the exponent " + bin[0:8].replace(".", "") + " is the mantessa.")
    return sign + exponentBin + bin[0:7]
    
    
def main():
    while True:
        value = getInput()
        if isValid(value):
            print ("Valid input")
            break
        else: 
            print("Invalid input, please try again")
    #We now have checked for validity. Lets set two workflows, one for positive and one for negative
    sign = getSign(value)
    if value[-1] == '.':
        value += '0'
    #Next we have to check our exponent. For this we use 5 bits to represent. The bias is 2^(n-1)-1
    #To get the value of the bias, we have to first convert the number from float to binary. Does the sign matter at this point? We just convert it like a regular number
    #We can reuse or dec to bin function from the previous lab
    
    simple = toSimple(value, sign).replace(".", "")
    print(simple)
    
    
        
    
if __name__ == "__main__":
    main()