import random
import time

x = 1
y = 1
tryAgain = 1
againTest = 1
selectionBreak = False
menuRetry = 1

def addition(a, b):
    output = a + b
    print(output)

def subtraction(a, b):
    output = a - b
    print(output)

def multiplication(a, b):
    output = a * b
    print(output)

def division(a, b):
    output = a / b
    print(output)

def randint(a, b):
    output = random.randint(a, b)
    print(output)

while menuRetry == 1:

    print("----------Harley's Calculator----------")
    print()
    print("     1.Addition")
    print("     2.Subtraction")
    print("     3.Multiplication")
    print("     4.Division")
    print("     5.Random Number")
    print()

    while selectionBreak == False:
        try:
            selection = int(input("Which process would you like to do?: "))

            if selection > 5 or selection == 0:
                print('That number is not in the options list. Try Again!')

            else:
                selectionBreak = True     

        except ValueError:
            print("That's not a number try again!")
            print()

    ## Addition


    if selection == 1:

        menuRetry = 0
        tryAgain = 1

        while tryAgain == 1:

            x = 1
            y = 1
            tryAgain = 1
            againTest = 1
            selectionBreak = False


            while x == 1:
                print()
                print("----------Addition----------")
                print()
                num1 = input("Enter your first number: ")
                try:
                    num1 = float(num1)
                    x = x + 1
                    y = 1
                except ValueError:
                    print("That's not a number try again!")     

                
            while y == 1:         
                num2 = input("Enter your second number: ")
                try:
                    num2 = float(num2)
                    y = y + 1
                except  ValueError:
                        print("That's not a number try again!")
            print()
            print("Calculating...")
            time.sleep(3)
            addition(num1, num2)

            while againTest == 1:
                again = input("Type 'yes' to do addition again? Alternatively press 1 to return to the menu or 2 to exit: ")
                if again.lower() == 'yes' or again.lower() == 'y':
                    againTest = 0
                    tryAgain = 1
                    x = 1
                    y = 0
                    
                elif again == '2':
                    print()
                    print("End of calculator!")
                    againTest = 0
                    tryAgain = 0
                    menuRetry = 0

                elif again == '1':
                    menuRetry = 1
                    print()
                    print("Rebooting...")
                    print()
                    time.sleep(2)
                    againTest = 0
                    tryAgain = 0   
                      
                else:
                    print()
                    print('I do not understand try again!!')

