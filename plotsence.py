import  matplotlib.pyplot as plt

c=0
v=[]
C0=[]
C1=[]
EV=[]
vs=[]
f=open("codes")
for l in f.readlines():
	v.append([[c], int(l[:4], 16), int(l[4:8], 16), int(l[8:10], 16)])
	C0.append(v[c][1])
	print(C0[c])
	C1.append(v[c][1])
	EV.append(v[c][2])
	vs.append(c)
	c+=1
plt.plot(vs, C0)
plt.ylabel("CODE H")
plt.xlabel("n")
plt.show()
