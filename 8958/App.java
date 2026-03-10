import java.util.Scanner;
public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);

        int T = scanner.nextInt();//테스트 케이스 개수
        
        for (int i=0; i<T; i++){
            int combo=0;
            int totalscore=0;
            String input = scanner.next();//위에서 발생하는 엔터 찌꺼기 해결
            for (int j=0; j<input.length(); j++){
               if(input.charAt(j)=='X'){
                    combo=0;
               }else{
                    combo++;
                    totalscore+=combo;
               }
            }
            System.out.println(totalscore);
        }
        
    }
}
