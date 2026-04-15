import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("Python To-Do List")
root.geometry("400x450")

# UI Elements
label = tk.Label(root, text="Enter Task Below:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4caf50", fg="white", width=20)
add_button.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
listbox.pack(pady=10, padx=10)

delete_button = tk.Button(root, text="Delete Selected Task", command=delete_task, bg="#f44336", fg="white", width=20)
delete_button.pack(pady=5)

# Run the application
root.mainloop()