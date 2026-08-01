#####################################################
# 4. Write a program which accepts one number
# and prints reverse of that number.
# Input: 123
# Output: 321
#####################################################

def ReverseNum(No):
    RevNo = 0
    while(No >= 1): 
        Digit = No % 10

        RevNo = RevNo * 10
        RevNo = RevNo + Digit

        No = No // 10

    return RevNo

def main():
    print("Enter number : ")
    Value = int(input())
    Ret = ReverseNum(Value)

    print(Ret)

if __name__ == "__main__":
    main()