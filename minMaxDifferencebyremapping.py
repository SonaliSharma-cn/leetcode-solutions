class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        
    
        max_digit = ''
        for ch in num_str:
            if ch != '9':
                max_digit = ch
                break
        if max_digit:
            max_num_str = num_str.replace(max_digit, '9')
        else:
            max_num_str = num_str

        min_digit = ''
        for ch in num_str:
            if ch != '0':
                min_digit = ch
                break
        if min_digit:
            min_num_str = num_str.replace(min_digit, '0')
        else:
            min_num_str = num_str

     
        max_num = int(max_num_str)
        min_num = int(min_num_str)

        return max_num - min_num

        