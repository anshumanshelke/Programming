#####################################################
#
# Write a program which accepts one number and 
# checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number
#
####################################################
def CheckPerfect(No):
    Sum = 0

    if(No < 1):
        print("Invalid Input, Retry")
        return

    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum + i

    if(Sum == No):
        return True   

    else:
        return False
    
def main():

    Value = int(input("Enter Number : "))

    Ret = CheckPerfect(Value)

    if(Ret == True):
        print(f"Yes, {Value} is a Perfect Number") 

    if(Ret == False):
        print(f"No, {Value} is NOT a Perfect Number") 

if __name__ == "__main__":
    main()