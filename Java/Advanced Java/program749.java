////////////////////////////////////////////////////////
/// 
/// input = my name is Amit school name is abhinav city name is pune
/// 
/// output = 3, i.e. 'name' this word is 3 times 
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program749
{
    public static void main(String A[])
    {
        Scanner sobj = new Scanner(System.in);

        System.out.println("Enter String :");
        String str = sobj.nextLine();
    
        str = str.trim();

        str = str.replaceAll("\\s+", " ");

        String Tokens[] = str.split(" ");

        int iCount = 0;

        for(int i = 0; i < Tokens.length; i++)
        {
            

            if(Tokens[i].equals("name"))
            {
                iCount ++;
            }
        }

        System.out.println("Frequency of word is : "+iCount);

        sobj.close();

    }

}