////////////////////////////////////////////////////////
/// 
/// take string from user and covert to camel case
/// technically this is going to edit the string
/// 
/// Input : my name is Amit
/// output : My Name Is Amit 
/// 
/// Input : my NAME is AmIt
/// output : My Name Is Amit 
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program741
{
    public static void main(String A[])
    {
        Scanner sobj = new Scanner(System.in);

        System.out.println("Enter String :");

        String str = sobj.nextLine();
        
        str = str.trim();

        str = str.replaceAll("\\s+", " ");

        str = str.toLowerCase();

        System.out.println(str);

        // String Tokens[] = str.split(" ");

        // for (int i = 0; i <= Tokens.length; i++ )
        // {

        // }
        // //pahile 2 byte array la convert kra

        char Arr[] = str.toCharArray();
        
        for(int i = 0; i < Arr.length; i++)
        {
            System.out.println(Arr[i]);
        }

        System.out.println(str);

        sobj.close();

    }

}