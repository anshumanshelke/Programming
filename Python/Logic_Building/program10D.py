# 4. Write a program which accept temperature in Fahrenheit and convert it into
# celsius. (1 celsius = (Fahrenheit -32) * (5/9))
# Input :
# Output :10
# -12.2222 (
# 10 - 32) * (5/9)
# Input :
# Output :34
# 1.11111
# (34 - 32) * (5/9)

def CelToFahren(No):

    CelTemp = (No -32) * (5/9)
    return CelTemp

def main():
    value1 = float(input("Enter Temperature :"))
    Result = CelToFahren(value1)

    print(f" {value1} degree Fahrenheit is {Result} degree Celcius")

if __name__ == "__main__":
    main()