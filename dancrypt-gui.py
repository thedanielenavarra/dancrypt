#!/bin/env python3

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import datetime

class dcgui:
		
	def getinfo(o, ifile):
		try:
			f=open("dancrypt.log")
			l=f.readlines()
			b=int(l[0].strip())
			d=float(l[1].strip())
			fl=os.path.getsize(ifile)
			return str(fl*d/b)
		except:
			messagebox.showerror("There's no log file")
			return str(1024)
	
	def chgc(o, e):
		o.root.code["state"]="readonly"

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
			o.root.plab["text"]=str(datetime.timedelta(seconds=float(o.getinfo(ifile))))+" seconds to go"
			o.root.prc["text"]="..."
			o.root.update()
			ox=os.popen(cmd)
			if o.v.get()=="c":
				o.chgd(0)
				o.root.code.delete(0, END)
				txt=ox.read().strip()
				o.root.code.insert(0, txt)
				o.chgc(0)
			o.root.prc["text"]="Process"
			o.root.update()
			
			
		else:
			tkinter.messagebox.showerror("Insert file to open and the name of the file to save")
		#print(cmd)

	def ifile(o, e):
		f=filedialog.askopenfilename()
		if f is not None:
			o.root.ifile["text"]=f
	
	def ofile(o, e):
		flt=(("All types", "*.*"),)
		if o.v.get()=="c":
			flt=(("Dancrypt file", "*.dancrp"), ("All types", "*.*"))
		f=filedialog.asksaveasfile(filetypes=flt, defaultextension=".dancrp")
		if f is not None:
			o.root.ofile["text"]=f.name	
	def swch(o, e):
		f=o.root.ifile["text"]
		o.root.ifile["text"]=o.root.ofile["text"]
		o.root.ofile["text"]=f

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
		o.root.radiod.grid(column=0, row=2)
		o.root.radioc.bind("<Button-1>", o.chgc)
		o.root.radiod.bind("<Button-1>", o.chgd)
		o.root.swc=Button(o.root, text="Switch")
		o.root.swc.grid(column=1, row=1)
		o.root.swc.bind("<Button-1>", o.swch)
		Label(o.root, text="Save file as:").grid(column=0, row=3)
		o.root.ofile=Button(o.root, text="file")
		o.root.ofile.bind("<Button-1>", o.ofile)
		o.root.ofile.grid(column=1, row=3)
		Label(o.root, text="Code:").grid(column=0, row=4)
		o.root.code=Entry(o.root, state="disabled")
		o.root.code.grid(column=1, row=4)
		o.root.prc=Button(o.root, text="Process")
		o.root.prc.grid(column=1, row=5)
		o.root.plab=Label(o.root)
		o.root.plab.grid(column=0, row=6)
		o.root.prc.bind("<Button-1>", o.exe)
		o.root.mainloop()

gui=dcgui()
