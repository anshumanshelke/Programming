# 2: Design a Python application that creates two threads.
# • Thread 1 should calculate and display the maximum element from an list.
# • Thread 2 should calculate and display the minimum element from the same list.
# • The list should be accepted from the user.

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