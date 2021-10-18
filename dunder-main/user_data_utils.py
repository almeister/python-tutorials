import os
import pathlib
import folder_scanner


def load_user_data(file_path):
    print(f"Loading user data from {file_path.name}...")


def main():
    examples_folder = os.path.join(os.getcwd(), "examples")
    files = folder_scanner.get_files_in_folder(examples_folder)
    for file in files:
        file_extension = pathlib.Path(file).suffix
        if file_extension == ".json":
            load_user_data(file)


main()

print("user_data_utils.py module name is : " + __name__)
