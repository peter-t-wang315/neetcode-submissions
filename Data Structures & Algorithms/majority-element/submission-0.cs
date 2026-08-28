public class Solution {
    public int MajorityElement(int[] nums) {
        int majorityNum = nums[0];
        int count = 1;

        // Count occurrences of each numbers.
        foreach (int num in nums.Skip(1))
        {
            // If we find another number that matches our current majority num, we add to the count.
            if (majorityNum == num) {
                count++;
            }
            // If the number we are at is a different number, we need to decrement the counter or restart it.
            else {
                // If the majorityNum actually doesn't have the most amount of occurrences, we need to change the majorityNum that's occured.
                if (count == 0) {
                    count++;
                    majorityNum = num;
                }
                // If the majorityNum still has the most occurrences, we just decrement it's count.
                else {
                    count--;
                }
            }
        }

        return majorityNum;
    }
}