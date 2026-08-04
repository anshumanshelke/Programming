# DecisionTreeClassifier() is the class- whose object is named model
# .fit() is the instance method that creates a pattern based on two arguements
# the first arguement is the list of Independent variables 
# the second arguement is the list of Dependent Variables 

from sklearn import tree

def main():

    print("Ball Clasification Case study:")

    Independent =  [[35,1],[47,1],[90,2],[48,1],[90,2],[35,1],
                [92,2],[35,1],[35,1],[35,1],[96,2],[43,1],
                [110,2]]
    # testing features : [[35,1],[95,2]]

    Dependent = [1,1,0,1,0,1,0,1,1,1,0,1,0]
    # testing label : [1,0]

    model = tree.DecisionTreeClassifier()

    model = model.fit(Independent,Dependent)

    Result = model.predict([[35,1],[95,2]])

    print("Predicted result of model is : ",Result)

if __name__ == "__main__":
    main()