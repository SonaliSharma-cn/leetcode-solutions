class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        senate = list(senate)
        banR, banD = 0, 0
        
        while True:
            countR, countD = 0, 0
            for i in range(len(senate)):
                if senate[i] == 'R':
                    if banR > 0:
                        banR -= 1
                        senate[i] = '0'
                    else:
                        banD += 1
                        countR += 1
                elif senate[i] == 'D':
                    if banD > 0:
                        banD -= 1
                        senate[i] = '0'
                    else:
                        banR += 1
                        countD += 1
            if countR == 0:
                return "Dire"
            if countD == 0:
                return "Radiant"
