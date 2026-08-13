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

class program740
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

        sobj.close();

    }

}