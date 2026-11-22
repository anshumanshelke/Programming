# 4.Write a program which accept number from user and display its table.
# Input :
# Output :2
# 2 4 6 8 10 12 14 16 18 20

def Table(Val):
    if(Val < 0):
        Val = -Val

    for i in range(1,11):
        print(i*Val,end = " ")
    print(" ")

def main():
    Value = int(input("Enter Number : "))

    Table(Value)

if __name__ == "__main__":
    main()