import os
import sys

try:
    directory_path = sys.argv[1]
    total_size = 0

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            total_size += file_size

    print(f"MARIMEA TOTALA: {total_size} BYTES")

except IndexError:
    print("INTRODU PATH-UL IN TERMINAL.")

except FileNotFoundError:
    print("NU S-A GASIT DIRECTORUL.")

except PermissionError:
    print("SORRY, N-AI ACCES.")

except Exception as e:
    print(f"UPS, EROARE: {e}")

# Run in terminal:
# python 3.py C:\Users\dasca\Desktop\GREEN_GUM\PYTHON\LAB_6\3
