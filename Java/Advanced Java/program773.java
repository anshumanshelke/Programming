////////////////////////////////////////////////////////
/// 
/// find occurence of every letter using hashmap
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program773
{
    public static void main(String A[])
    {
        Scanner sobj = new Scanner(System.in);

        HashMap <Character,Integer>hobj = new HashMap<Character,Integer>();

        // System.out.println();
        System.out.println("Enter String : ");
        String str = sobj.nextLine();

        char Arr[] = str.toCharArray();

        int iCount = 0;
        for(char ch : Arr)
        {
            if(hobj.containsKey(ch) == true)
            {
                iCount = hobj.get(ch);
                hobj.put(ch, iCount+1);
            }
            else
            {
                hobj.put(ch, 1);
            }
        }

        System.out.println(hobj);

        sobj.close();
    }
}