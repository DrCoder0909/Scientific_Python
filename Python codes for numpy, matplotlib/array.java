public class array{
	public static void main(String[] args)
	{
		Integer a[]= new Integer[10];
		for (int i =1; i<=10; i++){
			a[i-1]=i;
		}
		System.out.println(a);
	}
}