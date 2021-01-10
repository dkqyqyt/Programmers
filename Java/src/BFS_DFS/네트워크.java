package BFS_DFS;

import java.util.LinkedList;

public class 네트워크 {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visit = new boolean[n];
        for(int i = 0; i < n; i++){
            if(visit[i]) continue;
            answer++;
            bfs(i,computers,visit);
        }
        return answer;
    }
    
    void bfs(int point, int[][] computers, boolean[] visit) {
        LinkedList<Integer> que = new LinkedList<>();
        que.add(point);
        
        while(!que.isEmpty()) {
            int next_point = que.pop();
            for(int i = 0; i < computers[next_point].length; i++) {
                if(computers[next_point][i] == 0 || visit[i]) continue;
                
                visit[i] = true;
                que.add(i);
            }
        }
    }
}
