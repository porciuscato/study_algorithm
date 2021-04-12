import java.util.HashMap;

class Solution1 {
    public static void main(String[] args) {
        Solution1 sol = new Solution1();

        int[] cards = { 4, 5, 3, 2, 1 };
        int[] wants = { 2, 4, 4, 5, 1 };
        System.out.println(sol.solution(cards, wants));

        cards = new int[] { 5, 4, 5, 4, 5 };
        wants = new int[] { 1, 2, 3, 5, 4 };
        System.out.println(sol.solution(cards, wants));
    }

    public int solution(int[] gift_cards, int[] wants) {
        HashMap<Integer, Integer> card_count = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> want_count = new HashMap<Integer, Integer>();

        for (int card : gift_cards) {
            card_count.put(card, card_count.getOrDefault(card, 0) + 1);
        }
        for (int want : wants) {
            want_count.put(want, want_count.getOrDefault(want, 0) + 1);
        }

        int answer = 0;

        int want_left, card_left;
        for (int want : want_count.keySet()) {
            want_left = want_count.get(want);
            card_left = card_count.getOrDefault(want, 0);
            if (want_left >= card_left) {
                answer += want_left - card_left;
            }
        }
        return answer;
    }
}