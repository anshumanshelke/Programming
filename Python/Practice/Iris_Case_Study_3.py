# we'll make use of the Built-in function- lein()
# here, len() is a standalone function
# means there's NO need to create an object of any identifer

from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris Classification Case Study")
    print("-"*30)

    Dataset = load_iris()

    # MetaData of the dataset
    print("Independent Variables are : ")
    print(Dataset.feature_names)
    print("Length of independent variable : ",len(Dataset.feature_names))

    print("Dependent Variables are : ")
    print(Dataset.target_names)
    print("Length of dependent variable : ",len(Dataset.target_names))

    
if __name__ == "__main__":
    main()
