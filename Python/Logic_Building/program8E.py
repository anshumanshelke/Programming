# 5. Write a program which accept area in square feet 
# and convert it into square
# meter. (1 square feet = 0.0929 Square meter)

# Input :
# Output :7
# 0.650321
# #include<stdio.h>
# double SquareMeter(int iValue)
# {
# // Logic
# }
# int main()
# {
# int iValue = 0;
# double dRet = 0.0;
# printf( " Enter area in square feet");
# scanf("%d ",&fValue);
# dRet = SquareMeter(iValue);
# printf("________");
# return 0;
# }

def FtToMtr(No):

    ValInSqMtr = No *  0.0929 
    
    return ValInSqMtr

def main():
    value1 = float(input("Enter Area (in Sq Ft) :"))
    Result = FtToMtr(value1)

    print(f" {value1} Sq Ft is {Result} Sq Mtr")

if __name__ == "__main__":
    main()