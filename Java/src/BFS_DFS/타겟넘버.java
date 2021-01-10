package BFS_DFS;

public class 타겟넘버 {
	int count = 0;
    
    public int solution(int[] numbers, int target) {
        track(0,0,numbers,target);
        return count;
    }
    
    void track(int depth, int curr_sum, int[] numbers, int target) {
        if(depth == numbers.length) {
            if(curr_sum == target) {
                count++;
            }
            return;
        }       
        track(depth+1, curr_sum + numbers[depth],numbers, target);
        track(depth+1, curr_sum - numbers[depth],numbers, target);
    }
}
