class Solution:
    def resultingString(self, s: str) -> str:
        def is_consecutive(c1, c2):
            return abs(ord(c1) - ord(c2)) == 1 or abs(ord(c1) - ord(c2)) == 25
        
        stack = []
        
        for ch in s:
            if stack and is_consecutive(stack[-1], ch):
                stack.pop()  
            else:
                stack.append(ch)
        
        return ''.join(stack)

if __name__ == "__main__":
    user_input = input("Enter a lowercase string: ")
    sol = Solution()
    result = sol.resultingString(user_input)
    print("Resulting String after removing consecutive characters:", result)        