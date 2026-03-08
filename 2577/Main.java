import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
       Scanner scanner = new Scanner(System.in);

       int A = Integer.parseInt(scanner.nextLine());
       int B = Integer.parseInt(scanner.nextLine());
       int C = Integer.parseInt(scanner.nextLine());

       int[] counts = new int[10];

       int result = A*B*C;
       String strResult = String.valueOf(result);
       //String.valueOf(result) --> result를 문자열로 바꿔줌.

       for(int i=0; i<strResult.length(); i++){
        //문자열에서 문자 하나씩 꺼낸 후 그것을 정수로 바꿔줘야 한다.
        char ch = strResult.charAt(i);
        //charAt은 특정 위치에 있는 글자 하나만 쏙 빼오는 가위같은 역할
        int digit = ch-'0';

        counts[digit]++;
       }

       for(int i=0; i<counts.length; i++){
        System.out.println(counts[i]);
       }
    
    }
}
