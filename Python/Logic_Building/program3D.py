# 4. Accept one character from user and convert case of that character.
# Input : a     Output : A
# Input : D     Output : d

# using ord() and chr() function

def Convert(Letter):
        CharToAci = ((ord(Letter)))     # convert str -> ASCII

        if((CharToAci >= 97) and (CharToAci <= 122)):   # ( a <-> z)
            CharToAci = CharToAci - 32
            print(chr(CharToAci))

        elif((CharToAci >= 65) and (CharToAci <= 90)):   # ( A <-> Z)
            CharToAci = CharToAci + 32
            print(chr(CharToAci))

def main():
    cChar = str(input("Enter Character : "))

    Convert(cChar)


if __name__ == "__main__":
    main()
    