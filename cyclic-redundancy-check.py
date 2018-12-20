'''
    Code in Python (v.3.7.0) for Cyclic Redundancy Check
    Task 3, first homework by Julije Ožegović
    Computer Networks course @ FESB
    2018
'''

def oduzmi(gen, remain): 
    rem= []
    for x in range(0,len(gen)):
        rem.append(int(gen[x]^remain[x]))
    return rem

def crc(gen,mes,kodiraj = True):
    print(mes)
    quotient = []
    message = []
    generator = []
    for char in mes:
        message.append(int(char,2))     
    for char in gen:
        generator.append(int(char,2))   
    if kodiraj == True:                  
        for x in range(len(gen)-1):
            message.append(0)
    remainder = message[0:len(generator)]
    index = 0
    while index+len(generator) < len(message):   
        if remainder[0] == 1:                     

            quotient.append(1)                      
            remainder = oduzmi(generator,remainder)
        else:
            quotient.append(0)
        remainder.pop(0)                                    
        remainder.append(message[index+len(generator)])     
        index+=1
    if remainder[0] ==1:
        remainder = oduzmi(generator,remainder)
    remainder.pop(0)
    for item in remainder:
        mes+=str(item)
    return(mes)

def kodiraj():
    mes = str(input("Unesite poruku prijenosa (niz 0 i 1): "))
    gen = str(input("Unesite koeficijente generirajuceg polinoma (niz 0 i 1): "))

    print('Sekvenca: '+crc(gen,mes))
    print('Generator: ' +gen)

def provjeri():
    mes = str(input("Unesite sekvencu za detekciju greske (niz 0 i 1): "))
    gen = str(input("Unesite generirajuci polinom (niz 0 i 1): "))

    detection = crc(gen, mes, False)
    if int(detection[len(mes):]) != 0:      
        print("Javila se greška")
    else:
        print("Nema detektiranih grešaka")

def main():
    choice = str(input("Kodiraj (k) ili potvrdi (p)?"))
    if choice.lower() == 'k':
        kodiraj()
    elif choice.lower() == 'p':
        provjeri()
    else:
        main()
main()
