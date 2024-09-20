import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import openpyxl
import os
from datetime import datetime

# Function to handle form submission and save to Excel
def submit_data():
    try:
        bullet_name = bullet_name_entry.get()
        bullet_weight = bullet_weight_entry.get()
        brass_name = brass_name_entry.get()
        primer_type = primer_type_entry.get()
        powder_type = powder_type_entry.get()
        powder_weight = powder_weight_entry.get()
        oal_length = oal_length_entry.get()
        trimmed_length = trimmed_length_entry.get() if case_trimmed_var.get() == 1 else ""  # Only get trimmed length if enabled
        notes = notes_entry.get("1.0", tk.END).strip()
        operator = operator_combobox.get()
        caliber = caliber_combobox.get()  # Get selected caliber
        
        # Get the checkbox state and add an "X" if it is checked
        case_trimmed = "X" if case_trimmed_var.get() == 1 else ""

        # Ensure all fields are filled
        if not (bullet_name and bullet_weight and brass_name and primer_type and powder_type and powder_weight and oal_length and operator and caliber):
            messagebox.showwarning("Input Error", "All fields must be filled!")
            return

        # Convert numeric fields to float (if applicable)
        try:
            bullet_weight = float(bullet_weight)
            powder_weight = float(powder_weight)
            trimmed_length = float(trimmed_length) if case_trimmed_var.get() == 1 else ""
            oal_length = float(oal_length)
        except ValueError:
            messagebox.showerror("Input Error", "Please ensure that the numeric fields contain valid numbers.")
            return

        # Get the current date
        current_date = datetime.now().strftime('%Y-%m-%d')

        # Get the next ID based on the number of existing entries in the Excel file
        file_name = 'ammo_reloading_data.xlsx'
        if os.path.exists(file_name):
            book = openpyxl.load_workbook(file_name)
            sheet = book.active
            next_id = sheet.max_row  # The next ID is the current max row
        else:
            next_id = 1  # If the file doesn't exist, start with ID 1

        # Store the data in a dictionary
        data = {
            'ID': [next_id],  # Add the generated ID
            'Date': [current_date],
            'Operator': [operator],
            'Caliber': [caliber],  # Add the selected caliber
            'Bullet Name': [bullet_name],
            'Bullet Weight (grains)': [bullet_weight],
            'Brass Name': [brass_name],
            'Primer Type': [primer_type],
            'Powder Type': [powder_type],
            'Powder Weight (grains)': [powder_weight],
            'OAL Length (in)': [oal_length],
            'Case trimmed': [case_trimmed],  # Add the checkbox value ("X" if checked)
            'Trimmed Case Length (in)': [trimmed_length],
            'Notes': [notes]
        }

        # Convert the data to a DataFrame
        df = pd.DataFrame(data)

        # Check if the Excel file exists and append or create it
        if os.path.exists(file_name):
            with pd.ExcelWriter(file_name, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, index=False, header=False, startrow=next_id)
        else:
            df.to_excel(file_name, index=False)

        messagebox.showinfo("Data Submitted", f"Data with ID {next_id} has been logged successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def toggle_trimmed_length():
    if case_trimmed_var.get() == 1:
        trimmed_length_entry.config(state="normal")  # Enable the field
    else:
        trimmed_length_entry.config(state="disabled")  # Disable the field

# Function to load calibers from the calibers.txt file
def load_calibers():
    if os.path.exists("calibers.txt"):
        with open("calibers.txt", "r") as f:
            calibers = [line.strip() for line in f.readlines()]
    else:
        # Default calibers if the file doesn't exist
        calibers = [".22 Hornet", ".222", ".223", "6,5x55 SE", ".308"]
    return calibers

# Function to save calibers to the calibers.txt file
def save_calibers(new_caliber):
    calibers = load_calibers()
    if new_caliber not in calibers:
        calibers.append(new_caliber)
        with open("calibers.txt", "w") as f:
            for caliber in calibers:
                f.write(caliber + "\n")
        # Update the dropdown list
        caliber_combobox['values'] = calibers
        messagebox.showinfo("Success", f"Caliber '{new_caliber}' added successfully!")
    else:
        messagebox.showwarning("Duplicate", f"The caliber '{new_caliber}' already exists!")

# Function to add a new caliber
def add_caliber():
    new_caliber = new_caliber_entry.get().strip()
    if new_caliber:
        save_calibers(new_caliber)
        new_caliber_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid caliber.")

# Create the main window
root = tk.Tk()
root.title("Ammo Reloading Data Entry")
root.geometry("450x540")

# Create and place labels and entry fields
fields = {
    "Bullet Name": None,
    "Bullet Weight (grains)": None,
    "Brass Name": None,
    "Primer Type": None,
    "Powder Type": None,
    "Powder Weight (grains)": None,
    "OAL Length (in)": None
}

entries = {}

for idx, (label, var) in enumerate(fields.items()):
    tk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=idx, column=1, padx=10, pady=5, sticky="w")
    entries[label] = entry

