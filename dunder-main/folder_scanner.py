import os


def get_files_in_folder(folder):
    files_found = []
    with os.scandir(folder) as iterator:
        for item in iterator:
            if os.DirEntry.is_file(item):
                files_found.append(item)

    return files_found


def main():
    # Get path to current folder (where the script is)
    search_folder = os.getcwd()

    print(f"\nFiles in {search_folder}:")
    files = get_files_in_folder(search_folder)
    for file in files:
        print(f"\t{file.name}")

if __name__ == "__main__":
    main()

print("folder_scanner.py module name is : " + __name__)