#Subtraction

    if selection == 2:

            menuRetry = 0
            tryAgain = 1

            while tryAgain == 1:

                x = 1
                y = 1
                tryAgain = 1
                againTest = 1
                selectionBreak = False


                while x == 1:
                    print()
                    print("----------Subtraction----------")
                    print()
                    num1 = input("Enter your first number: ")
                    try:
                        num1 = float(num1)
                        x = x + 1
                        y = 1
                    except ValueError:
                        print("That's not a number try again!")     

                    
                while y == 1:         
                    num2 = input("Enter your second number: ")
                    try:
                        num2 = float(num2)
                        y = y + 1
                    except  ValueError:
                            print("That's not a number try again!")
                print()
                print("Calculating...")
                time.sleep(3)
                subtraction(num1, num2)

                while againTest == 1:
                    again = input("Type 'yes' to do subtraction again? Alternatively press 1 to return to the menu or 2 to exit: ")
                    if again.lower() == 'yes' or again.lower() == 'y':
                        againTest = 0
                        tryAgain = 1
                        x = 1
                        y = 0
                        
                    elif again == '2':
                        print()
                        print("End of calculator!")
                        againTest = 0
                        tryAgain = 0
                        menuRetry = 0

                    elif again == '1':
                        menuRetry = 1
                        print()
                        print("Rebooting...")
                        print()
                        time.sleep(2)
                        againTest = 0
                        tryAgain = 0   
                        
                    else:
                        print()
                        print('I do not understand try again!!')

    #Multiplication

    if selection == 3:

            menuRetry = 0
            tryAgain = 1

            while tryAgain == 1:

                x = 1
                y = 1
                tryAgain = 1
                againTest = 1
                selectionBreak = False


                while x == 1:
                    print()
                    print("----------Multiplication----------")
                    print()
                    num1 = input("Enter your first number: ")
                    try:
                        num1 = float(num1)
                        x = x + 1
                        y = 1
                    except ValueError:
                        print("That's not a number try again!")     

                    
                while y == 1:         
                    num2 = input("Enter your second number: ")
                    try:
                        num2 = float(num2)
                        y = y + 1
                    except  ValueError:
                            print("That's not a number try again!")
                print()
                print("Calculating...")
                time.sleep(3)
                multiplication(num1, num2)

                while againTest == 1:
                    again = input("Type 'yes' to do multiplication again? Alternatively press 1 to return to the menu or 2 to exit: ")
                    if again.lower() == 'yes' or again.lower() == 'y':
                        againTest = 0
                        tryAgain = 1
                        x = 1
                        y = 0
                        
                    elif again == '2':
                        print()
                        print("End of calculator!")
                        againTest = 0
                        tryAgain = 0
                        menuRetry = 0

                    elif again == '1':
                        menuRetry = 1
                        print()
                        print("Rebooting...")
                        print()
                        time.sleep(2)
                        againTest = 0
                        tryAgain = 0   
                        
                    else:
                        print()
                        print('I do not understand try again!!')

    #Division

    if selection == 4:

            menuRetry = 0
            tryAgain = 1

            while tryAgain == 1:

                x = 1
                y = 1
                tryAgain = 1
                againTest = 1
                selectionBreak = False


                while x == 1:
                    print()
                    print("----------Division----------")
                    print()
                    num1 = input("Enter your first number: ")
                    try:
                        num1 = float(num1)
                        x = x + 1
                        y = 1
                    except ValueError:
                        print("That's not a number try again!")     

                    
                while y == 1:         
                    num2 = input("Enter your second number: ")
                    try:
                        num2 = float(num2)
                        y = y + 1
                    except  ValueError:
                            print("That's not a number try again!")
                print()
                print("Calculating...")
                time.sleep(3)
                division(num1, num2)

                while againTest == 1:
                    again = input("Type 'yes' to do division again? Alternatively press 1 to return to the menu or 2 to exit: ")
                    if again.lower() == 'yes' or again.lower() == 'y':
                        againTest = 0
                        tryAgain = 1
                        x = 1
                        y = 0
                        
                    elif again == '2':
                        print()
                        print("End of calculator!")
                        againTest = 0
                        tryAgain = 0
                        menuRetry = 0

                    elif again == '1':
                        menuRetry = 1
                        print()
                        print("Rebooting...")
                        print()
                        time.sleep(2)
                        againTest = 0
                        tryAgain = 0   
                        
                    else:
                        print()
                        print('I do not understand try again!!')

    #Randint

    if selection == 5:

            menuRetry = 0
            tryAgain = 1

            while tryAgain == 1:

                x = 1
                y = 1
                tryAgain = 1
                againTest = 1
                selectionBreak = False


                while x == 1:
                    print()
                    print("----------Random Number Generator----------")
                    print()
                    num1 = input("What is the highest you would like the random number to be? : ")
                    try:
                        num1 = int(num1)
                        x = x + 1
                        y = 1
                    except ValueError:
                        print("That's not a whole number try again!")     

                    
                while y == 1:         
                    num2 = input('What is the lowest number you would like the number to be? : ')
                    try:
                        num2 = int(num2)
                        y = y + 1
                    except  ValueError:
                            print("That's not a whole number try again!")
                print()
                print("Calculating...")
                time.sleep(3)
                randint(num1, num2)

                while againTest == 1:
                    again = input("Type 'yes' to do a random number again? Alternatively press 1 to return to the menu or 2 to exit: ")
                    if again.lower() == 'yes' or again.lower() == 'y':
                        againTest = 0
                        tryAgain = 1
                        x = 1
                        y = 0
                        
                    elif again == '2':
                        print()
                        print("End of calculator!")
                        againTest = 0
                        tryAgain = 0
                        menuRetry = 0

                    elif again == '1':
                        menuRetry = 1
                        print()
                        print("Rebooting...")
                        print()
                        time.sleep(2)
                        againTest = 0
                        tryAgain = 0   
                        
                    else:
                        print()
                        print('I do not understand try again!!')                                                                
        
        

        
                                       

                 

                 
                                              
                 
                                                                                                                  
                         
          
     

