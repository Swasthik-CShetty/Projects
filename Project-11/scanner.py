import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import cv2
import numpy as np
import os
import json
from PIL import Image, ImageTk

# Class for biometric system
class BiometricSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Fingerprint Biometric Identification System")
        self.root.geometry("800x600")

        self.db_file = "biometric_database.json"
        self.biometric_db = self.load_database()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        # Enrollment Tab
        self.fingerprint_enrollment_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.fingerprint_enrollment_tab, text="Fingerprint Enrollment")
        self.setup_fingerprint_enrollment_tab()

        # Verification Tab
        self.fingerprint_verification_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.fingerprint_verification_tab, text="Fingerprint Verification")
        self.setup_fingerprint_verification_tab()

    # Load Database
    def load_database(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r') as file:
                    return json.load(file)
            except:
                return {}
        else:
            return {}

    # Save data to database file
    def save_database(self):
        with open(self.db_file, 'w') as file:
            json.dump(self.biometric_db, file)

    # ---------------- Enrollment Form ----------------
    def setup_fingerprint_enrollment_tab(self):
        form_frame = ttk.LabelFrame(self.fingerprint_enrollment_tab, text="User Information")
        form_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=10, pady=10)

        ttk.Label(form_frame, text="ID:").grid(row=0, column=0, sticky=tk.W)
        self.fp_id_entry = ttk.Entry(form_frame)
        self.fp_id_entry.grid(row=0, column=1)

        ttk.Label(form_frame, text="Name:").grid(row=1, column=0, sticky=tk.W)
        self.fp_name_entry = ttk.Entry(form_frame)
        self.fp_name_entry.grid(row=1, column=1)

        ttk.Label(form_frame, text="Gender:").grid(row=2, column=0, sticky=tk.W)
        self.fp_gender_var = tk.StringVar()
        gender_combo = ttk.Combobox(form_frame, textvariable=self.fp_gender_var, values=("Male","Female","Other"))
        gender_combo.grid(row=2, column=1)

        ttk.Label(form_frame, text="Age:").grid(row=3, column=0, sticky=tk.W)
        self.fp_age_entry = ttk.Entry(form_frame)
        self.fp_age_entry.grid(row=3, column=1)

        fp_frame = ttk.LabelFrame(self.fingerprint_enrollment_tab, text="Fingerprint")
        fp_frame.pack(side=tk.RIGHT, fill='both', expand=True, padx=10, pady=10)

        self.fp_enrollment_image_label = ttk.Label(fp_frame)
        self.fp_enrollment_image_label.pack()

        ttk.Button(fp_frame, text="Upload Fingerprint", command=self.upload_fingerprint).pack(pady=10)
        ttk.Button(fp_frame, text="Enroll User", command=self.enroll_fingerprint_user).pack(pady=10)

        self.enrollment_fingerprint = None

    # Upload fingerprint image
    def upload_fingerprint(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            self.enrollment_fingerprint = self.process_fingerprint(img)

            img_display = Image.open(file_path).resize((200,200))
            img_tk = ImageTk.PhotoImage(img_display)
            self.fp_enrollment_image_label.configure(image=img_tk)
            self.fp_enrollment_image_label.image = img_tk

            messagebox.showinfo("Success", "Fingerprint uploaded successfully!")

    # Convert fingerprint to simple feature hash
    def process_fingerprint(self, img):
        img = cv2.resize(img, (200,200))
        img = cv2.equalizeHist(img)
        thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
        return hash(thresh.tobytes())

    # Save user fingerprint to database
    def enroll_fingerprint_user(self):
        if not self.enrollment_fingerprint:
            messagebox.showerror("Error", "Please upload a fingerprint first!")
            return

        user_id = self.fp_id_entry.get().strip()
        name = self.fp_name_entry.get().strip()
        gender = self.fp_gender_var.get().strip()
        age = self.fp_age_entry.get().strip()

        if not user_id or not name or not gender or not age:
            messagebox.showerror("Error", "All fields are required!")
            return

        self.biometric_db[user_id] = {
            "name": name,
            "gender": gender,
            "age": age,
            "fingerprint": self.enrollment_fingerprint
        }

        self.save_database()
        messagebox.showinfo("Success", f"User {name} enrolled successfully!")

    # ---------------- Verification Tab ----------------
    def setup_fingerprint_verification_tab(self):
        verify_frame = ttk.LabelFrame(self.fingerprint_verification_tab, text="Verify Fingerprint")
        verify_frame.pack(side=tk.LEFT, fill='both', expand=True, padx=10, pady=10)

        self.fp_verification_image_label = ttk.Label(verify_frame)
        self.fp_verification_image_label.pack()

        ttk.Button(verify_frame, text="Upload Fingerprint", command=self.upload_verification_fingerprint).pack(pady=10)
        ttk.Button(verify_frame, text="Verify Identity", command=self.verify_fingerprint).pack(pady=10)

        results_frame = ttk.LabelFrame(self.fingerprint_verification_tab, text="Results")
        results_frame.pack(side=tk.RIGHT, fill='both', expand=True, padx=10, pady=10)

        self.fp_result_text = tk.Text(results_frame, height=20, width=40)
        self.fp_result_text.pack()

        self.verification_fingerprint = None

    # Upload fingerprint for verification
    def upload_verification_fingerprint(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files","*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            self.verification_fingerprint = self.process_fingerprint(img)

            img_display = Image.open(file_path).resize((200,200))
            img_tk = ImageTk.PhotoImage(img_display)
            self.fp_verification_image_label.configure(image=img_tk)
            self.fp_verification_image_label.image = img_tk

            messagebox.showinfo("Success", "Fingerprint uploaded")

    # Compare fingerprints using hash match
    def verify_fingerprint(self):
        if not self.verification_fingerprint:
            messagebox.showerror("Error", "Upload a fingerprint to verify!")
            return

        for uid, user in self.biometric_db.items():
            if user["fingerprint"] == self.verification_fingerprint:  # simple match
                self.fp_result_text.delete("1.0", tk.END)
                self.fp_result_text.insert(tk.END, f"✅ USER IDENTIFIED\n\nID: {uid}\nName: {user['name']}\nGender: {user['gender']}\nAge: {user['age']}")
                return

        self.fp_result_text.delete("1.0", tk.END)
        self.fp_result_text.insert(tk.END, "❌ No match found")

# Run program
if __name__ == "__main__":
    root = tk.Tk()
    app = BiometricSystem(root)
    root.mainloop()
