function CheckEven(No)
{
    console.log("Normal If-Else condition")

    if(No % 2 == 0)
    {
        console.log("It is even number")
    }
    else
    {
        console.log("It is odd number")
    }
    
    console.log("-----------------------------------------------------------")
}

function main()
{
    let value = 11
    CheckEven(value)

    console.log("-----------------------------------------------------------")
    console.log("Ternary Operator")
    let result = value % 2 == 0 ? "Even" : "Odd"
    console.log(`Number ${value} is `,result)
}

main()