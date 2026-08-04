#Ball classification case study

#here I've provided the Encoding  

# Rough -> 1 
# Smooth -> 2

# Tennis -> 1
# Cricket -> 0

def main():

    print("Ball Clasification Case study:")

    Features =  [[35,1],[47,1],[90,2],[48,1],[90,2],[35,1],
                [92,2],[35,1],[35,1],[35,1],[96,2],[43,1],
                [110,2],[35,1],[95,2]]

    Labels = [1,1,0,1,0,1,0,1,1,1, 0,1,0,1,0]

    print("Features are : ",Features)

    print("Labels are : ",Labels)

if __name__ == "__main__":
    main()