import java.util.PriorityQueue;


public class Heapjava {
    public static void main(String[] args) {
        PriorityQueue<Node> maxheap = new PriorityQueue<>(50000);
        for(int i = 0; i < 10; i++){
            Node node = new Node(-i, i);
            maxheap.add(node);
        }
        for(Node node: maxheap) {
            System.out.println(node.indexVal + " " + node.realVal);
        }
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
        return  this.indexVal <= target.indexVal ? -1 : 1;
    }
}
