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

pixel = tk.PhotoImage(width=55, height=55)

# creating the buttons
def buttons(text, frame):
	button = tk.Button(frame, text=text, font=('Arial', 20), image=pixel, bg="#333300", fg="white", compound="center")
	return button

def button_ops(text, frame, bg, fg):
	button = tk.Button(frame, text=text, font=('Arial', 20), image=pixel, bg=bg, fg=fg, activebackground="black", compound="center")
	return button

btn1 = buttons('1', frame1).pack()
btn4 = buttons('4', frame1).pack()
btn7 = buttons('7', frame1).pack()

btn2 = buttons('2', frame2).pack()
btn5 = buttons('5', frame2).pack()
btn8 = buttons('8', frame2).pack()
btn0 = button_ops('0', frame2, '#333300', 'white').pack()

btn3 = buttons('3', frame3).pack()
btn6 = buttons('6', frame3).pack()
btn9 = buttons('9', frame3).pack()

plus = button_ops('+', frame4, 'black', 'white').pack()
minus = button_ops('-', frame4, 'black', 'white').pack()
mul = button_ops('*', frame4, 'black', 'white').pack()
div = button_ops('/', frame4, 'black', 'white').pack()

# keeps the window open
root.mainloop
