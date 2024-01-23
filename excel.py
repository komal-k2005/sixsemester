import cv2
from pyzbar.pyzbar import decode
import sqlite3
from openpyxl import Workbook, load_workbook

# Function to scan QR code from an image
def scan_qr_code(image_path):
    image = cv2.imread(image_path)
    barcodes = decode(image)
    if barcodes:
        return barcodes[0].data.decode('utf-8')
    else:
        return None

# Function to update Excel file
def update_excel(file_path, data):
    try:
        workbook = load_workbook(file_path)
        sheet = workbook.active
        sheet.append([data])  # Assuming 'data' is a list of values to be added
        workbook.save(file_path)
        print("Excel updated successfully.")
    except Exception as e:
        print(f"Error updating Excel: {e}")

# Function to interact with the database
def store_in_database(data):
    conn = sqlite3.connect('your_database.db')  # Use your database details
    cursor = conn.cursor()
    
    # Example: Assuming a table 'qr_data' with a column 'info'
    cursor.execute("INSERT INTO qr_data (info) VALUES (?)", (data,))
    
    conn.commit()
    conn.close()

# Example usage
image_path = 'path/to/your/image.png'
scanned_data = scan_qr_code(image_path)

if scanned_data:
    store_in_database(scanned_data)
    update_excel('your_excel_file.xlsx', scanned_data)
else:
    print("No QR code found.")
