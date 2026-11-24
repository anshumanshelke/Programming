# 2. Accept amount in US dollar and return its corresponding value in Indian currency.
# Consider 1$ as 70 rupees.
# Input :
# Output :10
# 700
# Input :
# Output :3
# 270
# Input :
# Output :1200
# 84000

def DolToInr(InrVal):
    DlrVal = InrVal * 70
    return DlrVal

def main():
    iValue = int(input("Enter Value is $ : "))

    if(iValue <= 0):
        iValue = -iValue

    Result = DolToInr(iValue)
    print("Value in Indian Ruppes is :",Result)


if __name__ == "__main__":
    main()