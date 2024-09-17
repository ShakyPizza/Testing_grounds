import tkinter as tk
from tkinter import messagebox
import pandas as pd
import openpyxl
import os

# Function to handle form submission and save to Excel
def submit_data():
    try:
        bullet_name = bullet_name_entry.get()
        bullet_weight = bullet_weight_entry.get()
        brass_name = brass_name_entry.get()
        primer_type = primer_type_entry.get()
        powder_type = powder_type_entry.get()
        powder_weight = powder_weight_entry.get()
        trimmed_length = trimmed_length_entry.get()
        oal_length = oal_length_entry.get()

        # Ensure all fields are filled
        if not (bullet_name and bullet_weight and brass_name and primer_type and powder_type and powder_weight and trimmed_length and oal_length):
            messagebox.showwarning("Input Error", "All fields must be filled!")
            return

        # Store the data in a dictionary
        data = {
            'Bullet Name': [bullet_name],
            'Bullet Weight (grains)': [bullet_weight],
            'Brass Name': [brass_name],
            'Primer Type': [primer_type],
            'Powder Type': [powder_type],
            'Powder Weight (grains)': [powder_weight],
            'Trimmed Case Length (in)': [trimmed_length],
            'OAL Length (in)': [oal_length]
        }

        # Convert the data to a DataFrame
        df = pd.DataFrame(data)

        file_name = 'ammo_reloading_data.xlsx'

        # Check if the Excel file exists
        if os.path.exists(file_name):
            # Load the existing workbook
            book = openpyxl.load_workbook(file_name)
            writer = pd.ExcelWriter(file_name, engine='openpyxl', mode='a', if_sheet_exists='overlay')
            writer.book = book
            writer.sheets = {ws.title: ws for ws in book.worksheets}
            df.to_excel(writer, sheet_name='Sheet1', index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
            writer.save()
        else:
            # If the file doesn't exist, create it
            df.to_excel(file_name, index=False)

        messagebox.showinfo("Data Submitted", "Data has been logged successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Ammo Reloading Data Entry")

# Create and place labels and entry fields
fields = {
    "Bullet Name": None,
    "Bullet Weight (grains)": None,
    "Brass Name": None,
    "Primer Type": None,
    "Powder Type": None,
    "Powder Weight (grains)": None,
    "Trimmed Case Length (in)": None,
    "OAL Length (in)": None
}

entries = {}

for idx, (label, var) in enumerate(fields.items()):
    tk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=idx, column=1, padx=10, pady=5)
    entries[label] = entry

# Assign entries for easier access
bullet_name_entry = entries["Bullet Name"]
bullet_weight_entry = entries["Bullet Weight (grains)"]
brass_name_entry = entries["Brass Name"]
primer_type_entry = entries["Primer Type"]
powder_type_entry = entries["Powder Type"]
powder_weight_entry = entries["Powder Weight (grains)"]
trimmed_length_entry = entries["Trimmed Case Length (in)"]
oal_length_entry = entries["OAL Length (in)"]

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=len(fields), column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()