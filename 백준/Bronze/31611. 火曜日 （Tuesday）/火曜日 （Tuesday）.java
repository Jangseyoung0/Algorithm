import java.util.*;
public class Main { 
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in); 
    int x = sc.nextInt();
    if(x%7==2){
      System.out.println(1);
    }else{
      System.out.println(0);
    }
  }
}