import math

def getorder(order, l):
    orig=[0]*l
    facts=[0]*l
    c=0
    while c<l:
        orig[c]=c
        facts[c]=math.factorial(c)
        c+=1
    out=[]
    takefrom=orig
    #print("I'll take from", takefrom)
    while len(out)<l:
        divider=facts[l-len(out)-1]
        #print("Dividing bY:", divider)
        totake=int(order/divider)
        order=order%divider
        #print("REST:", order)
        out.append(takefrom[totake])
        takefrom.pop(totake)
        #print("TOKEN:", out[len(out)-1])
    return out

while True:
    s=int(input("Size: "))
    o=0
    while o<math.factorial(s):
        print("Result:", getorder(o, s))
        o+=1
    
    
