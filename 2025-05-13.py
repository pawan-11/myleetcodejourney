class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        c = Counter(s)
        a=0
        for k,v in c.items():
            wrap = ord(k)+t-ord('z')
            
            newlen = v+v*math.ceil(wrap/26) if wrap >= 0 else v
            #print(k, v, wrap, math.ceil(wrap/26), newlen)
            a += newlen
        return a
       