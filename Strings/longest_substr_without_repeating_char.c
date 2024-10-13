"""
Given a string s, find the length of the longest 
substring
without repeating characters.
"""


class Solution {
public:
    int lengthOfLongestSubstring(string s) 
    {
        vector<int> chars(128);

        int left = 0,right=0,temp=0;
        while (right < s.length()) {
            char r = s[right];
            chars[r]++;

            while (chars[r] > 1) {
                char l = s[left];
                chars[l]--;
                left++;
            }

            temp = max(temp, right - left + 1);

            right++;
        }

        return temp;
    };
};
