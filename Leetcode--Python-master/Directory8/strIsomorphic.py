'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
'''

class Solution(object):

    def __init__(self):
        self.dict={}

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for k,v in zip(s,t):
            if k not in self.dict:
                self.dict[k]=v
            else:
                #already k,v is in dict. check
                #check if it is isomorphic or not.
                if self.dict[k]!=v:
                    return False
        self.dict.clear()

        for k,v in zip(t,s):
            if k not in self.dict:
                self.dict[k]=v
            else:
                #already k,v is in dict. check
                #check if it is isomorphic or not.
                if self.dict[k]!=v:
                    return False
        return True

if __name__=="__main__":
    obj=Solution()
    s="aa"
    t="ab"
    res=obj.isIsomorphic(s,t)
    print(res)
