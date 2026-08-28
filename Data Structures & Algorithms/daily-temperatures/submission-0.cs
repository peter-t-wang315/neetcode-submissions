public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {
        Stack<int> seenTemps = new();
        int[] result = new int[temperatures.Length];
        int temp;

        for (int i = 0; i < temperatures.Length; i++) {
            temp = temperatures[i];
            while (seenTemps.Count > 0 && temperatures[seenTemps.Peek()] < temp) {
                int poppedI = seenTemps.Pop();
                result[poppedI] = i - poppedI;
            }
            seenTemps.Push(i);
        }

        while (seenTemps.Count > 0) {
            result[seenTemps.Pop()] = 0;
        }
        return result;
    }
}
