public class Solution {
    public int CharacterReplacement(string s, int k) {
        int ret = 0;
        int l = 0;
        int r = 0;
        int maxWindowFreq = 0;
        Dictionary<char, int> seen = new();

        while (r < s.Length) {
            char rightC = s[r];
            if (!seen.ContainsKey(rightC)) {
                seen[rightC] = 0;
            }
            seen[rightC]++;
            maxWindowFreq = Math.Max(maxWindowFreq, seen[rightC]);

            while ((r - l + 1) - maxWindowFreq > k) {
                seen[s[l]]--;
                l++;
            }

            ret = Math.Max(ret, r-l+1);
            r++;
        }

        return ret;
    }
}
