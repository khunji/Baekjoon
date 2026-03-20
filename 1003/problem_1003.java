/*
    n = 0일 때 fibonacci(0) -> 1 0
    n = 1일 때 fibonacci(1) -> 0 1
    n = 2일 때 fibonacci(2) -> 1 1
    n = 3일 때 fibonacci(3) -> 1 2
    ---->피보나치 수열이다!!
    --->동적 계획법으로 풀어보자.

*/



import java.util.Scanner;
public class problem_1003 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int [] dp_zero = new int[41]; //크기가 41인 배열 선언(인덱스 : 0~40)
        int [] dp_one = new int[41]; //크기가 41인 배열 선언(인덱스 : 0~40

        int T = sc.nextInt();

        dp_zero[0] = 1;
        dp_one[0] = 0;
        dp_zero[1] = 0;
        dp_one[1] = 1;

        for(int i=2; i<41; i++){
            dp_zero[i] = dp_zero[i-1] + dp_zero[i-2];
            dp_one[i] = dp_one[i-1] + dp_one[i-2];
        }

        for(int i=0; i<T; i++){
            int n = sc.nextInt();
            System.out.println(dp_zero[n] + " " + dp_one[n]);
        }

        sc.close();
        
    }

    
}
