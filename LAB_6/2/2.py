import os

# asta trebuie decomentata, dar am lasat o comentata ca sa nu mi mai redenumesc fisierele
# directory_path = "C:/Users/dasca/Desktop/GREEN_GUM/PYTHON/LAB_6/2/fisiere"

if os.path.exists(directory_path):
    files = os.listdir(directory_path)
    files.sort()
    count = 1
    for file in files:
        file_extension = os.path.splitext(file)[1]
        new_file_name = "file" + str(count) + file_extension
        try:
            os.rename(
                os.path.join(directory_path, file),
                os.path.join(directory_path, new_file_name),
            )
            count += 1
        except Exception as e:
            print(f"EROARE PENTRU {file}: {e}")
else:
    print(f"DIRECTORUL {directory_path} NU EXISTA.")
