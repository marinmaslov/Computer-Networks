'''
    Code in Python (v.3.7.0) for binary polynomial division
    Task 2, first homework by Julije Ožegović
    Computer Networks course @ FESB
    2018
'''

def binarno(x): 
    return bin(x)[2:] 

def dijeljenje(lhs, rhs):
    broj = lhs 
    djelitelj = rhs
    origlen = len(binarno(djelitelj))
    
    brojac = 1
    while (djelitelj | broj) > 2*djelitelj: 
        djelitelj <<= 1 
        brojac += 1

    rjesenje = 0
    while brojac>0:
        rjesenje <<= 1
        brojac -= 1
        print("%14s" % binarno(broj))
        djeliteljstr = binarno(djelitelj) 
        if (broj ^ djelitelj) < broj: 
            rjesenje |= 1
            broj ^= djelitelj
            print(1, " " * (11-len(djeliteljstr)), djeliteljstr[:origlen])
        else:
            print(0, " " * (11-len(djeliteljstr)), "0" * origlen)

        print(" " * (13-len(djeliteljstr)), "-" * origlen)
        djelitelj >>= 1
    print("%14s <<< ostatak" % binarno(broj)) 
    print(" -> %10s <<< rjesenje" % binarno(rjesenje)) 

if __name__ == '__main__':
    dijeljenje(132, 12) 
