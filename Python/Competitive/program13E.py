#####################################################
#
# 5. Write a program which accepts marks and
# displays grade condition 
# Example:
# Marks ≥ 75 → Distinction
# Marks ≥ 60 → First Class
# Marks ≥ 50 → Second Class
# Marks < 50 → Fail
#
####################################################

def DisplayGrade(No):

    if(No < 0):
        print("Invalid Input")
        return

    if(No >= 75):
        print("Distinction")
    elif(No < 75 and No>=65):
        print("First Class")
    elif(No < 65 and No>=50):
        print("Second Class")
    else:
        print("Fail")

def main():

    Value = int(input("Enter Number : "))

    DisplayGrade(Value)

if __name__ == "__main__":
    main()