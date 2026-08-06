# Q2) Display File Contents

# Problem Statement:
# Write a program which accepts a file name from the user, 
# opens that file, and displays the entire contents on the
# console.

# Input:
# Demo.txt

# Expected Output:
# Display contents of Demo. txt on console.

def main():
    FileToOpen= str(input("Enter file name : "))
    fobj = open(FileToOpen,"r")
    Data = fobj.read()
    print(Data)
    
if __name__ == "__main__":
    main()