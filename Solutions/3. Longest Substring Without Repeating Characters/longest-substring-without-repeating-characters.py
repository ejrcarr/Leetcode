class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = set()
        longest = l = 0
        for r in range(len(s)):
            letter = s[r]
            while letter in current_substring:
                current_substring.remove(s[l])
                l += 1
            current_substring.add(letter)
            longest = max(longest, r - l + 1)
        return longest
