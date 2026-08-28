public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        int l = 0;
        int r = 0;
        int sum = 0;
        int smallestWindow = nums.Length;

        while (r < nums.Length) {
            sum += nums[r];

            while (sum >= target) {
                smallestWindow = Math.Min(smallestWindow, r-l+1);
                sum -= nums[l];
                l++;
            }

            r++;
        }

        if (l == 0 && r == nums.Length) {
            return 0;
        }

        return smallestWindow;
    }
}