import java.util.ArrayList;

public class Solution2 {
    static int answer = 0;

    public static void main(String[] args) {
        Solution2 sol = new Solution2();
        int[][] needs = { { 1, 0, 0 }, { 1, 1, 0 }, { 1, 1, 0 }, { 1, 0, 1 }, { 1, 1, 0 }, { 0, 1, 1 } };
        int r = 2;
        System.out.println(sol.solution(needs, r));
    }

    public int solution(int[][] needs, int r) {
        ArrayList<Integer> origin = new ArrayList<Integer>();
        for (int i = 0; i < needs[0].length; i++) {
            origin.add(i);
        }
        combi(needs, origin, r, new ArrayList<Integer>(), 0, 0);
        return answer;
    }

    static void combi(int[][] needs, ArrayList<Integer> origin, int aim, ArrayList<Integer> array, int depth,
            int last) {
        if (depth == aim) {
            int pos = 0;
            for (int[] line : needs) {
                boolean flag = true;
                for (int i = 0; i < line.length; i++) {
                    int val = line[i];
                    if (val == 1) {
                        if (!array.contains(i)) {
                            flag = false;
                            break;
                        }
                    }
                }
                if (flag) {
                    pos += 1;
                }
            }

            if (pos >= answer) {
                answer = pos;
            }
        } else {
            for (int i = last; i < origin.size(); i++) {
                ArrayList<Integer> arr = new ArrayList<Integer>();
                for (int j = 0; j < array.size(); j++) {
                    arr.add(array.get(j));
                }
                arr.add(origin.get(i));
                combi(needs, origin, aim, arr, depth + 1, i + 1);
            }
        }
    }
}
