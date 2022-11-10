from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter import messagebox

def rab_clicked():
	s=selected.get()
	ss=txt.get()
	if ss=="":
		messagebox.showwarning('Внимание!', "Введите стоимость погонного метра ограды")
	else:
		if s==1:
			b=int(txt.get())
			c=(2.1*b+1.2*b)*2
		else:
			b=int(txt.get())
			c=(2.1*b+2.4*b)*2
		messagebox.showinfo('Стоимость ограды:', str(c)+" руб.")
		txt.delete(0,END)

root= Tk()
root.title(chr(10029)*3+" Onix_Ogradki v0.99 (с) 2022, HappyAnd_13 "+chr(10029)*3)

window_height = 100
window_width = 910
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.resizable(False, False)
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
root.iconphoto(False, PhotoImage(file='5.png'))
selected=IntVar()


lb0=Label(root,text="Программа расчета стоимости ограды Onix_Ogradki v0.99", font=("Arial Bold", 15))
lb0.grid(column=1,row=0,padx=10)

rad1=Radiobutton(root,text="Одинарная ограда",value=1, variable=selected)
rad1.grid(column=0,row=1,padx=10)
rad2=Radiobutton(root,text="Двойная ограда",value=2,variable=selected)
rad2.grid(column=1,row=1,padx=10)
selected.set(1)

lb1=Label(root,text="Стоимость погонного метра: ")
lb1.grid(column=0,row=2,padx=10)

txt = Entry(root,width=10)
txt.grid(column=1, row=2,padx=10)
txt.focus()

btn = Button(root, text="Получить результат!",cursor="hand2",command=rab_clicked,padx=10)
btn.grid(column=2, row=2,padx=10)
root.mainloop()
