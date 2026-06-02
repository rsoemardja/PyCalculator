import tkinter as tk

# screen initialization
root = tk.Tk()

# Name the window
root.title("Calculator")

# creating the frames
frame1 = tk.frame(root)
frame1.pack(side='left', anchor='n')
frame2 = tk.frame(root)
frame2.pack(side='left', anchor='n')
frame3 = tk.frame(root)
frame3.pack(side='left', anchor='n')
frame4 = tk.frame(root)
frame4.pack(side='left', anchor='n')

# keeps the window open
root.mainloop
