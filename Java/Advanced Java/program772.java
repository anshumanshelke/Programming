////////////////////////////////////////////////////////
/// 
/// tells whether key exists or NOT
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program772
{
    public static void main(String A[])
    {
        Scanner sobj = new Scanner(System.in);

        // System.out.println();
        System.out.println("Enter String : ");
        String str = sobj.nextLine();

        char Arr[] = str.toCharArray();

        for(char ch : Arr)
        {
            System.out.println(ch);
        }

        //as per key word - it's for loop
        // as per logical way- it's for each loop
        // drawback- it's not controlled, i.e. it's only i++, we can't i+= 2

        sobj.close();
    }
}