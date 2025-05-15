import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String s=sc.next();//문자열 입력
        String alp="abcdefghijklmnopqrstuvwxyz";
        char [] arr=new char[alp.length()];
        for(int i=0;i<alp.length();i++){
            arr[i]=alp.charAt(i);
            if(s.indexOf(arr[i])>=0){
                System.out.print(s.indexOf(arr[i])+" ");
            }
            else{
                System.out.print(-1+" ");
            }
        }
    }
}