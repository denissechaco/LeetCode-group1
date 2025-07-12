class node{
        key: number|undefined;
        value : number|undefined;
        prev : node | null = null;
        next : node | null = null;
        constructor(key:number,value:number){
            this.key=key
            this.value=value
        }
    }

class   LRUCache {
    capacity: number;
    private cache!: Map<number, node>;
    private left: node;
    private right : node;
    constructor(capacity: number) {
        this.capacity = capacity
        this.cache = new Map();
        this.left = new node(0,0);
        this.right = new node (0,0);
        this.left.next=this.right;
        this.right.prev=this.left;

    }

    public get(key:number):any{
        if(this.cache.has(key)){
            let A : node = this.cache.get(key)!;
            this.removeNode(A);
            this.insertToRight(A);
            return A.value;
        }
        return -1
    }

    public put(key:number,value:number){
        if(this.cache.has(key)){
            this.removeNode(this.cache.get(key)!);
        }
        const A = new node(key,value);
        this.cache.set(key,A);
        this.insertToRight(A);
        if(this.cache.size>this.capacity){
            let least : node = this.left.next!;
            this.removeNode(least);
            this.cache.delete(least.key!);

        }
                
    }

    private removeNode(A:node){
        A.prev!.next=A.next;
        A.next!.prev=A.prev;
    }

    private insertToRight(A:node):void{
        A.prev=this.right.prev;
        A.next=this.right;

        this.right.prev!.next = A;
        this.right.prev = A;
    }

}
