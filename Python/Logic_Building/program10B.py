# 2. Write a program which accept width & height of rectangle from user and calculate
# its area. (Area = Width * Height)
# Input :
# Output :
# 5.3 9.78
# 51.834
# #include<stdio.h>
# double RectArea(float fWidth, float fHeight)
# {
# // Logic
# }
# int main()
# {
# float fValue1 = 0.0, fValue2 = 0.0;
# double dRet = 0.0;
# printf(" Enter width");
# scanf("% f ",&fValue1);
# printf("Enter height");
# scanf("%f",&fValue2);
# dRet = RectArea(fValue1, fValue2);
# printf("________");
# return 0;
# }



def RectArea(fHeight, fWidth):
    Area = float(0.0)
    Area = fWidth * fHeight
    return Area

def main():
    value1 = float(input("Enter Height of Rectangle :"))
    value2 = float(input("Enter Width of Rectangle :"))
    Result = RectArea(value1,value2)

    print(f"Area of Rectangle is {Result}")

if __name__ == "__main__":
    main()