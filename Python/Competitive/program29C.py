# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through
# command line arguments, creates a new file named Demo.txt,
# and copies all contents from the given file into Demo.txt.

# Input (Command Line):
# ABC.txt

# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

def main():
    FileToOpen= str(input("Enter file name : "))
    fobj1 = open(FileToOpen,"r")
    Data = str(fobj1.read())
    print(Data)

    fobj2 = ("Demo.txt","r")

    fobj2.write(Data)


    
if __name__ == "__main__":
    main()