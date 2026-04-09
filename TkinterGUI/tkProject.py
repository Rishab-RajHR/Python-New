import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First GUI Project")
root.geometry('600x400')

# Create a label
label = tk.Label(root, text="Welcome to Alex GUI",font=("Arial", 16))
label.pack()

# Start GUI
root.mainloop()