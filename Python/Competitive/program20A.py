# Design a Python application that creates two separate threads
# named Even and Odd.
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module.
# • Ensure proper thread creation and execution.

import threading

def EvenF():
    for i in range(2,21,2):
        print(i,end=" ")
    print("")

def OddF():
    for i in range(1,20,2):
        print(i,end=" ")
    print("")

def main():
    EvenT = threading.Thread(target = EvenF)
    OddT = threading.Thread(target = OddF)

    EvenT.start()
    OddT.start()


if __name__ == "__main__":
    main()