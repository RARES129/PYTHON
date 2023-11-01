import os


def unique_sorted_extensions(directory):
    extensions = set()
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            extension = filename.split(".")[-1]
            extensions.add(extension)
    return sorted(list(extensions))


# Example usage:
directory = "C:/Users/dasca/Documents"
unique_extensions = unique_sorted_extensions(directory)
print(unique_extensions)
