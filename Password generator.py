import tkinter as tk
import string
import random
import pyperclip

# Create a tkinter window
window = tk.Tk()
window.title("Password Generator")
window.geometry("600x600")
window.configure(bg="white")

# Add a label for password display
password_label = tk.Label(window, text="", font=("Arial", 20), bg="white")
password_label.pack(pady=50)

# Function to generate password and display
def generate_password():
    length = length_scale.get()
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Generate a password using random.sample
    password = "".join(random.sample(all_chars, length))

    # Display the generated password in the label
    password_label.config(text=password)

# Add a slider to select the password length
length_label = tk.Label(window, text="Select password length:", font=("Arial", 12), bg="white")
length_label.pack()

length_scale = tk.Scale(window, from_=8, to=32, orient=tk.HORIZONTAL, length=200)
length_scale.pack()

# Add a button to generate password and copy
generate_button = tk.Button(window, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_button.pack(pady=20)

copy_button = tk.Button(window, text="Copy Password", font=("Arial", 12), command=lambda: pyperclip.copy(password_label.cget("text")))
copy_button.pack()

window.mainloop()
