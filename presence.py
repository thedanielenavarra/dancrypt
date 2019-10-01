import os
from tkinter import *
from tkinter import ttk

class repeat:

	def getmax(o):
		o.max=len([line.rstrip('\n') for line in open("codes")])
		
	def start(o):
		lines = [line.rstrip('\n') for line in open("codes")]	
		for l in lines:
			o.root.chars[l[int(sys.argv[1])]]['prog']['value']+=1
			o.root.chars[l[int(sys.argv[1])]]['perc']['text']=str(int(100*o.root.chars[l[int(sys.argv[1])]]['prog']['val']/o.max))+"%"
			

	def gen(o):
		n=int(sys.argv[2])
		c=0
		f=open("codes", "w")
		while c<n:
			f.write(os.popen("./dancrypt c dancrypt file").read())
			c+=1
		f.close()

	def __init__(o):
		if len(sys.argv)==1:
			os.system("python3 presence.py 0 & python3 presence.py 1 &python3 presence.py 2 &python3 presence.py 3 &python3 presence.py 4 &python3 presence.py 5 &python3 presence.py 6 &python3 presence.py 7 &python3 presence.py 8 &python3 presence.py 9")
			return
			#sys.argv.append(0)
			#f=repeat()
			#sys.argv[1]=1
			#f=repeat()
			#sys.argv[1]=2
			#f=repeat()
			#sys.argv[1]=3
			#f=repeat()
			#sys.argv[1]=4
			#f=repeat()
			#sys.argv[1]=5
			#f=repeat()
			#sys.argv[1]=6
			#f=repeat()
			#sys.argv[1]=7
			#f=repeat()
		if sys.argv[1]=="gen":
			o.gen()
			return
		o.root=Tk()
		o.root.title("Repeat controller")
		pos=[
			"150x350+0+0",
			"150x350+150+0",
			"150x350+300+0",
			"150x350+450+0",
			"150x350+600+0",
			"150x350+0+400",
			"150x350+150+400",
			"150x350+300+400",
			"150x350+450+400",
			"150x350+600+400"]
		o.root.geometry(pos[int(sys.argv[1])])
		print("ANALIZE: ", sys.argv[1])
		o.root.num=Label(o.root, text="0")
		o.root.chars={
			'0': {'lab': Label(o.root, text="0"),
				'prog': ttk.Progressbar(o.root)},
			'1': {'lab': Label(o.root, text="1"),
				'prog': ttk.Progressbar(o.root)},
			'2': {'lab': Label(o.root, text="2"),
				'prog': ttk.Progressbar(o.root)},
			'3': {'lab': Label(o.root, text="3"),
				'prog': ttk.Progressbar(o.root)},
			'4': {'lab': Label(o.root, text="4"),
				'prog': ttk.Progressbar(o.root)},
			'5': {'lab': Label(o.root, text="5"),
				'prog': ttk.Progressbar(o.root)},
			'6': {'lab': Label(o.root, text="6"),
				'prog': ttk.Progressbar(o.root)},
			'7': {'lab': Label(o.root, text="7"),
				'prog': ttk.Progressbar(o.root)},
			'8': {'lab': Label(o.root, text="8"),
				'prog': ttk.Progressbar(o.root)},
			'9': {'lab': Label(o.root, text="9"),
				'prog': ttk.Progressbar(o.root)},
			'A': {'lab': Label(o.root, text="A"),
				'prog': ttk.Progressbar(o.root)},
			'B': {'lab': Label(o.root, text="B"),
				'prog': ttk.Progressbar(o.root)},
			'C': {'lab': Label(o.root, text="C"),
				'prog': ttk.Progressbar(o.root)},
			'D': {'lab': Label(o.root, text="D"),
				'prog': ttk.Progressbar(o.root)},
			'E': {'lab': Label(o.root, text="E"),
				'prog': ttk.Progressbar(o.root)},
			'F': {'lab': Label(o.root, text="F"),
				'prog': ttk.Progressbar(o.root)}
		}
		c=0
		o.root.bb=Label(o.root, text=sys.argv[1])
		o.root.bb.grid(column=0, row=16)
		for LET in sorted(o.root.chars.keys()):
			o.root.chars[LET]['lab'].grid(column=0, row=c)
			o.root.chars[LET]['prog']['maximum']=o.getmax()
			o.root.chars[LET]['prog']['value']=0
			o.root.chars[LET]['prog'].grid(column=1, row=c)
			o.root.chars[LET]['perc']=Label(o.root)
			o.root.chars[LET]['perc'].grid(column=2, row=c)
			c+=1
		o.start()
		o.root.mainloop()

o=repeat()
