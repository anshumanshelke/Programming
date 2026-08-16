////////////////////////////////////////////////////////
/// 
/// 
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program755    
{
    public static void main(String A[])
    {
        int i = 0;
        int iMax = 0;

        Scanner sobj = new Scanner(System.in);

        System.out.println("Enter String :");
        String str = sobj.nextLine();
    
        str = str.trim();

        str = str.replaceAll("\\s+", " ");

        str = str.toLowerCase();

        char Arr[] = str.toCharArray();

        int Frequency[] = new int[26];

        // for(i=0; i < Frequency.length; i++)
        // {
        //     Frequency[i] = 0;
        // }

        // a    b   c   d
        //  97  98  99  100
        //  0   1   2   3

        for(i=0; i < Arr.length; i++)
        {
            if(Arr[i] >= 'a' && Arr[i] <= 'z')
            {
                Frequency[(int)Arr[i]-97]++;
            }
        }

        char ch = '\0';
        System.out.println("Frequency of each letter is : ");
        
        for(i = 0; i < Frequency.length; i++)
        {
            if(Frequency[i] > 0)
            {
                System.out.println((char)(i + 97)+ " : " +Frequency[i]);
                if(iMax < Frequency[i])
                {
                    iMax = Frequency[i];
                    ch= (char)(i + 97);
                }
            }
        }

        System.out.println("Maximum occured character is : " + ch +" with frequency : "+ iMax);

        sobj.close();

    }
}