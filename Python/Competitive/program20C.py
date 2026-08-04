# Design a Python application that creates two threads named 
# EvenList and OddList.
# • Both threads should accept a list of integers as input.
# • The EvenList thread should:
# ◦ Extract all even elements from the list.
# ◦ Calculate and display their sum.
# • The OddList thread should:
# ◦ Extract all odd elements from the list.
# ◦ Calculate and display their sum.
# • Threads should run concurrently.

import threading
from functools import reduce

def EvenFunction(RawList):
    FilteredEvenList = (list(filter(lambda x : x if x % 2 == 0 else 0,RawList)))

    DataAfterReduce = int(reduce(lambda x,sum: x + sum,FilteredEvenList))

    print(DataAfterReduce)

def OddFunction(RawList):
    FilteredOddList = (list(filter(lambda x : x if x % 2 == 1 else 0,RawList)))

    DataAfterReduce = int(reduce(lambda x,sum: x + sum,FilteredOddList))

    print(DataAfterReduce)

def main():

    nums = list()

    size_of_nums = int(input("Enter Size of list : "))

    for i in range(0,size_of_nums,1):
        no = int(input())
        nums.append(no)

    EvenList = threading.Thread(target = EvenFunction, args= (nums,))
    OddList = threading.Thread(target = OddFunction, args=(nums,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

if __name__ == "__main__":
    main()