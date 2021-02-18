import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;

public class boj1655 {

    public static void main(String[] args) throws IOException {
        static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String s = br.readLine();
        int N = Integer.parseInt(s);

        PriorityQueue<Node> maxheap = new PriorityQueue<>(50000);
        PriorityQueue<Node> minheap = new PriorityQueue<>(50000);

        for(int i = 0; i < N; i++){
            String x = br.readLine();
			int num = Integer.parseInt(x);

            if(num % 2 == 0) maxheap.add(new Node(-num, num));
            else minheap.add(new Node(num, num));
            
            int vmaxheap = 0;
            int vminheap = 0;

            for(Node node: maxheap){
                vmaxheap = node.realVal;
                break;
            }
            for(Node node: minheap){
                vminheap = node.realVal;
                break;
            }

            if(i >= 1 && vmaxheap > vminheap) {
                Node big = maxheap.remove();
                Node sml = minheap.remove();
                minheap.add(new Node(big.realVal, big.realVal));
                maxheap.add(new Node(-sml.realVal, sml.realVal));
            }

            int answer = 0;
            for(Node node: maxheap) {
                answer = node.realVal;
                break;
            }
            sb.append(answer + "\n");
        }
        System.out.println(sb.toString());
    }
}

class Node implements Comparable<Node> {
    int indexVal;
    int realVal;

    public Node(int indexVal, int realVal) {
        this.indexVal = indexVal;
        this.realVal = realVal;
    }

    @Override
    public int compareTo(Node target) {
        return  this.indexVal < target.indexVal ? -1 : 1;
    }
}