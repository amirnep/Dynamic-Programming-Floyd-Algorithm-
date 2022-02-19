from numpy import *

class floyd(object):
    def __init__(self,v):
        self.v = v #For number of v
        self.w = zeros((self.v,self.v)) #Matrix W
        self.d = zeros((self.v,self.v)) #Matrix D
        self.num = 0
        
    def input_num(self): #This is for input weights and add them to matrix w.
        """This is Floyd Algorithm."""
        print("For inf please Enter larger number than wieghts for example 50.\n")
        
        for i in range(0,self.v,1):
            print()
            for j in range(0,self.v,1):
                self.num = int(input("Enter v{} to v{} weight: ".format(i+1,j+1))) #Enter 50 or larger: 100 for infinity.
                self.w[i,j] = self.num

    def run(self): #This if for run floyd algorithm.
        self.d = self.w

        for k in range(0,self.v,1):
            for i in range(0,self.v,1):
                for j in range(0,self.v,1):
                    self.d[i,j] = min(self.d[i,j],self.d[i,k]+self.d[k,j])

        return self.d
