import qrcode
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, filedialog
from tkinter import ttk


# Function to generate and save QR code
def generate_qr():
    data = entry_data.get()
    filename = entry_filename.get()

    if not data or not filename:
        messagebox.showwarning("Input Error", "Both fields are required!")
        return

    try:
        # Generate the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')

        # Save the QR code
        save_path = f"{filename}.png"
        img.save(save_path)
        messagebox.showinfo("Success", f"QR Code saved as {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Function to clear input fields
def clear_fields():
    entry_data.set("")
    entry_filename.set("")


# Create the main window
root = Tk()
root.title("QR Code Generator")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Create a style for ttk widgets
style = ttk.Style()
style.theme_use("clam")  # Use the 'clam' theme for modern-looking widgets
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 10), padding=5)
style.configure("TEntry", font=("Helvetica", 12))

# Input Fields
entry_data = StringVar()
entry_filename = StringVar()

frame = ttk.Frame(root, padding="10")
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Enter Data:").grid(row=0, column=0, sticky="w", pady=5)
data_entry = ttk.Entry(frame, textvariable=entry_data, width=30)
data_entry.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Enter Filename:").grid(row=1, column=0, sticky="w", pady=5)
filename_entry = ttk.Entry(frame, textvariable=entry_filename, width=30)
filename_entry.grid(row=1, column=1, pady=5)

# Buttons
button_frame = ttk.Frame(frame)
button_frame.grid(row=2, column=0, columnspan=2, pady=10)

generate_button = ttk.Button(button_frame, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=0, column=0, padx=5)

clear_button = ttk.Button(button_frame, text="Clear", command=clear_fields)
clear_button.grid(row=0, column=1, padx=5)

# Footer Label
footer = Label(root, text="QR Code Generator © 2024", bg="#f0f0f0", fg="gray", font=("Helvetica", 10))
footer.pack(side="bottom", pady=5)

# Start the Tkinter event loop
root.mainloop()
