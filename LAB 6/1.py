import os
import sys

try:
    # Get directory path and file extension from command line arguments
    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    # Check if directory path exists
    if not os.path.exists(directory_path):
        raise Exception("Directory path does not exist")

    # Search for all files with the given extension in the specified directory
    for file_name in os.listdir(directory_path):
        if file_name.endswith(file_extension):
            file_path = os.path.join(directory_path, file_name)

            # Read file contents and print them
            with open(file_path, "r") as file:
                print(file.read())

except IndexError:
    print("Please provide directory path and file extension as command line arguments")

except Exception as e:
    print(e)
