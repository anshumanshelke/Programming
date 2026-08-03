# 10. Write a program which accept name from user 
# and display length of its name.
# Input : Marvellous Output : 10

def Count(word):
    return int(len(word))

def main():
    name = str(input("Enter Name : "))
    Ret = int(Count(name))
    print(Ret)

if __name__ == "__main__":
    main()