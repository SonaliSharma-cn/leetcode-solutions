from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write
input_str = input("Enter characters without space (like aaabbccc): ")  #aaabbcccc
chars = list(input_str)

sol = Solution()
new_length = sol.compress(chars)

print("Compressed List:", chars[:new_length])     #Compressed List: ['a', '3', 'b', '2', 'c', '4']
print("New Length:", new_length)                  #New Length: 6