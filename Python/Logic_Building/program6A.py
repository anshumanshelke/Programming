# 1. Write a program which accept number from user and if number is less than 50
# then print small , if it is greater than 50 and less than 100 then print medium, if it is
# greater than 100 then print large.

def Number(Val):

    if(Val < 50):
        print("Small")

    elif((Val>= 50) and (Val<=100)):
        print("medium")

    else:
        print("large")


def main():
    Value = int(input("Enter number : "))

    Number(Value)

if __name__ == "__main__":
    main()