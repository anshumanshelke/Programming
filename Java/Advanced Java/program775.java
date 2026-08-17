////////////////////////////////////////////////////////
/// 
/// Maximum occurence of any letter 
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program775
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
        char temp = '\0';
        int iMax = 0;
        
        for(char ch : Arr)
        {
            if(hobj.containsKey(ch) == true)
            {
                iCount = hobj.get(ch);
                hobj.put(ch, iCount+1);

                if(iMax < iCount)
                {
                    iMax = iCount;
                    temp = ch;
                }
            }
            else
            {
                hobj.put(ch, 1);

                if(iMax < iCount)
                {
                    iMax = iCount;
                    temp = ch;
                }
            }
        }

        for(char cValue : hobj.keySet())
        {
            System.out.println(cValue+" occurs "+hobj.get(cValue) +" times");
        }

            System.out.println(iMax+" is the maximum occurence of  "+temp+" letter ");


        sobj.close();
    }
}