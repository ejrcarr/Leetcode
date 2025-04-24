class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = set()
        letters = deque()
        longest = 0
        l = 0
        for r in range(len(s)):
            letter = s[r]
            while letters and letter in current_substring:
                temp = letters.popleft()
                current_substring.remove(temp)
                l += 1
            letters.append(letter)
            current_substring.add(letter)
            longest = max(longest, len(letters))
        return longest
