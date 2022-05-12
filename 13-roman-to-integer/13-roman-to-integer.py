class Solution(object):
    def romanToInt(self, s):
        sol=0
        diction={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for idx, val in enumerate(s):
            
            if((idx+1 < len(s)) and (diction[val]<diction[s[idx+1]])):
                sol=sol-diction[val]
            else:
                sol=sol+diction[val]
        return sol