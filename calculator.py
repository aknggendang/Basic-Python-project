#Alfaizi Ahmad Zahran (Akanggendang)
#20210920
#Basic Calculator
#Python


from time import sleep



while True:
    #simple question (optional)
    ans = input("\nHi There,This is a python calculator,do you wanna try it?(y/n)")

    if ans == 'y':
        print("\nOke there you go.......")      
        sleep(5)                              
    else :
        print("Oooh.oke have a nice day")
        quit()    

    
    
    num1 = int(input("input the first number : "))
    op = input("Choose an operator [+,-,x,/]:")    
    num2 = int(input("Input The second number  : "))             
   
    #for decimal number you can use Float data type

    if op == '+':
        print("\nresult = ",num1 + num2)
    elif op == '-':
        print("\nresult = ",num1-num2)                       #Basic else if statement
    elif op == 'x':
        print("\nresult = ",num1*num2)
    elif op == '/':
        print("\nresult = ",num1/num2)
    else:
        print("\nError input")    #Error Message (Optional)



















    


    


