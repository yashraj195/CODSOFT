import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, t_name):
        t_name = t_name.strip()
        if t_name:
            self.tasks.append({"t_name": t_name, "available": True, "deleted": False, "updated": False})
            return f"Task '{t_name}' added successfully!"
        return "Task name cannot be empty."

    def remove_task(self, t_name):
        for task in self.tasks:
            if t_name.lower() == task["t_name"].lower() and not task["deleted"]:
                task["deleted"] = True
                return f"Task '{task['t_name']}' removed successfully!"
        return f"Task '{t_name}' not found!"

    def toggle_task_availability(self, t_name):
        for task in self.tasks:
            if t_name.lower() == task["t_name"].lower() and not task["deleted"]:
                task["available"] = not task["available"]
                return f"Task '{task['t_name']}' {'completed' if not task['available'] else 'not completed'}."
        return f"Task '{t_name}' not found!"

    def update_task(self, old_name, new_name):
        new_name = new_name.strip()
        if new_name:
            for task in self.tasks:
                if old_name.lower() == task["t_name"].lower() and not task["deleted"]:
                    task["t_name"] = new_name
                    task["updated"] = True
                    return f"Task '{old_name}' updated to '{new_name}'."
            return f"Task '{old_name}' not found!"
        return "New task name cannot be empty."

class TodoApp:
    def __init__(self, root, todo_list):
        self.root = root
        self.todo_list = todo_list

        self.setup_ui()

    def setup_ui(self):
        self.root.title("To-do List")
        self.root.geometry("600x850")
        self.root.resizable(True, True)

        self.create_heading_frame()
        self.create_main_frame()

        self.update_task_listbox()

    def create_heading_frame(self):
        heading_frame = tk.Frame(self.root, bg="yellow", pady=20)
        heading_frame.pack(fill=tk.X)

        title_label = tk.Label(heading_frame, text="To-do List", font=("Helvetica", 28, "bold", "italic"), bg="yellow", fg="black")
        title_label.pack(padx=20)

    def create_main_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        self.create_scrollable_task_frame(frame)
        self.create_task_input_frame(frame)
        self.create_task_management_frame(frame)
        self.create_history_frame(frame)
        self.create_exit_button(frame)

    def create_scrollable_task_frame(self, parent_frame):
        self.canvas = tk.Canvas(parent_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.task_frame = tk.Frame(self.scrollable_frame)
        self.task_frame.pack()

    def create_task_input_frame(self, parent_frame):
        add_frame = tk.Frame(parent_frame)
        add_frame.pack(pady=10)

        self.add_entry = tk.Entry(add_frame, width=40, font=("Helvetica", 14))
        self.add_entry.pack(side=tk.LEFT, padx=5)
        add_button = tk.Button(add_frame, text="Create Task", command=self.add_task, bg="lightblue", font=("Helvetica", 14))
        add_button.pack(side=tk.LEFT)

    def create_task_management_frame(self, parent_frame):
        self.remove_frame = self.create_remove_task_frame(parent_frame)
        self.update_frame = self.create_update_task_frame(parent_frame)

    def create_remove_task_frame(self, parent_frame):
        remove_frame = tk.Frame(parent_frame)
        remove_frame.pack(pady=10)

        self.remove_entry = tk.Entry(remove_frame, width=40, font=("Helvetica", 14))
        self.remove_entry.pack(side=tk.LEFT, padx=5)
        remove_button = tk.Button(remove_frame, text="Remove Task", command=self.remove_task, bg="lightblue", font=("Helvetica", 14))
        remove_button.pack(side=tk.LEFT)

        return remove_frame

    def create_update_task_frame(self, parent_frame):
        update_frame = tk.Frame(parent_frame)
        update_frame.pack(pady=10)

        old_task_label = tk.Label(update_frame, text="Existing Task Name:", font=("Helvetica", 12))
        old_task_label.pack(side=tk.LEFT, padx=5)

        self.update_old_entry = tk.Entry(update_frame, width=20, font=("Helvetica", 14))
        self.update_old_entry.pack(side=tk.LEFT, padx=5)

        new_task_label = tk.Label(update_frame, text="New Task Name:", font=("Helvetica", 12))
        new_task_label.pack(side=tk.LEFT, padx=5)

        self.update_new_entry = tk.Entry(update_frame, width=20, font=("Helvetica", 14))
        self.update_new_entry.pack(side=tk.LEFT, padx=5)

        update_button = tk.Button(update_frame, text="Update Task", command=self.update_task, bg="lightblue", font=("Helvetica", 14))
        update_button.pack(side=tk.LEFT)

        return update_frame

    def create_history_frame(self, parent_frame):
        history_frame = tk.Frame(parent_frame)
        history_frame.pack(pady=20)

        history_label = tk.Label(history_frame, text="Task History", font=("Helvetica", 20, "bold"))
        history_label.pack()

        history_listbox_frame = tk.Frame(history_frame)
        history_listbox_frame.pack()

        self.history_listbox = tk.Listbox(history_listbox_frame, width=50, height=10, font=("Helvetica", 14))
        self.history_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        history_scrollbar = tk.Scrollbar(history_listbox_frame, orient="vertical", command=self.history_listbox.yview)
        history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.history_listbox.configure(yscrollcommand=history_scrollbar.set)

    def create_exit_button(self, parent_frame):
        button_frame = tk.Frame(parent_frame)
        button_frame.pack(pady=20)

        exit_button = tk.Button(button_frame, text="Exit", command=self.exit_app, bg="red", fg="white", font=("Helvetica", 14))
        exit_button.pack(side=tk.LEFT, padx=10)

    def update_task_listbox(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for task in self.todo_list.tasks:
            if not task["deleted"]:
                var = tk.BooleanVar(value=not task["available"])
                cb = tk.Checkbutton(self.task_frame, text=task["t_name"], variable=var,
                                    command=lambda t=task["t_name"], v=var: self.toggle_task(t, v), font=("Helvetica", 14))
                cb.pack(anchor='w')

        self.update_history_listbox()

    def update_history_listbox(self):
        self.history_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            status_list = []
            if task["deleted"]:
                status_list.append("Deleted")
            if task["updated"]:
                status_list.append("Updated")
            if not task["available"]:
                status_list.append("Completed")
            if not status_list:
                status_list.append("Pending")
            status = ", ".join(status_list)
            self.history_listbox.insert(tk.END, f"{task['t_name']} - {status}")

    def add_task(self):
        t_name = self.add_entry.get().strip()
        message = self.todo_list.add_task(t_name)
        messagebox.showinfo("Info", message)
        self.update_task_listbox()
        self.add_entry.delete(0, tk.END)

    def remove_task(self):
        t_name = self.remove_entry.get().strip()
        message = self.todo_list.remove_task(t_name)
        messagebox.showinfo("Info", message)
        self.update_task_listbox()
        self.remove_entry.delete(0, tk.END)

    def update_task(self):
        old_name = self.update_old_entry.get().strip()
        new_name = self.update_new_entry.get().strip()
        message = self.todo_list.update_task(old_name, new_name)
        messagebox.showinfo("Info", message)
        self.update_task_listbox()
        self.update_old_entry.delete(0, tk.END)
        self.update_new_entry.delete(0, tk.END)

    def toggle_task(self, t_name, var):
        message = self.todo_list.toggle_task_availability(t_name)
        messagebox.showinfo("Info", message)
        self.update_task_listbox()

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.quit()

if __name__ == "__main__":
    todo_list = ToDoList()
    root = tk.Tk()
    app = TodoApp(root, todo_list)
    root.mainloop() 