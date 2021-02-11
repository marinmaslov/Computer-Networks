'''
    Code in Python (v.3.7.0) for binary polynomial division
    Task 4, second homework by Julije Ožegović
    Computer Networks course @ FESB
    2018
'''
class Graf: 
    def __init__(self, cvorovi): 
        self.V= cvorovi 
        self.Graf = [] 
        
    def dodajVezu(self, u, v, w): 
        self.Graf.append([u, v, w]) 
          
    def printArr(self, udaljenost): 
        print("Čvor   Udaljenost od izvorišta") 
        for i in range(self.V): 
            print("%d \t\t %d" % (i, udaljenost[i])) 
          
    def BellmanFord(self, izvoriste): 
        udaljenost = [float("Inf")] * self.V 
        udaljenost[izvoriste] = 0 

        for i in range(self.V - 1): 
            for u, v, w in self.Graf: 
                if udaljenost[u] != float("Inf") and udaljenost[u] + w < udaljenost[v]: 
                        udaljenost[v] = udaljenost[u] + w 

        for u, v, w in self.Graf: 
                if udaljenost[u] != float("Inf") and udaljenost[u] + w < udaljenost[v]: 
                        print ("Graf sadrži negativen puteve.")
                        return
                          
        self.printArr(udaljenost) 

g = Graf(5) 
g.dodajVezu(0, 1, -1) 
g.dodajVezu(0, 2, 2) 
g.dodajVezu(1, 2, 5) 
g.dodajVezu(1, 3, 2) 
g.dodajVezu(1, 4, 9) 
g.dodajVezu(3, 2, 5) 
g.dodajVezu(3, 1, 7) 
g.dodajVezu(4, 3, -3) 
  
g.BellmanFord(0) 
