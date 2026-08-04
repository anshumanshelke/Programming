# 4: Design a Python application that creates three threads named Small, Capital, and
# Digits.
# • All threads should accept a string as input.
# • The Small thread should count and display the number of lowercase characters.
# • The Capital thread should count and display the number of uppercase characters.
# • The Digits thread should count and display the number of numeric digits.
# • Each thread must also display:
# ◦ Thread ID
# ◦ Thread Name

import threading

def CountSmall(sentence):
    Count = 0
    for i in sentence:
        if((i>='a') and (i<='z')):
            Count = Count + 1
    print("No. of Small Cased letter : ",Count)

    threading.current_thread().name   # inside EvenFunction -> "EvenList"

def CountBig(sentence):
    Count = 0
    for i in sentence:
        if((i>='A') and (i<='Z')):
            Count = Count + 1
    print("No. of Capital Cased letter : ",Count)

def CountDigits(sentence):
    Count = 0
    for i in sentence:
        if((i>='0') and (i<='9')):
            Count = Count + 1
    print("No. of Digits : ",Count)


def main():
    StringX = str(input("Enter String : "))

    Small = threading.Thread(target = CountSmall, args= (StringX,))
    Capital = threading.Thread(target = CountBig, args= (StringX,))
    Digit = threading.Thread(target = CountDigits, args= (StringX,))

    Small.start()
    Capital.start()
    Digit.start()

    Small.join()
    Capital.join()
    Digit.join()

if __name__ == "__main__":
    main()