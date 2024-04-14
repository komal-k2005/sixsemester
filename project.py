import cv2
import qrcode
from pyzbar.pyzbar import decode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def read_qr_code():
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        decoded_objs = decode(frame)
        for obj in decoded_objs:
            return obj.data.decode('utf-8')
        cv2.imshow("QR Code Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def main():
    # Initialize an empty dictionary to store student information
    students = {}

    # Input number of students
    num_students = int(input("Enter the number of students: "))

    # Input student information
    for i in range(num_students):
        roll_number = input(f"Enter roll number for student {i+1}: ")
        name = input(f"Enter name for student {i+1}: ")
        students[roll_number] = name

    # Generate QR code for each student
    for roll_number, name in students.items():
        qr_data = f"Roll Number: {roll_number}\nName: {name}"
        generate_qr_code(qr_data, f"student_{roll_number}_qr.png")
        print(f"QR Code generated for {name} with roll number {roll_number}")

    # Read QR code from camera feed
    print("Please scan the QR code to mark attendance.")
    scanned_data = read_qr_code()

    # Extract roll number from scanned data
    roll_number = scanned_data.split("\n")[0].split(": ")[1]

    # Check if the scanned roll number exists in the students dictionary
    if roll_number in students:
        print(f"Attendance marked for {students[roll_number]} with roll number {roll_number}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    main()
