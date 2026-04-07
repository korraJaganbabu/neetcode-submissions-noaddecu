class Solution:
    def isValid(self, s: str) -> bool:
        d = { ')': '(', '}' : '{', ']' : '[' }
        l = []
        for i in s:
            if i in d:
                if l and l[-1] == d[i]:
                    l.pop()
                else:
                    return False
            else:
                l.append(i)
        
        return True if not l else False
        

        