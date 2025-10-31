# Fingerprint Biometric Identification System

This repository contains a simple Fingerprint Biometric Identification System implemented in Python.
The system uses Tkinter for the GUI and OpenCV for image processing. It accepts fingerprint **image uploads only** (no camera required).

## Features
- Enroll users by uploading fingerprint images and entering ID, name, gender, age.
- Verify users by uploading a fingerprint image and matching against the saved database (JSON).
- Beginner-friendly prototype suitable for college projects / learning.

## Technologies
- Python 3
- Tkinter (GUI)
- OpenCV (cv2) for image processing
- NumPy
- Pillow (PIL) for image display
- JSON for simple local storage

## Files
- `scanner.py` - Main application code (GUI + processing).
- `README.md` - Project README.

## Installation
```bash
pip install opencv-python pillow numpy reportlab
```

## Run
```bash
python scanner.py
```

## How it works
1. Enrollment: upload fingerprint image → process image → compute a simple hash → save to JSON with user details.
2. Verification: upload image → compute hash → compare with stored hashes → if equal, user is identified.

## Limitations & Future Work
- Current matching uses exact hash comparison — not robust to rotation, scaling, or noise.
- Future work: ORB/SIFT matching, ML-based matching (CNN/Siamese), live scanner support, encrypted storage, SQL backend.

## License
This project is provided for educational purposes.
