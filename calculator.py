import tkinter as tk

# screen initialization
root = tk.Tk()

# Step 1: Create the window
# Name the window
root.title("Calculator")

# Step 5: Set the background color of the window
entry = tk.Entry(root, width=9, font=('Arial', 38, 'bold'),state='readonly')
entry.pack(pady=(30, 10))

#Step 2: Set the size of the window
# creating the frames
frame1 = tk.Frame(root)
frame1.pack(side='left', anchor='n')
frame2 = tk.Frame(root)
frame2.pack(side='left', anchor='n')
frame3 = tk.Frame(root)
frame3.pack(side='left', anchor='n')
frame4 = tk.Frame(root)
frame4.pack(side='left', anchor='n')

pixel = tk.PhotoImage(width=55, height=55)

# Step 6: Create a function to insert text into the entry widget
def command(text):
	entry.config(state='normal')
	entry.insert(tk.END, text)
	entry.config(state='readonly')


# Step 3: Create the buttons
# creating the buttons
# the buttons are created using a function to avoid repetition of codew
def buttons(text, frame):
	button = tk.Button(frame, text=text, font=('Arial', 20), image=pixel, bg="#333300", fg="white", compound="center")
	return button

def button_ops(text, frame, bg, fg):
	button = tk.Button(frame, text=text, font=('Arial', 20), image=pixel, bg=bg, fg=fg, activebackground="black", compound="center")
	return button

# Step 4: Place the buttons on the window
# Button 1, 4, 7 in frame1
btn1 = buttons('1', frame1).pack()
btn4 = buttons('4', frame1).pack()
btn7 = buttons('7', frame1).pack()

# Button 2, 5, 8, 0 in frame2
btn2 = buttons('2', frame2).pack()
btn5 = buttons('5', frame2).pack()
btn8 = buttons('8', frame2).pack()
btn0 = button_ops('0', frame2, '#333300', 'white').pack()

# Button 3, 6, 9 in frame3
btn3 = buttons('3', frame3).pack()
btn6 = buttons('6', frame3).pack()
btn9 = buttons('9', frame3).pack()

# Button +, -, *, / in frame4
plus = button_ops('+', frame4, 'black', 'white').pack()
minus = button_ops('-', frame4, 'black', 'white').pack()
mul = button_ops('*', frame4, 'black', 'white').pack()
div = button_ops('/', frame4, 'black', 'white').pack()

# keeps the window open
root.mainloop()
