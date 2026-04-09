import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First GUI Project")
root.geometry('600x400')

# Create a label
label = tk.Label(root, text="Welcome to Alex GUI Project",font=("Arial", 16))
label.pack()

# Create a Entry Field
entry = tk.Entry(root)
entry.pack()

# Start GUI
root.mainloop()