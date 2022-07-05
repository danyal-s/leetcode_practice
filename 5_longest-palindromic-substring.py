# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest_palindrome = s[0]
        longest_palindrome_len = 1
        
        
        def find_longest_palindrome():
            nonlocal i, j, k, s, longest_palindrome, longest_palindrome_len
            while j >= 0 and k < len(s) and s[j] == s[k]:
                palindrome = s[j:k+1]
                if len(palindrome) > longest_palindrome_len:
                    longest_palindrome = palindrome
                    longest_palindrome_len = len(palindrome)
                j-=1
                k+=1
        
        for i in range(len(s) - 1) :
            
            # check if s[i] and s[i+1] match for even palindrome selection
            
            if s[i] == s[i+1]:
                j = i
                k = i+1       
                find_longest_palindrome()
            
            # check if s[i] and s[i+2] match for odd palindrome selection
        
            if i + 2 < len(s):
                if s[i] == s[i+2]:
                    j = i
                    k = i+2
                    find_longest_palindrome()
        
        return longest_palindrome
