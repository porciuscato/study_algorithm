import java.util.PriorityQueue;
import java.util.HashMap;

public class Solution3 {
    static int[] answer = { 0, 0 };
    static final int MAX = 500000000;

    public static void main(String[] args) {
        Solution3 sol = new Solution3();
        int n = 6;
        int[] passenger = { 1, 1, 1, 1, 1, 1 };
        int[][] train = { { 1, 2 }, { 1, 3 }, { 1, 4 }, { 3, 5 }, { 3, 6 } };
        System.out.println(sol.solution(n, passenger, train));
    }

    public int[] solution(int n, int[] passenger, int[][] train) {
        int[][] stations = new int[n][n];
        for (int[] data : train) {
            int a = data[0] - 1;
            int b = data[1] - 1;
            stations[a][b] = 1;
            stations[b][a] = 1;
        }
        dijkstra(stations, 0, passenger);
        return answer;
    }

    public static void dijkstra(int[][] stations, int start, int[] passenger) {
        int N = stations.length;
        int[] distance = new int[N];
        for (int i = 0; i < N; i++) {
            distance[i] = MAX;
        }
        distance[0] = 0;

        PriorityQueue<HashMap<Integer, Integer>> que = new PriorityQueue<HashMap<Integer, Integer>>();

        que.add(new HashMap<Integer, Integer>(distance[0], 0));

        int distance_until_now, node;
        while (que.contains()) {
            HashMap<Integer, Integer> val = que.remove();
            System.out.println(val);
        }
    }

}
