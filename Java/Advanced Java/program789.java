////////////////////////////////////////////////////////
/// 
/// 
/// 
////////////////////////////////////////////////////////

import java.util.*;

class program789
{
    public static void main(String A[])
    { 
        Scanner sobj = new Scanner(System.in);

        int iRow = 0, iCol = 0;
        int i = 0, j = 0;

        System.out.println("Enter number of rows : ");
        iRow = sobj.nextInt();

        System.out.println("Enter number of Column : ");
        iCol = sobj.nextInt();

        int Arr[][] = new int[iRow][iCol];

        System.out.println("Enter the elements of Matrix");

        for(i = 0; i < iRow; i++)
        {
            for(j = 0; i < iCol; j++)
            {
                Arr[i][j] = sobj.nextInt();
            }
        }

        System.out.println("Elements of Matrix are -");

        for(i = 0; i < iRow; i++)
        {
            for(j = 0; i < iCol; j++)
            {
                System.out.println(Arr[i][j] + "\t");
                System.out.println();
            }
        }

        sobj.close();    
    }
}