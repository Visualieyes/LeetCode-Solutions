class Solution:
    #syntax steroids
    def reverseWords(self, s: str) -> str:
        string_reversed = ' '.join( [i for i in (s.split()[::-1]) if i] )
                    
        return string_reversed
        
    
    #split words to remove spaces
    #Traverse through list in reverse, 
    #append space and word in split list     
    def reverseWords2(self, s: str) -> str:
        s_list = s.split()
        reverse_s = ''
        if (len(s_list) >= 2):
            reverse_s += s_list[-1]
            for i in range(len(s_list)-2, -1, -1):
                reverse_s += ' ' + s_list[i]
            return reverse_s
        else:
            return s
                
'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
Example 4:

Input: s = "  Bob    Loves  Alice   "
Output: "Alice Loves Bob"
Example 5:

Input: s = "Alice does not even like bob"
Output: "bob like even not does Alice"
'''
