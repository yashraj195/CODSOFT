import mysql.connector
import tkinter as tk
from tkinter import messagebox, Scrollbar, RIGHT, Y, END

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("600x500")

        self.conn = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="#########", 
            database="contact_book" 
        )
        self.cursor = self.conn.cursor()
        self.create_table()

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(8, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.create_title_label()
        self.create_entry_widgets()
        self.create_buttons()
        self.create_contact_listbox()

    def create_table(self):
        """Create the contact_list table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contact_list (
                c_name VARCHAR(255) NOT NULL,
                ph_no VARCHAR(15) PRIMARY KEY,
                email_id VARCHAR(30),
                address VARCHAR(60)
            )
        ''')
        self.conn.commit()

    def create_title_label(self):
        """Create the title label."""
        title_label = tk.Label(self.root, text="Contact Book", font=("Helvetica", 16, "bold"),bg="green", fg="black")
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

    def create_entry_widgets(self):
        """Create entry widgets for user input."""
        self.c_name_var = tk.StringVar()
        self.ph_no_var = tk.StringVar()
        self.email_id_var = tk.StringVar()
        self.address_var = tk.StringVar()

        labels = ["Name", "Phone Number", "Email ID", "Address"]
        variables = [self.c_name_var, self.ph_no_var, self.email_id_var, self.address_var]

        for i in range(len(labels)):
            label = labels[i]
            var = variables[i]
            tk.Label(self.root, text=label).grid(row=i + 1, column=0, padx=10, pady=5)
            tk.Entry(self.root, textvariable=var).grid(row=i + 1, column=1, padx=10, pady=5)

    def create_buttons(self):
        """Create buttons for various actions."""
        actions = [
            ("Add Contact", self.add_contact),
            ("View Contacts", self.view_contacts),
            ("Search Contact", self.search_contact),
            ("Delete Contact", self.delete_contact)
        ]

        for i in range(len(actions)):
            text, command = actions[i]
            tk.Button(self.root, text=text, command=command).grid(row=5 + i // 2, column=i % 2, padx=10, pady=10)

    def create_contact_listbox(self):
        """Create a listbox to display contacts."""
        self.contact_listbox = tk.Listbox(self.root, height=10, width=60)
        self.contact_listbox.grid(row=7, column=0, columnspan=4, padx=20, pady=10)

    def add_contact(self):
        """Add a new contact to the database."""
        c_name = self.c_name_var.get()
        ph_no = self.ph_no_var.get()
        email_id = self.email_id_var.get()
        address = self.address_var.get()

        if c_name and ph_no:
            try:
                self.cursor.execute('''
                    INSERT INTO contact_list (c_name, ph_no, email_id, address)
                    VALUES (%s, %s, %s, %s)
                ''', (c_name, ph_no, email_id, address))
                self.conn.commit()
                messagebox.showinfo("Success", "Contact added successfully!")
                self.clear_entries()
            except mysql.connector.IntegrityError:
                messagebox.showerror("Error", "Phone number must be unique.")
        else:
            messagebox.showwarning("Input Error", "Name and Phone Number are required.")

    def view_contacts(self):
        """Display all contacts in the listbox."""
        self.contact_listbox.delete(0, tk.END)
        self.contact_listbox.insert(tk.END, "All Contacts")
        self.contact_listbox.insert(tk.END, "-" * 80)
        self.contact_listbox.insert(tk.END, "Name              \t\tPhone Number          \t\tEmail ID                       \t\tAddress")
        self.contact_listbox.insert(tk.END, "-" * 80)

        self.cursor.execute('SELECT * FROM contact_list')
        contacts = self.cursor.fetchall()

        for contact in contacts:
            contact_str = f"{contact[0]:<15}    \t{contact[1]:<15}    \t{contact[2]:<20}      \t{contact[3]:<30}"
            self.contact_listbox.insert(tk.END, contact_str)

    def search_contact(self):
        """Search for a contact by name or phone number."""
        search_term = self.c_name_var.get() or self.ph_no_var.get()
        
        if not search_term:
            messagebox.showwarning("Input Error", "Please enter a Name or Phone Number to search.")
            return

        self.contact_listbox.delete(0, tk.END)
        self.cursor.execute('''
            SELECT * FROM contact_list WHERE c_name LIKE %s OR ph_no LIKE %s
        ''', ('%' + search_term + '%', '%' + search_term + '%'))
        contacts = self.cursor.fetchall()

        self.contact_listbox.insert(tk.END, "Name   \t\tPhone Number    \t\tEmail ID       \t\tAddress")
        self.contact_listbox.insert(tk.END, "-" * 80)

        for contact in contacts:
            contact_str = f"{contact[0]:<15}\t{contact[1]:<15}\t{contact[2]:<20}\t{contact[3]:<30}"
            self.contact_listbox.insert(tk.END, contact_str)

    def delete_contact(self):
        """Delete a selected contact from the database."""
        selected_contact = self.contact_listbox.get(tk.ACTIVE)
        if selected_contact and selected_contact != "Name\t\tPhone Number\t\tEmail ID\t\tAddress":
            contact_parts = selected_contact.split('\t')
            if len(contact_parts) > 1:
                ph_no = contact_parts[1].strip()
                try:
                    self.cursor.execute('DELETE FROM contact_list WHERE ph_no = %s', (ph_no,))
                    self.conn.commit()
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                    self.view_contacts()
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error deleting contact: {err}")
            else:
                messagebox.showwarning("Selection Error", "Unable to extract phone number.")
        else:
            messagebox.showwarning("Selection Error", "No contact selected or format mismatch.")


    def clear_entries(self):
        """Clear the input fields."""
        self.c_name_var.set("")
        self.ph_no_var.set("")
        self.email_id_var.set("")
        self.address_var.set("")

    def close_connection(self):
        """Close the database connection."""
        self.conn.close()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
    app.close_connection()