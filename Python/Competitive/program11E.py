#####################################################
# 5. Write a program which accepts one number
# and checks whether it is palindrome or not.
# Input: 121
# Output: Palindrome
#####################################################

def ReverseNum(No):

    temp = No
    RevNo = 0
    while(No >= 1): 
        Digit = No % 10

        RevNo = RevNo * 10
        RevNo = RevNo + Digit

        No = No // 10

    if(temp == RevNo):
        return True     #True- it's palindrome
    
    else:               #false- NOT palindrome
        return False
    

def main():
    print("Enter number : ")
    Value = int(input())
    Ret = ReverseNum(Value)

    if(Ret == True):
        print("NUmber is Palindrome")

    else:
        print("NOT a Palindrome Number")

if __name__ == "__main__":
    main()