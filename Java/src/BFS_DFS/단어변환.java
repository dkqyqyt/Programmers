package BFS_DFS;

import java.util.LinkedList;

public class 단어변환 {
	public int solution(String begin, String target, String[] words) {
        int answer = 0;
        LinkedList<String> que = new LinkedList<>();
        que.add(begin);
        boolean[] visit = new boolean[words.length];
        int depth = 0;
        while(!que.isEmpty()) {
            int it = que.size();
            for(int i = 0; i < it; i++) {
                String word = que.poll();
                if(word.equals(target)) return depth;
                for(int j = 0; j < words.length; j++){
                    if(visit[j]) continue;
                    String compareWord = words[j];
                    int diff = 0;
                    for(int k = 0; k < word.length(); k++) {
                        if(word.charAt(k) != compareWord.charAt(k)) {
                            diff++;
                        }
                    }
                    if(diff == 1) {
                        visit[j] = true;
                        que.add(compareWord);
                    }
                }
            }
            depth++;
        }
        return 0;
    }
}
