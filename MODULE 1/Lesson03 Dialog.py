# from tkinter import messagebox

# res = messagebox.askquestion('Message title', 'Message ask content')
# print(res)
# res = messagebox.askyesno('Message title', 'Message y/n content')
# print(res)
# res = messagebox.askyesnocancel('Message title', 'Message y/n/cancel content')
# print(res)
# res = messagebox.askokcancel('Message title', 'Message ok/cancel content')
# print(res)
# res = messagebox.askretrycancel('Message title', 'Message retry/cancel content')
# print(res)


from tkinter import *
from tkinter import filedialog

root = Tk()
op = filedialog.askopenfilename()
print(op)
sa = filedialog.asksaveasfilename()
op1='8'


root.mainloop()