class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
      
        for ch in num_str:
            if ch != '9':
                max_num = num_str.replace(ch, '9')
                break
        else:
            max_num = num_str
       
        if num_str[0] != '1':
            min_num = num_str.replace(num_str[0], '1')
        else:
            for ch in num_str[1:]:
                if ch not in ['0', '1']:
                    min_num = num_str.replace(ch, '0')
                    break
            else:
                min_num = num_str
        
        return int(max_num) - int(min_num)

        