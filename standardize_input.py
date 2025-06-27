"""
The data sets from kaggle use different class identifications

This python file normalises the class_id and class names to:
    names: ["gun", "knife"]
"""

import os

def return_corrected_class(string_number):
    if int(string_number) == 0:
        return "1"
    else:
        return "0"

def swap_class_identifications(data_path):
    lines = []
    for label_file in os.listdir(data_path):

        if not label_file[-4:] == ".txt":
            pass

        txt_file_path = os.path.join(data_path, label_file)

        with open(txt_file_path, "r") as f:
            lines = f.readlines()
        
        # if the text file is empty it means the picture does not contain the object
        if len(lines) == 0:
            continue

        # switch the class identification
        elements = lines[0].strip().split()
        class_id = elements[0]
        elements[0] = return_corrected_class(class_id)

        # now change the value in the text file
        updated_txt = " ".join(elements) + "\n"

        with open(txt_file_path, 'w') as f:
            f.writelines(updated_txt)


def main():
    directories = []

    print("Enter the directory names in order")

    while True:
        directory = input(">>").strip()

        if directory == 'done':
            break

        if directory:
            directories.append(directory)

    data_path = "."
    for path in directories:
        data_path += f"/{path}"

    swap_class_identifications(data_path)

if __name__=='__main__':
    main()