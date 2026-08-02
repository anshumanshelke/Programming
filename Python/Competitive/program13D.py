#####################################################
#
# Write a program which accepts one number and
# prints binary equivalent.
#
####################################################

def PrintBinary(No):
    Digit = 0
    Binary = ""

    while( No != 0):
        Digit = ( No % 2 )
        Binary = str(Digit) + Binary 
        No = No // 2

    print(Binary)
    
def main():

    Value = int(input("Enter Number : "))

    PrintBinary(Value)

if __name__ == "__main__":
    main()