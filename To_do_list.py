import tkinter as tk
from tkinter import simpledialog, messagebox


class To_do_list:
    def __init__(self):
        self.tasks = []

    def task_available(self):
        tasks_str = "Available Tasks:\n"
        for task in self.tasks:
            if task["available"]:
                tasks_str += f"{task['t_name']}\n"
        return tasks_str

    def add_task(self, t_name):
        self.tasks.append({"t_name": t_name, "available": True})
        return "Task added successfully!"

    def remove_task(self, t_name):
        for task in self.tasks:
            if t_name.lower() == task["t_name"].lower():
                self.tasks.remove(task)
                return "Task removed successfully!"
        return "Task not found!"

    def search_task(self, t_name):
        for task in self.tasks:
            if t_name.lower() in task["t_name"].lower():
                if task["available"]:
                    return f"Task found: {task['t_name']}"
        return "Task not found!"

    def toggle_task_availability(self, t_name):
        for task in self.tasks:
            if t_name == task["t_name"]:
                task["available"] = not task["available"]
                return f"Task {'completed' if not task['available'] else 'not completed'}: {task['t_name']}"
        return "Task not found!"


class TodoApp:
    def __init__(self, root, todo_list):
        self.root = root
        self.todo_list = todo_list

        self.root.title("To-do List")
        self.root.geometry("500x650")
        self.root.resizable(True, True)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.title_label = tk.Label(self.frame, text="To-do List", font=("Helvetica", 24))
        self.title_label.pack(pady=20)

        self.task_frame = tk.Frame(self.frame)
        self.task_frame.pack()

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=10)

        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=10)

        self.search_button = tk.Button(self.frame, text="Search Task", command=self.search_task)
        self.search_button.pack(pady=10)

        self.update_task_listbox()

    def update_task_listbox(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for task in self.todo_list.tasks:
            var = tk.BooleanVar(value=not task["available"])
            cb = tk.Checkbutton(self.task_frame, text=task["t_name"], variable=var,
                                command=lambda t=task["t_name"], v=var: self.toggle_task(t, v))
            cb.pack(anchor='w')

    def add_task(self):
        t_name = simpledialog.askstring("Add Task", "Enter the task:")
        if t_name:
            message = self.todo_list.add_task(t_name)
            messagebox.showinfo("Info", message)
            self.update_task_listbox()

    def remove_task(self):
        t_name = simpledialog.askstring("Remove Task", "Enter the task you want to remove:")
        if t_name:
            message = self.todo_list.remove_task(t_name)
            messagebox.showinfo("Info", message)
            self.update_task_listbox()

    def search_task(self):
        t_name = simpledialog.askstring("Search Task", "Enter the task:")
        if t_name:
            message = self.todo_list.search_task(t_name)
            messagebox.showinfo("Info", message)

    def toggle_task(self, t_name, var):
        message = self.todo_list.toggle_task_availability(t_name)
        messagebox.showinfo("Info", message)
        self.update_task_listbox()


if __name__ == "__main__":
    todo_list = To_do_list()

    root = tk.Tk()
    app = TodoApp(root, todo_list)
    root.mainloop()
