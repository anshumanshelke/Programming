#####################################################
#
# Write a program which accepts length and
# width of rectangle and prints area.
# 
#####################################################
def PrintRange(No1, No2):
    Ans = No1 * No2
    return Ans
    

def main():

    Value1 = int(input("Enter Length : "))
    Value2 = int(input("Enter Width : "))

    Ret = PrintRange(Value1, Value2)

    print("Area of Rectangle : ",Ret)

if __name__ == "__main__":
    main()