#######################################################
# 3. Write a program which accepts one number 
# and prints factorial of that number.
# Input: 5
# Output: 120
#######################################################

def ProductOfNo(No):
    Product = 1
    for i in range(1,(No+1)):
        Product = Product * i

    return Product

def main():
    print("Enter number : ")
    Value = int(input())
    Ret = ProductOfNo(Value)

    print(Ret)

if __name__ == "__main__":
    main()