# 1.Write a program which accept one number from user and print that number of
# even numbers on screen.
# Input :7
# Output:2 4 6 8 10 12 14

def main():
    Val1 = int(input("Enter number : "))

    if(Val1 <= 0):
        print("Invalid input, enterred number should be greater than ZERO")

    for i in range(1,Val1+1):
        print(i*2, end = " ")

if __name__ == "__main__":
    main()