//Type 2
import java.util.Scanner;

    class program41
    {
        static void CheackDivisible(int iNo)
        {

            if((iNo % 3 == 0) && (iNo % 5 == 0))
            {
                System.out.println("Number is divisible by 3 and 5");
            }

            else
            {
                System.out.println("Number is NOT divisible by 3 and 5");
            }
        }

    

    public static void main(String A[])
    {
        
        Scanner sobj = new Scanner(System.in);
        System.out.println("Enter Number : "); 
    
        int iValue = 0;
        iValue = sobj.nextInt();

        CheackDivisible(iValue);    

    }
}

