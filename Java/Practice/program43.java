//Type 3
import java.util.Scanner;

    class program43
    {
        public static boolean CheackDivisible(int iNo)
        {

            if((iNo % 3 == 0) && (iNo % 5 == 0))
            {
                return true;
            }

            else
            {
                return false; 
           }
        }

    

    public static void main(String A[])
    {
        
        int iValue = 0;
        boolean bRet = false;

        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter Number : "); 
    

        iValue = sobj.nextInt();

        bRet = CheackDivisible(iValue);    

            if(bRet == true)
            {
                System.out.println("Number is divisible by 3 and 5");
            }

            else
            {
                System.out.println("Number is NOT divisible by 3 and 5");
            }

    }


}

