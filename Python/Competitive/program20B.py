# 2: Design a Python application that creates two threads 
# named EvenFactor and OddFactor.
# • Both threads should accept one integer number as a parameter.
# 
# • The EvenFactor thread should:
# ◦ Identify all even factors of the given number.
# ◦ Calculate and display the sum of even factors.
# 
# • The OddFactor thread should:
# ◦ Identify all odd factors of the given number.
# ◦ Calculate and display the sum of odd factors.

import threading

def EvenFactor(No):
    Sum = 0
    for i in range(1,No+1,1):
        if((No%i == 0) and (i%2 == 0)):
            Sum = Sum + i

    print(Sum)

def OddFactor(No):
    Sum = 0
    for i in range(1,No+1,1):
        if((No%i == 0) and (i%2 == 1)):
            Sum = Sum + i

    print(Sum)

def main():

    EvenValue = int(input("Enter Value for Even Thread : "))
    OddValue = int(input("Enter Value for Odd Thread : "))


    EvenT = threading.Thread(target = EvenFactor, args= (EvenValue,))
    OddT = threading.Thread(target = OddFactor, args=(OddValue,))

    EvenT.start()
    OddT.start()


if __name__ == "__main__":
    main()