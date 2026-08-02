#####################################################
#
# Write a program which accepts radius of circle
# and prints area of circle.
#
####################################################
def PrintRange(No):
    Ans = No * 3.14
    return Ans
    

def main():

    Value = int(input("Enter Radius : "))

    Ret = PrintRange(Value)

    print("Area of Circle is : ",Ret)

if __name__ == "__main__":
    main()