#####################################################
# 1. Write a program which accepts one number
# and checks whether it is prime or not.
# Input: 11
# Output: Prime Number
#####################################################

def CheckPrime(No):

    if(No <= 1):
        return False

    for i in range(2,No):
        if(No % i == 0):
            return False
            
    return True

def main():
    print("Enter number : ")
    Value = int(input())
    Ret = CheckPrime(Value)

    if(Ret == True):
        print("Number is Prime")

    else:
        print("Number is NOT Prime")


if __name__ == "__main__":
    main()