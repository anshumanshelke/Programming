# 3. Write a program which accept distance in kilometre 
# and convert it into meter. (1
# kilometre = 1000 Meter)
# Input :
# Output :5
# 5000
# Input :
# Output :12
# 12000
# #include<stdio.h>
# int KMtoMeter(int iNo)
# {
# // Logic
# }
# int main()
# {
# int iValue = 0, iRet = 0;
# printf("Enter distance");
# scanf("%d ",&iValue1);
# iRet = KMtoMeter(iValue);
# printf("________");
# return 0;
# }

def KMtoMeter(No):

    ValInMtr = No * 1000
    
    return ValInMtr

def main():
    value1 = float(input("Enter Distance :"))
    Result = KMtoMeter(value1)

    print(f" {value1} Kms is {Result} meters")

if __name__ == "__main__":
    main()