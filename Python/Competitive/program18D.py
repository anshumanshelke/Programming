# 4.Write a program which accept N numbers from user and
# store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

from functools import reduce

def FindFreq(No1, No2):
    Count = 0
    if No1 == No2:
        Count = Count + 1
    return Count

def main():
    Size = 0
    Arr = list()

    target = int(input("Enter the Number you want to know frequency of"))

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    print(Arr)

    RData = reduce(FindFreq,target,Arr)

    print("Maximum of the given elements is : ",RData)
    
if __name__ == "__main__":
    main()