////////////////////////////////////////////////////////
/// 
/// get method used
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program768
{
    public static void main(String A[])
    {
        Scanner sobj = new Scanner(System.in);

        Hashtable <Character,Integer>hobj = new Hashtable<Character,Integer>();

        hobj.put('a', 1);
        hobj.put('b', 1);
        hobj.put('a', 2);
        hobj.put('b', 2);

        System.out.println(hobj);
        System.out.println(hobj.get('b'));

        sobj.close();
        sobj.close();

    }
}