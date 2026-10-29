function Addition(Value1, Value2)
{
    return Value1 + Value2
}

function main()
{
    let no1 = 10;
    let no2 = 11;
    let Ans = 0;

    Ans = Addition(no1, no2)

    console.log(`Addition is of ${no1} & ${no2} is : `, Ans)
}

main()