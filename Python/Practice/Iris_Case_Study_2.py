# feature_names is an attribute of object named Dataset
# since Dataset is a identifier to an object (python is object oriented lang)
# feature_names - gives the shared independent variables names
# target_names - gives the shared dependent variable names

from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris classification Case study")
    print("-"*30)

    Dataset = load_iris()

    # MetaData of the dataset 
    print("Independent Variables are : ")
    print(Dataset.feature_names)

    print("Dependent Variables are : ")
    print(Dataset.target_names)


if __name__ == "__main__":
    main()
