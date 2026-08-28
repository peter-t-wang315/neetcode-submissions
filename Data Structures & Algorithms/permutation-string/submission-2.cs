public class Solution {
    public bool CheckInclusion(string s1, string s2) {
        if (s1.Length > s2.Length) return false;

        int right = 0;
        int left = 0;
        int[] s1Chars = new int[26];
        int[] s2Chars = new int[26];

        foreach (char c in s1) {
            s1Chars[c - 'a']++;
            s2Chars[s2[right] - 'a']++;
            right++;
        }

        right--;
        while (right < s2.Length-1) {
            if (s1Chars.SequenceEqual(s2Chars)) {
                return true;
            }

            right++;
            s2Chars[s2[left] - 'a']--;
            s2Chars[s2[right] - 'a']++;
            left++;
        }

        return s1Chars.SequenceEqual(s2Chars);
    }
}
