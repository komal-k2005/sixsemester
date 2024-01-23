import tkinter as tk
from tkinter import messagebox
import sqlite3
import qrcode

# Database setup (using SQLite for simplicity)
conn = sqlite3.connect('student_database.db')
cursor = conn.cursor()

# Create the student table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        student_id TEXT NOT NULL,
        contact_number TEXT,
        other_info TEXT
    )
''')
conn.commit()

# Function to generate QR code
def generate_qr_code(student_id):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(student_id)
    qr.make(fit=True)
    qr_code = qr.make_image(fill_color="black", back_color="white")
    qr_code.save(f"{student_id}_qr.png")

# Function to add a new student
def add_student():
    name = entry_name.get()
    student_id = entry_student_id.get()
    contact_number = entry_contact.get()
    other_info = entry_other.get()

    # Check if the student ID already exists
    cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    existing_student = cursor.fetchone()

    if existing_student:
        messagebox.showerror("Error", "Student ID already exists!")
    else:
        # Insert the student into the database
        cursor.execute('''
            INSERT INTO students (name, student_id, contact_number, other_info)
            VALUES (?, ?, ?, ?)
        ''', (name, student_id, contact_number, other_info))
        conn.commit()

        # Generate QR code for the student
        generate_qr_code(student_id)

        messagebox.showinfo("Success", "Student added successfully!")

# Function to search for a student by ID
def search_student():
    student_id = entry_search.get()

    # Retrieve the student from the database
    cursor.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    student = cursor.fetchone()

    if student:
        messagebox.showinfo("Student Details", f"Name: {student[1]}\nContact: {student[3]}\nOther Info: {student[4]}")
    else:
        messagebox.showerror("Error", "Student not found!")

# Create the main application window
app = tk.Tk()
app.title("Virtual Student ID Card System")

# Create and place UI elements
label_name = tk.Label(app, text="Name:")
label_student_id = tk.Label(app, text="Student ID:")
label_contact = tk.Label(app, text="Contact Number:")
label_other = tk.Label(app, text="Other Information:")
label_search = tk.Label(app, text="Search by Student ID:")

entry_name = tk.Entry(app)
entry_student_id = tk.Entry(app)
entry_contact = tk.Entry(app)
entry_other = tk.Entry(app)
entry_search = tk.Entry(app)

button_add_student = tk.Button(app, text="Add Student", command=add_student)
button_search_student = tk.Button(app, text="Search Student", command=search_student)

# Grid layout
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_name.grid(row=0, column=1, padx=10, pady=5)
label_student_id.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_student_id.grid(row=1, column=1, padx=10, pady=5)
label_contact.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry_contact.grid(row=2, column=1, padx=10, pady=5)
label_other.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
entry_other.grid(row=3, column=1, padx=10, pady=5)
label_search.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
entry_search.grid(row=4, column=1, padx=10, pady=5)
button_add_student.grid(row=5, column=1, pady=10)
button_search_student.grid(row=5, column=2, pady=10)

# Start the application
app.mainloop()

# Close the database connection
conn.close()
