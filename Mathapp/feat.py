import numpy as np

class linear_ALG:
    def __init__(self,a,b):
        self.a= a
        self.b=b

    def solve(self):
       return np.linalg.solve(self.a,self.b)



    
