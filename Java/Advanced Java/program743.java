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
/// Sting -> Array -> update -> output as string
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program743
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

        char Arr[] = str.toCharArray();
        
        if(Arr[0] >= 'a' && Arr[0] <= 'z')
        {
            Arr[0] = (char)(Arr[0] - 32);
        }

        for(int i = 0; i < Arr.length; i++)
        {
            if(Arr[i] == ' ')
            {
                if(Arr[i+1] >= 'a' && Arr[i+1] <= 'z')
                {
                    Arr[i+1] = (char)(Arr[i+1] - 32);
                }
            }
        }

        String output = new String(Arr);

        System.out.println("Updated string is : "+output);

        sobj.close();

    }

}