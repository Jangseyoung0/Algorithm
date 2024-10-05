import java.util.*;
public class Main { 
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in); 
    int d,h,m;
    d = sc.nextInt();
    h = sc.nextInt();
    m = sc.nextInt();
    int bd=11;
    int bh=11;
    int bm=11;
    if(d<bd || (d==bd && h<bh) || (d==bd && h==bh && m<bm)){
      System.out.println(-1);
    }else{
      System.out.println((d - bd) * 24 * 60 + (h - bh) * 60 + (m - bm));
    } 
  } 
}