import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
       Scanner scanner = new Scanner(System.in);

       String input = scanner.nextLine();//엔터 입력 받을 때까지 계속 입력
       
       String[] numbers = input.split(" ");//공백을 기준으로 나눈 후 String 배열에 넣자.

       int a = Integer.parseInt(numbers[0]); //너비 저장
       int b = Integer.parseInt(numbers[1]); //높이 비율 저장
       int c = Integer.parseInt(numbers[2]); //너비 비율 저장

       double xsquared = Math.pow(a,2)/(Math.pow(b,2)+Math.pow(c,2));

       double x = Math.sqrt(xsquared);

       int realheight = (int)(b*x);
       int realwidth = (int)(c*x);

       System.out.println(realheight+" "+realwidth);


    }
}
