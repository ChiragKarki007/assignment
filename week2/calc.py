a = int(input("Enter the first number: \n"))
b = int(input("Enter the second number: \n"))

oper=int(input("What operation would you like to perform? \n \
        1.Addition\n \
        2.Subtraction\n \
        3.Multiplication\n \
        4.Division\n "))

add = a+b
sub = a-b
mul = a*b
div = a/b

if oper == 1:
    print("The sum is: ",add)

elif oper == 2:
    print("The difference is: ",sub)

elif oper == 3:
    print("The product is: ",mul)

elif oper == 4 :
    print("The division is: ",div)

else:
    print("Invalid option.")





            

