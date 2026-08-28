public class MinStack {
    private LinkedList<int> head;
    private LinkedList<int> min;

    public MinStack() {
        head = new();
        min = new();
    }
    
    public void Push(int val) {
        head.AddFirst(val);
        
        if (min.Count == 0 || min.First.Value >= val){
            min.AddFirst(val);
        }
    }
    
    public void Pop() {
        int x = head.First.Value;
        head.RemoveFirst();

        if (min.First.Value == x){
            min.RemoveFirst();
        }
    }
    
    public int Top() {
        return head.First.Value;
    }
    
    public int GetMin() {
        return min.First.Value;
    }
}
