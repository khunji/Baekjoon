import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);
        char[][] arr = new char[5][15];

        for(int i=0; i<5; i++){
            String word = scanner.next();
            for(int j=0; j<word.length();j++){
                arr[i][j] = word.charAt(j);
            }
        }

        for(int j=0; j<15; j++){
            for(int i=0; i<5; i++){
                if(arr[i][j]!='\u0000'){
                    System.out.print(arr[i][j]);
                }
            }
        }


        scanner.close();
    }
}
