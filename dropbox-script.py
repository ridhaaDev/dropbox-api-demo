import dropbox
from decouple import config

ACCESS_TOKEN = config('ACCESS_TOKEN')

import os
script_dir = os.path.dirname(__file__)

class FilePath:
    def __init__(self):
        self.path = ''

    def set_path(self, new_path):
        self.path = new_path
    
    def get_path(self):
        return self.path
    
def get_user_command():
    user_input = input(f"""Enter an action to take:
Download
Forward
Back
Exit

Type a command like 
"Download 0" if you see a file to download a file
"Forward 1 to navigate within a folder"
"Back" to navigate backwards
Command: 
""")
    
    return user_input;

def list_file_folders(dbx, file_path):
    result = dbx.files_list_folder(file_path)
    files_folder_list = {}
    
    for i, entry in enumerate(result.entries):
        files_folder_list[i] = entry.path_display
    return files_folder_list

def print_file_folder_dir(files_folder_dict):
    for key, value in files_folder_dict.items():
        print(key, value)

def main():
    file_path = FilePath()
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    files_folder_list = list_file_folders(dbx, file_path.get_path())
    print_file_folder_dir(files_folder_list)
    
    while True:
        user_input = get_user_command()
        command_type = user_input.split(" ")[0]
        if command_type == "Download":
            index = int(user_input.split(" ")[1])
            selected_folder = files_folder_list[index]
            print("Selected")
            print(selected_folder)
        elif command_type == "Forward":
            index = int(user_input.split(" ")[1])
            selected_folder = files_folder_list[index]

            file_path.set_path(file_path.get_path() + selected_folder)

            print("File path: ")
            print(file_path.get_path())

            list_folders = list_file_folders(dbx, file_path.get_path())

            print("List folders: ")
            print_file_folder_dir(list_folders)
        elif command_type == "Exit":
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
