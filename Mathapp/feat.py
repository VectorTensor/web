import numpy as np

class linear_ALG:
    def __init__(self,a,b):
        self.a= a
        self.b=b

    def solve(self):
       return np.linalg.solve(self.a,self.b)

class mat:
    def __init__(self, a):
        self.a=a

    def Rank(self):
        return np.linalg.matrix_rank(self.a)

    def eign(self):
        return np.linalg.eigvals(self.a)    

    


    
