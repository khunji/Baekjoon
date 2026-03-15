import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        int [] num = new int[16];
        num[0] = 4;
        num[1] = 9;
        num[2] = 25;

        for(int i=3; i<16; i++){
            num[i] = (int) Math.pow(Math.sqrt(num[i-1]) * 2 - 1, 2);
        }

        System.out.println(num[n]);

        scanner.close();
    }
}
