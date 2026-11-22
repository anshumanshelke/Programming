# 5. Write a program which accept number from user and display its table in reverse
# order.
# Input :
# Output :2
# 20 18 16 14 12 10 8 6 4 2

def Table(Val):
    if(Val < 0):
        Val = -Val

    for i in range(10,0,-1):
        print(i*Val,end = " ")
    print(" ")

def main():
    Value = int(input("Enter Number : "))

    Table(Value)

if __name__ == "__main__":
    main()