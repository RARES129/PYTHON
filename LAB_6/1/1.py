import os
import sys

try:
    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    if not os.path.isdir(directory_path):
        raise Exception("PATH INVALID")

    for filename in os.listdir(directory_path):
        if filename.endswith(file_extension):
            file_path = os.path.join(directory_path, filename)
            try:
                with open(file_path, "r") as file:
                    contents = file.read()
                    print(contents)
            except:
                print(f"EROARE LA CITIREA FISIERELOR: {file_path}")
except:
    print("NU I OK CE AI SCRIS IN TERMINAL, INCEARCA IAR")

# run this in terminal:
# python 1.py C:\Users\dasca\Desktop\GREEN_GUM\PYTHON\LAB_6\1 .txt
