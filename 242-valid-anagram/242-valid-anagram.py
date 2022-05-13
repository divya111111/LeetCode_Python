class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s)!=len(t):
            return False
        
        hashs={}
        hasht={}

        for i in range(len(s)):

            hashs[s[i]]=1+hashs.get(s[i],0)
            hasht[t[i]]=1+hasht.get(t[i],0)

        for c in hashs:
            if(hashs[c] !=hasht.get(c,0)):
                return False
            
        return True
            
        
        
     