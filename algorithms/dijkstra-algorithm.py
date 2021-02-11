'''
    Code in Python (v.3.7.0) for dijkstra algorithm
    Task 5, second homework by Julije Ožegović
    Computer Networks course @ FESB
    2018
'''
import collections
import math
 
class Graf:
  def __init__(self):
      self.cvorovi = set()
      self.veze = collections.defaultdict(list)
      self.tezina = {}
 
  def dodajCvor(self, value):
    self.cvorovi.add(value)
 
  def dodajVezu(self, odCvora, doCvora, udaljenost):
    if odCvora == doCvora: pass
    self.veze[odCvora].append(doCvora)
    self.tezina[(odCvora, doCvora)] = udaljenost
 
  def __str__(self):
    string = "cvorovi: " + str(self.cvorovi) + "\n"
    string += "veze: " + str(self.veze) + "\n"
    string += "tezina: " + str(self.tezina)
    return string
 
def dijkstra(Graf, start):
  S = set()
  delta = dict.fromkeys(list(Graf.cvorovi), math.inf)
  prethodni = dict.fromkeys(list(Graf.cvorovi), None)
  delta[start] = 0
 
  while S != Graf.cvorovi:
    v = min((set(delta.keys()) - S), key=delta.get)
    for neighbor in set(Graf.veze[v]) - S:
      novi_put = delta[v] + Graf.tezina[v, neighbor]
      if novi_put < delta[neighbor]:
        delta[neighbor] = novi_put
        prethodni[neighbor] = v
    S.add(v)
	
  return (delta, prethodni)
 
 
 
def najkraciPut(Graf, start, end):
    delta, prethodni = dijkstra(Graf, start)
    put = []
    cvor = end

    while cvor is not None:
        put.append(cvor)
        cvor = prethodni[cvor]

    put.reverse()
    return put

G = Graf()
G.dodajCvor('a')
G.dodajCvor('b')
G.dodajCvor('c')
G.dodajCvor('d')
G.dodajCvor('e')
 
G.dodajVezu('a', 'b', 1)
G.dodajVezu('a', 'c', 6)
G.dodajVezu('a', 'd', 12)
G.dodajVezu('b', 'c', 1)
G.dodajVezu('c', 'e', 2)
G.dodajVezu('d', 'e', 7)


print(G) 
print(dijkstra(G, 'a'))
print("Najkrači put: ")
print(najkraciPut(G, 'a', 'e'))
