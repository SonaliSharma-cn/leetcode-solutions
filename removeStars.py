class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                if stack:  
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == "__main__":
    s = input("Enter the string: ")      #leet**cod*e

    sol = Solution()
    result = sol.removeStars(s)
    print("String after removing stars:", result)     #lecoe
