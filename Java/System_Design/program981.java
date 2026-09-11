/// Singelton cha final code

class ParkingLot
{
    private static ParkingLot instance;
    
    private ParkingLot()
    {
        System.out.println("Parking Log object gets created");
    }

    public static ParkingLot getInstanceLot()
    {
        if (instance == null)
        {
            instance = new ParkingLot();
        }

        return instance;
    }
}

class program981
{
    public static void main(String A[])
    {
        ParkingLot pobj1 = ParkingLot.getInstanceLot();
        ParkingLot pobj2 = ParkingLot.getInstanceLot();
        ParkingLot pobj3 = ParkingLot.getInstanceLot();


    }
}