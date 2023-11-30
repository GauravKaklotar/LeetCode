class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        nb_operation=0
        parity=0
        x=bin(n)
        x=x[2::]
        i=0
        while i < len(x):
            if x[i]=="1":
                if  not parity % 2:
                    nb_operation+=(2**(len(x) - i ))-1 
                else:
                    nb_operation-=(2**(len(x) - i ))-1 
                parity+=1
            i+=1
        return nb_operation             
                    