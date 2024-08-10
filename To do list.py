import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
       
        self.title_label = tk.Label(self.root, text="To-Do List", font=("Helvetica", 18))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task to delete.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task != "":
                self.tasks[selected_task_index] = updated_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except:
            messagebox.showwarning("Warning", "You must select a task to update.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
