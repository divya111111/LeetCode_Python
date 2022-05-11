class Solution(object):
    def firstUniqChar(self, s):
        _map={}  # _map={l:1,e:3,t:1.....}   for leetcode ex
        for i in s:
            if(i in _map):
                _map[i]+=1
            else:
                _map[i]=1
                
        for idx, val in enumerate(s):
            if(_map[val]==1):
                return idx
        return -1
     