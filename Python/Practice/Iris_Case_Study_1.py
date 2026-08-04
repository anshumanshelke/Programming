#sklearn is a toy case study- which is inbuilt in the sklearn module
#the complete dataset of iris Case study is saved into the variable named Dataset 
#when the dataset is printed- using the print function- we can see the dataset on console
#but since it's been transfered from the .cvs file- it's not representable on the console

from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris classification Case study")
    print("-"*30)

    Dataset = load_iris()

    print(Dataset)

if __name__ == "__main__":
    main()