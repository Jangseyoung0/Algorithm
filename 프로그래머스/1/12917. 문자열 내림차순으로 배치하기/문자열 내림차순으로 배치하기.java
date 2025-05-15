import java.util.Arrays;
import java.util.Collections;
class Solution {
    public String solution(String s) {
        Character[] arr=new Character[s.length()];
        for(int i=0;i<s.length();i++){
            arr[i]=s.charAt(i);
        }
        String answer = "";
        Arrays.sort(arr,Collections.reverseOrder());
        StringBuilder sb=new StringBuilder();
        for(char c : arr){
            sb.append(c);
        }
        answer=sb.toString();
        return answer;
    }
}