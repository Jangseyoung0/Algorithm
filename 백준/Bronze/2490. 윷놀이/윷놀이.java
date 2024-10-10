import java.util.*;
public class Main { 
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in); 
    int arr[][]=new int [3][4];
    int cnt=0;
    for(int i=0;i<arr.length;i++){
      for(int j=0;j<arr[0].length;j++){
        arr[i][j]=sc.nextInt();
      }
    }
    for(int i=0;i<arr.length;i++){
      for(int j=0;j<arr[0].length;j++){
        if(arr[i][j]==0){
          cnt++;
        }
      }
      switch (cnt) {
        case 0:
          System.out.println('E');
          break;
        case 1:
          System.out.println("A");
          break;
        case 2:
          System.out.println("B");
          break;
        case 3:
          System.out.println("C");
          break;
        default:
          System.out.println("D");
          break;
      }
      cnt=0;
    }
    sc.close();
  }
}