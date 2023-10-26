class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod=1000000007
        ways=[1]*len(arr)
        arr.sort()
        hmap={}
        for i in range(len(arr)):
            hmap[arr[i]]=i
        
        for i in range(len(arr)):
            root=arr[i]
            for j in range(i):
                if root%arr[j]==0:
                    y=root//arr[j]
                    if y in hmap:
                        ways[i]+=ways[j] * ways[hmap[y]]
                        ways[i]%=mod
        
        return sum(ways)%mod   