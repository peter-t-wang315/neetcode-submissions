public class Solution {
    public List<int> FindClosestElements(int[] arr, int k, int x) {
        int l = 0;
        int r = arr.Length-1;
        int mid = (r+l)/2;

        while (l < r) {
            mid = (r+l)/2;
            if (mid+k < arr.Length && x - arr[mid] > arr[mid+k] - x) {
                l = mid+1;
            }
            else {
                r = mid;
            }
        }

        return arr[l..(l+k)].ToList();
    }
}