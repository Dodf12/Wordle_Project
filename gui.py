import tkinter as tk
def gui():
    window = tk.Tk()

    window.rowconfigure(0, minsize=50)
    window.columnconfigure([0, 1, 2, 3], minsize=50)

    label1 = tk.Label(text="W", bg="green", fg="black")
    label2 = tk.Label(text="O", bg="yellow", fg="black")
    label3 = tk.Label(text="R", bg="grey", fg="black")
    label4 = tk.Label(text="D", bg="green", fg="black")
    label5 = tk.Label(text="L", bg="yellow", fg="black")
    label6 = tk.Label(text="E", bg="grey", fg="black")
    
    
    label1.grid(row=0, column=0)
    label2.grid(row=0, column=1)
    label3.grid(row=0, column=2)
    label4.grid(row=0, column=3)
    label5.grid(row=0, column=4)
    label6.grid(row=0, column=5)

    window.mainloop()

gui()