import tkinter as tk
from tkinter import messagebox
import pandas as pd
import openpyxl
import os
from datetime import datetime

# Function to handle form submission and save to Excels
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

        # Convert numeric fields to float (if applicable)
        try:
            bullet_weight = float(bullet_weight)
            powder_weight = float(powder_weight)
            trimmed_length = float(trimmed_length)
            oal_length = float(oal_length)
        except ValueError:
            messagebox.showerror("Input Error", "Please ensure that the numeric fields contain valid numbers.")
            return

        # Get the current date
        current_date = datetime.now().strftime('%Y-%m-%d')

        # Store the data in a dictionary, including the date
        data = {
            'Date': [current_date],  # Add the current date to the data
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
            # Load existing workbook
            book = openpyxl.load_workbook(file_name)
            sheet = book.active

            # Find the next available row
            next_row = sheet.max_row + 1

            # Append data to the Excel file (without headers)
            for row in df.itertuples(index=False, name=None):
                for col, value in enumerate(row, start=1):
                    sheet.cell(row=next_row, column=col, value=value)
                next_row += 1  # Move to the next row
            book.save(file_name)
        else:
            # If the file doesn't exist, write data with headers
            df.to_excel(file_name, index=False)

        messagebox.showinfo("Data Submitted", "Data has been logged successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Ammo Reloading Data Entry")

# Set a minimum size for the window
root.geometry("400x420")  # Adjust size as needed

# Define a common width for all input fields
common_width = 20

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
    tk.Label(root, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root, width=common_width)  # Set width to match the Notes field
    entry.grid(row=idx, column=1, padx=10, pady=5, sticky="w")
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

# Add Notes field (multi-line Text widget) with the same width as the Entry fields
tk.Label(root, text="Notes").grid(row=len(fields), column=0, padx=10, pady=5, sticky="e")
notes_entry = tk.Text(root, height=3, width=27)  # Set width to match Entry fields
notes_entry.grid(row=len(fields), column=1, padx=10, pady=5, sticky="w")

# Add Submit button with better centering
submit_button = tk.Button(root, text="Submit", command=submit_data)

# Make sure the button spans both columns and is centered
submit_button.grid(row=len(fields)+1, column=0, columnspan=2, pady=20, padx=20, sticky="ew")

# Start the main event loop
root.mainloop()