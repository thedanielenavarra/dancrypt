from tkinter import *
from tkinter import filedialog
import os

class dcgui:
	
	def chgc(o, e):
		o.root.code["state"]="normal"

	def chgd(o, e):
		o.root.code["state"]="normal"

	def exe(o, e):
		cmd="./dancrypt "
		ifile=o.root.ifile["text"]
		ofile=o.root.ofile["text"]	
		if ifile.count(" ")!=0:
			ifile="\""+ifile+"\""
		if ofile.count(" ")!=0:
			ofile="\""+ofile+"\""
		if ifile is not "file" and ofile is not "file":
			if o.v.get()=="c":
				cmd+="c "+ifile+" "+ofile
			else:
				cmd+="d "+ifile+" "+ofile+" "+o.root.code.get()
			ox=os.popen(cmd)
			if o.v.get()=="c":
				o.root.code.delete(0, END)
				txt=ox.read().replace("\n", "")
				print(txt)
				o.root.code["text"]=txt
			print(ox.read())
			o.root.code["text"]
			
		else:
			tkinter.messagebox.showerror("Insert file to open and the name of the file to save")
		print(cmd)

	def ifile(o, e):
		f=filedialog.askopenfilename()
		if f is not None:
			o.root.ifile["text"]=f
	
	def ofile(o, e):
		f=filedialog.asksaveasfile(filetypes=(("Dancrypt file", "*.dancrp"), ("All types", "*.*")), defaultextension=".dancrp")
		if f is not None:
			o.root.ofile["text"]=f.name	

	def __init__(o):
		o.root=Tk()
		o.root.title("Dancrypt")
		Label(o.root, text="File to process:").grid(column=0, row=0)
		o.root.ifile=Button(o.root, text="file")
		o.root.ifile.grid(column=1, row=0)
		o.root.ifile.bind("<Button-1>", o.ifile)
		o.v=StringVar()
		o.v.set("c")
		o.root.radioc=Radiobutton(o.root, text="Crypt", value="c", variable=o.v)
		o.root.radiod=Radiobutton(o.root, text="Decrypt", value="d", variable=o.v)
		o.root.radioc.grid(column=0, row=1)
		o.root.radiod.grid(column=1, row=1)
		o.root.radioc.bind("<Button-1>", o.chgc)
		o.root.radiod.bind("<Button-1>", o.chgd)
		Label(o.root, text="Save file as:").grid(column=0, row=2)
		o.root.ofile=Button(o.root, text="file")
		o.root.ofile.bind("<Button-1>", o.ofile)
		o.root.ofile.grid(column=1, row=2)
		Label(o.root, text="Code:").grid(column=0, row=3)
		o.root.code=Entry(o.root, state="disabled")
		o.root.code.grid(column=1, row=3)
		o.root.prc=Button(o.root, text="Process")
		o.root.prc.grid(column=1, row=4)
		o.root.prc.bind("<Button-1>", o.exe)
		o.root.mainloop()

gui=dcgui()
