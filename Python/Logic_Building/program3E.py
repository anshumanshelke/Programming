# 5. Accept on character from user or check whether that character is vowel
# (a,e,i,o,u) or not.
# Input : E Output : True
# Input : d Output : False

def Convert(Letter):

        if((Letter == 'a') or 
           (Letter == 'e') or
           (Letter == 'i') or
           (Letter == 'o') or
           (Letter == 'u')  ):   # ( a <-> z)
           return True

        elif((Letter == 'A') or 
           (Letter == 'E') or
           (Letter == 'I') or
           (Letter == 'O') or
           (Letter == 'U')  ):   # ( a <-> z)
           return True

        else:
            return False

def main():
    cChar = str(input("Enter Character : "))

    bRet = Convert(cChar)

    if(bRet == True):
        print("Given letter is Vowel")

    if(bRet == False):
        print("Given letter is Consonant")

if __name__ == "__main__":
    main()
    