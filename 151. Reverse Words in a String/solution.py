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

