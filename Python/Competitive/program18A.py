# Write a program which accept N numbers from user 
# and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

from functools import reduce

def SumOfAll(No1, No2):
    return No1 + No2    

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

    RData = reduce(SumOfAll,Arr)

    print("Sum of given elements : ",RData)
    
if __name__ == "__main__":
    main()