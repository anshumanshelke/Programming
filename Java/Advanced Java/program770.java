////////////////////////////////////////////////////////
/// 
/// tells whether key exists or NOT
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program770
{
    public static void main(String A[])
    {
        Scanner sobj = new Scanner(System.in);

        Hashtable <Character,Integer>hobj = new Hashtable<Character,Integer>();

        hobj.put('a', 1);
        hobj.put('b', 1);
        hobj.put('a', 2);
        hobj.put('b', 2);

        System.out.println(hobj.containsKey('b'));
        System.out.println(hobj.containsKey('c'));

        sobj.close();
    }
}