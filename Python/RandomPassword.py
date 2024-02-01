import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.label_length = tk.Label(root, text="Password Length:", font=("Arial", 12))
        self.label_length.pack(pady=10)

        self.length_entry = tk.Entry(root, font=("Arial", 12))
        self.length_entry.pack(pady=10)

        self.checkbox_frame = tk.Frame(root)
        self.checkbox_frame.pack(pady=10)

        self.include_letters_var = tk.IntVar()
        self.include_numbers_var = tk.IntVar()
        self.include_lowercase_var = tk.IntVar()
        self.include_uppercase_var = tk.IntVar()
        self.include_symbols_var = tk.IntVar()

        tk.Checkbutton(self.checkbox_frame, text="Include Letters", variable=self.include_letters_var, font=("Arial", 10)).pack(pady=5)
        tk.Checkbutton(self.checkbox_frame, text="Include Numbers", variable=self.include_numbers_var, font=("Arial", 10)).pack(pady=5)
        tk.Checkbutton(self.checkbox_frame, text="Include Lowercase", variable=self.include_lowercase_var, font=("Arial", 10)).pack(pady=5)
        tk.Checkbutton(self.checkbox_frame, text="Include Uppercase", variable=self.include_uppercase_var, font=("Arial", 10)).pack(pady=5)
        tk.Checkbutton(self.checkbox_frame, text="Include Symbols", variable=self.include_symbols_var, font=("Arial", 10)).pack(pady=5)

        self.generate_button = tk.Button(root, text="Generate and Copy Password", command=self.generate_and_copy_password, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.generate_button.pack(pady=20)

        self.password_label = tk.Label(root, text="", font=("Arial", 14))
        self.password_label.pack(pady=10)

    def generate_and_copy_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Password length must be greater than 0")

            selected_characters = ""
            if self.include_letters_var.get():
                selected_characters += string.ascii_letters
            if self.include_numbers_var.get():
                selected_characters += string.digits
            if self.include_lowercase_var.get():
                selected_characters += string.ascii_lowercase
            if self.include_uppercase_var.get():
                selected_characters += string.ascii_uppercase
            if self.include_symbols_var.get():
                selected_characters += string.punctuation

            if not selected_characters:
                raise ValueError("Select at least one character type")

            password = self.generate_random_password(length, selected_characters)
            self.password_label.config(text=f"Generated Password: {password}")

            # Copy the password to the clipboard
            pyperclip.copy(password)
            messagebox.showinfo("Password Copied", "Password copied to clipboard!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def generate_random_password(self, length, characters):
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
