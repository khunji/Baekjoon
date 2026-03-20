/*
문제 접근
체스판의 가장 윗 줄 맨 왼쪽이 'W','B'로 시작하는 체스판을 두 개 미리 만들어 놓고 입력한 보드를 하나씩 비교하자....
*/
import java.util.Scanner;
public class problem_1018 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();//세로 크기
        int M = sc.nextInt();//가로 크기

        char [][] board = new char[N][M];

        for(int i=0; i<N; i++){//보드 입력
            board[i] = sc.next().toCharArray();
        }

        char [][] boardW = {//8 * 8 크기
            {'W','B','W','B','W','B','W','B'},
            {'B','W','B','W','B','W','B','W'},
            {'W','B','W','B','W','B','W','B'},
            {'B','W','B','W','B','W','B','W'},
            {'W','B','W','B','W','B','W','B'},
            {'B','W','B','W','B','W','B','W'},
            {'W','B','W','B','W','B','W','B'},
            {'B','W','B','W','B','W','B','W'} 
        };

        char [][] boardB = {//8 * 8 크기
            {'B','W','B','W','B','W','B','W'},
            {'W','B','W','B','W','B','W','B'},
            {'B','W','B','W','B','W','B','W'},
            {'W','B','W','B','W','B','W','B'},
            {'B','W','B','W','B','W','B','W'},
            {'W','B','W','B','W','B','W','B'},
            {'B','W','B','W','B','W','B','W'},
            {'W','B','W','B','W','B','W','B'} 
        };

        int minCount = 64;

        for(int i=0; i<N-7; i++){
            for(int j=0; j<M-7; j++){
                int countW = 0;
                int countB = 0;
                for(int k=i; k<i+8; k++){
                    for(int l=j; l<j+8; l++){
                        if(board[k][l] != boardW[k-i][l-j]){
                            countW++;
                        }
                        if(board[k][l] != boardB[k-i][l-j]){
                            countB++;
                        }
                    }
                }

                int currentMin = Math.min(countW, countB);
                minCount = Math.min(minCount, currentMin);

            }
        }

        System.out.println(minCount);
        
        sc.close();
    }
}
