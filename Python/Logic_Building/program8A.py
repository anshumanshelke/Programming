# 1.Write a program which accept radius of circle from user and calculate its area.

# Consider value of PI as 3.14. (Area = PI * Radius * Radius)
# Input :5.3
# Output : 88.2026
# Input :10.4
# Output : 339.6224
# #include<stdio.h>
# double CircleArea(float fRadius)
# {
# // Logic
# }
# int main()
# {
# float fValue = 0.0;
# double dRet = 0.0;
# printf(" Enter radius");
# scanf("%f ",&fValue);
# dRet = CircleArea(fValue);
# printf("________");
# return 0;
# }

def CircleArea(No):
    Area = float(0.0)
    PI = float(3.14)
    Area = PI * No * No
    return Area

def main():
    value = float(input("Enter Radius Of Circle :"))
    Result = CircleArea(value)

    print(f"Area of Circle with radius {value} is {Result}")

if __name__ == "__main__":
    main()