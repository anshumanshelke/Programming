#####################################################
#
# 3. Write a program which accepts two numbers 
# and prints addition, subtraction multiplication and division.
#
#####################################################

def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    return Ans

def Substraction(No1, No2):
    Ans = 0
    Ans = No1 - No2
    return Ans

def Division(No1, No2):
    Ans = 0
    Ans = No1 / No2
    return Ans
    
def Multiplication(No1, No2):
    Ans = 0
    Ans = No1 * No2
    return Ans

def main():
    Ret = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter Second number : "))

    Ret = Addition(Value1, Value2)
    print("Addition is : ",Ret)

    Ret = Substraction(Value1, Value2)
    print("Differnce is : ",Ret)

    Ret = Multiplication(Value1, Value2)
    print("Product of Multiplication is : ",Ret)

    Ret = Division(Value1, Value2)
    print("Product of Division is : ",Ret)

if __name__ == "__main__":
    main()