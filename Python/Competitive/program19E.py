# 5.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce

def ChkPrime(No):
    for i in range (2,((No//2)+1),1):
        if No%(i) == 0:
            return
    return No

def IncrementByTwo(No):
    return (No * 2)

def Max(No1,No2):
    if(No1>No2):
        return No1
    return No2

def main():
    Arr = list()
    Size = int(input("Enter the size of array : "))

    for i in range (0,Size):
        no = int(input())
        Arr.append(no)

    print(Arr)

    Fdata = list(filter(ChkPrime,Arr))

    print(Fdata)

    Mdata = list(map(IncrementByTwo,Fdata))

    print(Mdata)

    Rdata = int(reduce(Max,Mdata))

    print(Rdata)

if __name__ == "__main__":
    main()