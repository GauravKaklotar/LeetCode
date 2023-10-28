class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a=1;
        e=1;
        i=1;
        o=1;
        u=1;
        a1=0;
        e1=0;
        i1=0;
        o1=0;
        u1=0;
        mod = pow(10, 9)+7
        for x in range(2, n+1):
            a1 = (e + i + u) % mod;
            e1 = (a + i) % mod;
            i1 = (e + o) % mod;
            o1 = i;
            u1 = (o + i) % mod;
            
            a = a1;
            e = e1;
            i = i1;
            o = o1;
            u = u1;
            
        return (a+e+i+o+u)%mod
        