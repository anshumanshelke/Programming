# 9. Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20

def Display(No):
    for i in range(1,No+1):
        print(i * 2)

def main():
    Value = int(input("Enter Number : "))
    Display(Value)

if __name__ == "__main__":
    main()