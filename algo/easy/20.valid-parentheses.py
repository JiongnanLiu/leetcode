class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_table = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in map_table:
                if stack:
                    top_ele = stack.pop()
                else:
                    top_ele = '#'
                if map_table[i] != top_ele:
                    return False
            else:
                stack.append(i)
        return not stack