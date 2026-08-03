# 5.Write a program which accept N numbers from user and store it into List.
# Return addition of all prime numbers from that List.
# Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5)

from MarvellousNum import ChkPrime
from functools import reduce

Addition=lambda No1,No2:No1+No2
    
def main():
    print("Enter number of elements:")
    Value=int(input())

    Result=[]

    print("Enter Elements : ")
    for i in range(Value):
        no = int(input())
        Result.append(no)

    print(Result)

    ListPrime=filter(ChkPrime,Result)
    print(ListPrime)
    
    #Ret=reduce(Addition,ListPrime)
    #print(Ret)

if __name__ == "__main__":
    main()