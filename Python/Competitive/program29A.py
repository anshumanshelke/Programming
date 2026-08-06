# Q1) Check File Exists in Current Directory

# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current
# directory or not.

# Input:
# Demo.txt

# Expected Output:
# Display whether Demo. txt exists or not.

import os

def main():
    FileToFind = str(input("Enter file name : "))
    
    flag = False

    for FolderName , SubFolder , FileName in os.walk("Marvellous"):
        for fname in FileName:
            if(fname == FileToFind):
                flag = True
                break
            
    if(flag==True):
        print("File Exist")
    else:
        print("File DON'T exist")


if __name__ == "__main__":
    main()