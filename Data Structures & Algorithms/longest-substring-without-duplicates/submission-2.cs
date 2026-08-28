public class Solution {
    public int LengthOfLongestSubstring(string s) {
        HashSet<char> seen = new ();
        int l = 0;
        int r = 0;
        int max = 0;

        for(;r < s.Length; r++) {
            if (seen.Contains(s[r])) {
                max = Math.Max(max, r-l);
                while(s[l] != s[r]) {
                    seen.Remove(s[l]);
                    l++;
                }
                l++;
            }
            seen.Add(s[r]);
        }

        return Math.Max(max, r-l);
    }
}
