# Write a program which accept N numbers from user
# and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

from functools import reduce

def Maximum(No1, No2):
    if No1 > No2:
        return No1
    else:
        return No2  

def main():
    Size = 0
    Arr = list()

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    print(Arr)

    RData = reduce(Maximum,Arr)

    print("Maximum of the given elements is : ",RData)
    
if __name__ == "__main__":
    main()