////////////////////////////////////////////////////////
/// 
/// Maximum occurence of any letter 
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program783
{
    public static void main(String A[])
    {
        HashMap <String,Integer>hobj = new HashMap<String,Integer>();

        Scanner sobj = new Scanner(System.in);

        System.out.println("Enter String : ");
        String str = sobj.nextLine();

        str = str.trim();
        str = str.replaceAll("\\s+", " ");

        String Tokens[] = str.split(" ");

        int iCount = 0;

        for( String s : Tokens)
            {
                if((hobj.containsKey(s)))
                {
                    hobj.put(s, hobj.get(s)+1);
                }
                else
                {   
                    hobj.put(s, 1);
                }
            } 

        System.out.println(hobj);

        for (String sValue : hobj.keySet())
        {
            if(hobj.get(sValue) > iMax)
            {
                iMax = hobj.get(sValue);
                temp = sValue;
            }
        }

        System.out.println(temp + " Occurs Maximum no. of times : "+iMax);

        sobj.close();
    }
}