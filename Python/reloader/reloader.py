import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import openpyxl
import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# Function to save data to PDF
def save_to_pdf():
    try:
        # Get the latest submission data
        bullet_name = bullet_combobox.get()
        bullet_weight = bullet_weight_entry.get()
        brass_name = brass_name_entry.get()
        primer_type = primer_type_entry.get()
        powder_type = powder_type_entry.get()
        powder_weight = powder_weight_entry.get()
        oal_length = oal_length_entry.get()
        trimmed_length = trimmed_length_entry.get() if case_trimmed_var.get() == 1 else "N/A"
        notes = notes_entry.get("1.0", tk.END).strip()
        operator = operator_combobox.get()
        caliber = caliber_combobox.get()
        case_trimmed = "X" if case_trimmed_var.get() == 1 else "No"

        # Get the current date
        current_date = datetime.now().strftime('%Y-%d-%m')

        # Create a new PDF file name with the date included
        pdf_file_name = f"reloaded_ammo_{bullet_name}_{current_date}.pdf"

        # Create a new PDF
        pdf_file = canvas.Canvas(pdf_file_name, pagesize=A4)
        pdf_file.setFont("Helvetica", 12)

        # Add information to the PDF
        pdf_file.drawString(100, 800, f"Hleðsluupplýsingar")
        pdf_file.drawString(100, 780, f"Dags: {current_date}")
        pdf_file.drawString(100, 760, f"Nafn kúlu: {bullet_name}")
        pdf_file.drawString(100, 740, f"Þyngd kúlu: {bullet_weight} grains")
        pdf_file.drawString(100, 720, f"Patróna: {brass_name}")
        pdf_file.drawString(100, 700, f"Primer: {primer_type}")
        pdf_file.drawString(100, 680, f"Púður: {powder_type}")
        pdf_file.drawString(100, 660, f"Púður þyngd: {powder_weight} grains")
        pdf_file.drawString(100, 640, f"OAL lengd: {oal_length} in")
        pdf_file.drawString(100, 620, f"Stytt í lengd: {trimmed_length}")
        pdf_file.drawString(100, 600, f"Patróna stytt: {case_trimmed}")
        pdf_file.drawString(100, 580, f"Caliber: {caliber}")
        pdf_file.drawString(100, 560, f"Nafn: {operator}")
        pdf_file.drawString(100, 540, f"Athugasemdir: {notes}")

        # Save and close the PDF file
        pdf_file.save()

        messagebox.showinfo("PDF Saved", f"PDF saved as '{pdf_file_name}' successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")





# Function to handle form submission and save to Excel
def submit_data():
    try:
        bullet_name = bullet_combobox.get()
        bullet_weight = bullet_weight_entry.get()
        brass_name = brass_name_entry.get()
        primer_type = primer_type_entry.get()
        powder_type = powder_type_entry.get()
        powder_weight = powder_weight_entry.get()
        oal_length = oal_length_entry.get()
        trimmed_length = trimmed_length_entry.get() if case_trimmed_var.get() == 1 else ""  # Only get trimmed length if enabled
        operator = operator_combobox.get()
        caliber = caliber_combobox.get()  # Get selected caliber
        notes = notes_entry.get("1.0", tk.END).strip()
        
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

def load_bullets():
    if os.path.exists("bullets.txt"):
        with open("bullets.txt", "r") as f:
            bullets = [line.strip() for line in f.readlines()]
    else:
        # Default bullets if the file doesn't exist
        bullets = ["Bullet A", "Bullet B", "Bullet C"]
    return bullets

# Function to save bullets to the bullets.txt file
def save_bullets(new_bullet):
    bullets = load_bullets()
    if new_bullet not in bullets:
        bullets.append(new_bullet)
        with open("bullets.txt", "w") as f:
            for bullet in bullets:
                f.write(bullet + "\n")
        # Update the dropdown list
        bullet_combobox['values'] = bullets
        messagebox.showinfo("Success", f"Bullet '{new_bullet}' added successfully!")
    else:
        messagebox.showwarning("Duplicate", f"The bullet '{new_bullet}' already exists!")

# Function to add a new bullet
def add_bullet():
    new_bullet = new_bullet_entry.get().strip()
    if new_bullet:
        save_bullets(new_bullet)
        new_bullet_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid bullet name.")

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
root.geometry("450x800")

