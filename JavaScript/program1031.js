function CheckEven(No)
{
    if (No % 2 == 0)
    {   
        return true
    }
    
    else
    {
        return false
    }
}

function main()
{
    let Value = 11

    let bRet = false

    bRet = CheckEven(Value)
    bRet = CheckEven(Value)

    if (bRet == true)
    {   
    console.log("Its is even number")
    }
    
    else
    {
        console.log("Its is Odd number")
    }
}

main()