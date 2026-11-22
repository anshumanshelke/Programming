# 2. Accept single digit number from user and print it into word.
# Input : 9
# Output : Nine
# Input : -3
# Output : Three
# Input : 12
# Output : Invalid Number

def Number(Val):

    if(Val < 0):
        Val = -Val
    
    if(Val >= 10):
        print("Invalid Input")

    words = ["Zero","One","Two","Three" ,"Four","Five","Six","Seven","Eight","Nine"]

    for i,value in enumerate(words):
        if(i == Val):
            print(value)

def main():
    Value = int(input("Enter number : "))
      
    Number(Value)

if __name__ == "__main__":
    main()