# Bullet dropdown (Combobox) at the top
tk.Label(root, text="Bullet Name").grid(row=0, column=0, padx=10, pady=5, sticky="e")
bullets = load_bullets()  # Load bullets from file
bullet_combobox = ttk.Combobox(root, values=bullets, state="readonly")
bullet_combobox.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Input field and button to add a new bullet at the top
tk.Label(root, text="Add New Bullet").grid(row=1, column=0, padx=10, pady=5, sticky="e")
new_bullet_entry = tk.Entry(root)
new_bullet_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

add_bullet_button = tk.Button(root, text="Add Bullet", command=add_bullet)
add_bullet_button.grid(row=2, column=1, padx=5, pady=5)

# Create and place other labels and entry fields starting from row 3
fields = {
    "Bullet Weight (grains)": None,
    "Brass Name": None,
    "Primer Type": None,
    "Powder Type": None,
    "Powder Weight (grains)": None,
    "OAL Length (in)": None
}

entries = {}

for idx, (label, var) in enumerate(fields.items()):
    tk.Label(root, text=label).grid(row=idx+3, column=0, padx=10, pady=5, sticky="e")
    entry = tk.Entry(root)
    entry.grid(row=idx+3, column=1, padx=10, pady=5, sticky="w")
    entries[label] = entry

# Assign entries for easier access
bullet_weight_entry = entries["Bullet Weight (grains)"]
brass_name_entry = entries["Brass Name"]
primer_type_entry = entries["Primer Type"]
powder_type_entry = entries["Powder Type"]
powder_weight_entry = entries["Powder Weight (grains)"]
oal_length_entry = entries["OAL Length (in)"]

# Case trimming checkbox
case_trimmed_var = tk.IntVar()  # This will be 1 if checked, 0 if unchecked
tk.Label(root, text="Case trimming").grid(row=len(fields)+3, column=0, padx=10, pady=5, sticky="e")
hylki_stytt_checkbox = tk.Checkbutton(root, text="Case trimmed", variable=case_trimmed_var, command=toggle_trimmed_length)
hylki_stytt_checkbox.grid(row=len(fields)+3, column=1, padx=10, pady=5, sticky="w")

# Trimmed Case Length field
tk.Label(root, text="Trimmed Case Length (in)").grid(row=len(fields)+4, column=0, padx=10, pady=5, sticky="e")
trimmed_length_entry = tk.Entry(root, state="disabled")  # Initially disabled
trimmed_length_entry.grid(row=len(fields)+4, column=1, padx=10, pady=5, sticky="w")

# Operator dropdown (Combobox)
tk.Label(root, text="Operator").grid(row=len(fields)+5, column=0, padx=10, pady=5, sticky="e")
operator_combobox = ttk.Combobox(root, values=["Arnar Halldórsson", "Benedikt Orri", "Kjartan Magnússon", "Daði Lange"], state="readonly")
operator_combobox.grid(row=len(fields)+5, column=1, padx=10, pady=5, sticky="w")

# Caliber dropdown (Combobox)
tk.Label(root, text="Caliber").grid(row=len(fields)+6, column=0, padx=10, pady=5, sticky="e")
calibers = load_calibers()  # Load calibers from file
caliber_combobox = ttk.Combobox(root, values=calibers, state="readonly")
caliber_combobox.grid(row=len(fields)+6, column=1, padx=10, pady=5, sticky="w")

# Input field and button to add a new caliber
tk.Label(root, text="Add New Caliber").grid(row=len(fields)+7, column=0, padx=10, pady=5, sticky="e")
new_caliber_entry = tk.Entry(root)
new_caliber_entry.grid(row=len(fields)+7, column=1, padx=10, pady=5, sticky="w")

add_caliber_button = tk.Button(root, text="Add Caliber", command=add_caliber)
add_caliber_button.grid(row=len(fields)+8, column=1, padx=5, pady=5) 

# Notes field
tk.Label(root, text="Notes").grid(row=len(fields)+9, column=0, padx=10, pady=5, sticky="e")
notes_entry = tk.Text(root, height=4, width=30)
notes_entry.grid(row=len(fields)+9, column=1, padx=10, pady=5, sticky="w")

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=len(fields)+10, column=0, columnspan=2, pady=20, padx=20, sticky="ew")

# Add a button for saving to PDF
save_pdf_button = tk.Button(root, text="Save to PDF", command=save_to_pdf)
save_pdf_button.grid(row=len(fields)+11, column=0, columnspan=2, pady=5, padx=10)

# Start the main event loop
root.mainloop()