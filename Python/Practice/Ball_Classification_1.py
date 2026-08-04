#Ball classification case study

#here a dataset is manually feed into the program
#as features we have- the wight of ball and the Surface info
#since it's supervised Learning model- there's labels
#As labels we've the labels named cricket and tennis

def main():
    Features =  [[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],[35,"Rough"],
                [92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],[96,"Smooth"],[43,"Rough"],
                [110,"Smooth"],[35,"Rough"],[95,"Smooth"]]

    Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket",
              "Tennis","Tennis","Tennis", "Cricket","Tennis","Cricket","Tennis","Cricket"]

    print(Features)

    print(Labels)

if __name__ == "__main__":
    main()