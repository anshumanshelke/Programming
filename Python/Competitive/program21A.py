# 1: Design a Python application that creates two threads named 
# Prime and NonPrime.
# • Both threads should accept a list of integers.
# • The Prime thread should display all prime numbers from the list.
# • The NonPrime thread should display all non-prime numbers from the list.

import threading

def DisplayPrime(ListOfInt):
    ListOfPrime = list()
    for ElementOfList in ListOfInt:
        flag = False
        for i in range(2,(ElementOfList // 2)+1,1):
            if(ElementOfList % i == 0):
                flag = True

        if(flag == False):
                ListOfPrime.append(ElementOfList)

    print("Prime elemets are :",ListOfPrime)

def DisplayNonPrime(ListOfInt):
    ListOfNonPrime = list()
    for ElementOfList in ListOfInt:
        for i in range(2,(ElementOfList // 2)+1,1):
            if(ElementOfList % i == 0):
                ListOfNonPrime.append(ElementOfList)
                break

    print("Non Prime elemets are :",ListOfNonPrime)
    
                

def main():
    nums = list()

    Size = int(input("Enter the number of elemets : "))

    print(f"Enter {Size} elemets : ")
    for i in range(0,Size,1):
        no = int(input())
        nums.append(no)

    print("Given list is : ",nums)

    Prime = threading.Thread(target = DisplayPrime, args= (nums,))
    NonPrime = threading.Thread(target = DisplayNonPrime, args= (nums,))

    Prime.start()
    NonPrime.start()

    Prime.join()
    NonPrime.join()

if __name__ == "__main__":
    main()