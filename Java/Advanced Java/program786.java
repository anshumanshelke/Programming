////////////////////////////////////////////////////////
/// 
/// 
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program786
{
    public static void main(String A[])
    { 
        Scanner sobj = new Scanner(System.in);
        sobj.close();

        //Jagged array
        int Arr[][] = {{10,20,30}, {40,50,60}, {70,80,90, 100} , {11,21} };

        System.out.println(Arr.length);

        System.out.println(Arr[0].length);
        System.out.println(Arr[1].length);
        System.out.println(Arr[2].length);
        System.out.println(Arr[3].length);

        for(int i = 0; i < Arr.length ; i++)
        {
            for(int j = 0; j < Arr[i].length ; j++)
            {
                System.out.println(Arr[i][j] +"\t");
            }
            System.out.println();
        }
    
    }
}