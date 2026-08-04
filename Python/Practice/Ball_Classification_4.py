#tree (submodule) from the sklearn module is imported

from sklearn import tree

def main():

    print("Ball Clasification Case study:")

    Independent =  [[35,1],[47,1],[90,2],[48,1],[90,2],[35,1],
                [92,2],[35,1],[35,1],[35,1],[96,2],[43,1],
                [110,2],[35,1],[95,2]]

    Dependent = [1,1,0,1,0,1,0,1,1,1, 0,1,0,1,0]

    print("Independent Variables are : ",Independent)

    print("Dependent variables are : ",Dependent)

if __name__ == "__main__":
    main()