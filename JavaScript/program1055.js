
function main()
{
    let value = "My name is Raj"
    console.log(value.length,"Space is counted") //14
    console.log(value.charAt(0))     //M
    console.log(value.charCodeAt(0))  //77
    console.log(value.codePointAt(11))  //82
    console.log(value.at(4))            //a
    console.log(value[4])               //a
    console.log(value.at(-6))          //i
    ret = value.charAt(value.length-5)
    console.log(ret)                  //s
}

main()