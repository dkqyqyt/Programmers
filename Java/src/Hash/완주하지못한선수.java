package Hash;

import java.util.Map;
import java.util.HashMap;
public class 완주하지못한선수 {
	public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String,Integer> hm = new HashMap<>();
        
        for(String name: participant) {
            if(hm.get(name) == null) {
                hm.put(name,1);
            }else {
                int value = hm.get(name);
                hm.put(name,value+1);
            }
        }
        
        for(String name: completion) {
            int value = hm.get(name);
            hm.put(name,value - 1);
        }
        
        for(String name: hm.keySet()) {
            if(hm.get(name) != 0) {
                answer = name;
            }
        }
        return answer;
    }
}
