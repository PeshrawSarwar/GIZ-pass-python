

class Solution(object):

    @staticmethod
    def longest_palindromic(s: str):
        # Square Matrix - length = length of the string [False]
        matrix = [[False for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            # major diagonal elements = True
                matrix[i][i] = True 
        max_length = 1
        start = 0
        # 2 to length of s+1
        for l in range(2,len(s)+1):
            # 0 to to length of s-1+1
            for i in range(len(s)-l+1):
                end = i+l
                if l==2:
                    if s[i] == s[end-1]:
                        matrix[i][end-1]=True
                        max_length = l
                        start = i
                else:
                    if s[i] == s[end-1] and matrix[i+1][end-2]:
                        matrix[i][end-1]=True
                        max_length = l
                        start = i
        return s[start:start+max_length]

ob = Solution()
print(ob.longest_palindromic("lagalabcdnananana")) 
# Output -> ananana


