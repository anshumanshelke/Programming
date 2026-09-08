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

class program974
{
    public static void main(String A[])
    {
        ParkingLot pobj1 = ParkingLot.getInstanceLot();
        ParkingLot pobj2 = ParkingLot.getInstanceLot();

        System.out.println(pobj1 == pobj2);
    }
}