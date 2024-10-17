import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primer ventana")
ventana.geometry("500x400+500+200")
ventana.minsize(400,200)
ventana.maxsize(800,600)
ventana.iconbitmap("dev.ico")
ventana.configure(bg="lightgreen")
ventana.resizable(False,True)
ventana.attributes("-alpha",0.9)
ventana.mainloop()