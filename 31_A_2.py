# -*- coding: utf-8 -*-
"""
Created on Sat May 22 12:09:40 2021

@author: Manodeep
"""

print("Choices:\n 1 - Binary integer to Decimal \n 2 - Decimal integer to Binary\n 3 - Binary fraction to Decimal \n 4 - Decimal fraction to Binary \n")

x = input("Please enter your choice: ")
 
x = int(x)
 
if(x==1):
    b_num = list(input("Input a binary integer number: "))
    value = 0

    for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
            value = value + pow(2, i)
    print("The decimal value of the number is", value)

elif(x==2):
    def decimalToBinary(num):
        """This function converts decimal number
        to binary and prints it"""
        if num > 1:
            decimalToBinary(num // 2)
        print(num % 2, end='')


    # decimal number
    number = int(input("Enter an integer decimal number: "))

    decimalToBinary(number)
    
elif(x==3):
    # of binary fractional to decimal conversion
    def binaryToDecimal(binary, length) :
        
        # Fetch the radix point
        point = binary.find('.')

        # Update point if not found
        if (point == -1) :
            point = length

        intDecimal = 0
        fracDecimal = 0
        twos = 1

        # Convert integral part of binary
        # to decimal equivalent
        for i in range(point-1, -1, -1) :
            
            # Subtract '0' to convert
            # character into integer
            intDecimal += ((ord(binary[i]) -
                            ord('0')) * twos)
            twos *= 2

        # Convert fractional part of binary
        # to decimal equivalent
        twos = 2
        
        for i in range(point + 1, length):
            
            fracDecimal += ((ord(binary[i]) -
                            ord('0')) / twos);
            twos *= 2.0

        # Add both integral and fractional part
        ans = intDecimal + fracDecimal
        
        return ans

    # Driver code :
    if __name__ == "__main__" :
        num = float(input("Enter a fraction binary number: "))
        n = str(num)
        print(binaryToDecimal(n, len(n)))

elif(x==4):
    def float_bin(number, places = 3):
  
    # split() seperates whole number and decimal 
    # part and stores it in two seperate variables
        whole, dec = str(number).split(".")

        # Convert both whole number and decimal  
        # part from string type to integer type
        whole = int(whole)
        dec = int (dec)

        # Convert the whole number part to it's
        # respective binary form and remove the
        # "0b" from it.
        res = bin(whole).lstrip("0b") + "."

        # Iterate the number of times, we want
        # the number of decimal places to be
        for x in range(places):

            # Multiply the decimal value by 2 
            # and seperate the whole number part
            # and decimal part
            whole, dec = str((decimal_converter(dec)) * 2).split(".")

            # Convert the decimal part
            # to integer again
            dec = int(dec)

            # Keep adding the integer parts 
            # receive to the result variable
            res += whole

        return res
  
        # Function converts the value passed as
        # parameter to it's decimal representation
    def decimal_converter(num): 
        while num > 1:
            num /= 10
        return num
    
    n = input("Enter a Decimal fraction : ")
    p = int(input("Enter the number of decimal places of the result : \n"))

    print(float_bin(n, places = p))

else:
    print("Wrong Choice")