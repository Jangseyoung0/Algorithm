import java.util.*;
public class Main { 
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in); 
    int n = sc.nextInt();
    int m = sc.nextInt();
    int s;
    if(n>=20){
      s = 24+m-n;
    }else{
      s = m-n;
    }
    System.out.println(s);
  }
}