# Assign entries for easier access
bullet_name_entry = entries["Bullet Name"]
bullet_weight_entry = entries["Bullet Weight (grains)"]
brass_name_entry = entries["Brass Name"]
primer_type_entry = entries["Primer Type"]
powder_type_entry = entries["Powder Type"]
powder_weight_entry = entries["Powder Weight (grains)"]
oal_length_entry = entries["OAL Length (in)"]

# Operator dropdown (Combobox)
tk.Label(root, text="Operator").grid(row=len(fields), column=0, padx=10, pady=5, sticky="e")
operator_combobox = ttk.Combobox(root, values=["Arnar Halldórsson", "Benedikt Orri", "Kjartan Magnússon", "Daði Lange"], state="readonly")
operator_combobox.grid(row=len(fields), column=1, padx=10, pady=5, sticky="w")

# Caliber dropdown (Combobox)
tk.Label(root, text="Caliber").grid(row=len(fields)+1, column=0, padx=10, pady=5, sticky="e")
calibers = load_calibers()  # Load calibers from file
caliber_combobox = ttk.Combobox(root, values=calibers, state="readonly")
caliber_combobox.grid(row=len(fields)+1, column=1, padx=10, pady=5, sticky="w")

# Input field and button to add a new caliber
tk.Label(root, text="Add New Caliber").grid(row=len(fields)+2, column=0, padx=10, pady=5, sticky="e")
new_caliber_entry = tk.Entry(root)
new_caliber_entry.grid(row=len(fields)+2, column=1, padx=10, pady=5, sticky="w")

add_caliber_button = tk.Button(root, text="Add Caliber", command=add_caliber)
add_caliber_button.grid(row=len(fields)+3, column=0, columnspan=2, pady=5, padx=10, sticky="ew")

# Case trimming checkbox
case_trimmed_var = tk.IntVar()  # This will be 1 if checked, 0 if unchecked
tk.Label(root, text="Case trimming").grid(row=len(fields)+4, column=0, padx=10, pady=5, sticky="e")
hylki_stytt_checkbox = tk.Checkbutton(root, text="Case trimmed", variable=case_trimmed_var, command=toggle_trimmed_length)
hylki_stytt_checkbox.grid(row=len(fields)+4, column=1, padx=10, pady=5, sticky="w")

# Trimmed Case Length field
tk.Label(root, text="Trimmed Case Length (in)").grid(row=len(fields)+5, column=0, padx=10, pady=5, sticky="e")
trimmed_length_entry = tk.Entry(root, state="disabled")  # Initially disabled
trimmed_length_entry.grid(row=len(fields)+5, column=1, padx=10, pady=5, sticky="w")

# Notes field
tk.Label(root, text="Notes").grid(row=len(fields)+6, column=0, padx=10, pady=5, sticky="e")
notes_entry = tk.Text(root, height=4, width=30)
notes_entry.grid(row=len(fields)+6, column=1, padx=10, pady=5, sticky="w")

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=len(fields)+7, column=0, columnspan=2, pady=20, padx=20, sticky="ew")

# Start the main event loop
root.mainloop()