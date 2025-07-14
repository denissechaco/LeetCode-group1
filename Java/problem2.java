class LRUCache {
    private int capacity;
    private Map<Integer, Node> cache;
    private Node left;
    private Node right;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();

        // left is least recently used pointer node
        // right is most recently used point node
        left = new Node(0, 0);
        right = new Node(0, 0);

        // creates the doubly linked list
        left.next = right;
        right.prev = left;
    }

    // this also adds the node to become the most recently used
    public int get(int key) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            removeNode(node);
            insertToRight(node);
            return node.value;
        }
        return -1;
    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            removeNode(cache.get(key));
        }
        Node node = new Node(key, value);
        cache.put(key, node);
        insertToRight(node);

        // remove least recently used node if cache
        // size passes capacity
        if (cache.size() > capacity){
            Node least = left.next;
            removeNode(least);
            cache.remove(least.key);
        }

    }

    private void removeNode(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    // adds node to be the most recently used (right)
    private void insertToRight(Node node){
        node.prev = right.prev;
        node.next = right;

        right.prev.next = node;
        right.prev = node;
    }

    private class Node {
        int key;
        int value;
        Node prev;
        Node next;

        public Node( int key, int value){
            this.key = key;
            this.value = value;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */