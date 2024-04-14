import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk
import cv2

class QRApp:
    def __init__(self, master):
        self.master = master
        self.master.title("QR Code Generator and Scanner")

        self.qr_data_entry = tk.Entry(master, width=40)
        self.qr_data_entry.grid(row=0, column=0, padx=10, pady=10)

        self.generate_button = tk.Button(master, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.grid(row=0, column=1, padx=5, pady=10)

        self.scan_button = tk.Button(master, text="Scan QR Code", command=self.scan_qr_code)
        self.scan_button.grid(row=0, column=2, padx=5, pady=10)

        self.qr_label = tk.Label(master)
        self.qr_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def generate_qr_code(self):
        data = self.qr_data_entry.get()
        if data:
            qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img_pil = img.get_image()
            img_pil = img_pil.resize((300, 300), Image.NEAREST)
            self.qr_image = ImageTk.PhotoImage(img_pil)
            self.qr_label.config(image=self.qr_image)
        else:
            messagebox.showwarning("Warning", "Please enter data to generate QR code.")

    def scan_qr_code(self):
        camera = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()

        while True:
            _, img = camera.read()
            data, bbox, _ = detector.detectAndDecode(img)
            
            if bbox is not None:
                for i in range(len(bbox)):
                    cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
                if data:
                    messagebox.showinfo("QR Code Scan", f"Scanned Data: {data}")
                    break
            cv2.imshow("QR Code Scanner", img)
            if cv2.waitKey(1) == ord("q"):
                break

        camera.release()
        cv2.destroyAllWindows()

def main():
    root = tk.Tk()
    app = QRApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
