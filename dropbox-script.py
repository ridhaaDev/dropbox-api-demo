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
    
    def get_previous_path(self):
        return '/'.join(self.get_path().split('/')[:-1])
    
def get_user_command():
    user_input = input(f"""Enter an action to take:
Forward
Back
Download
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
    files_folder_dict = {}
    
    for i, entry in enumerate(result.entries):
        files_folder_dict[i] = entry.path_display
    return files_folder_dict

def print_files_and_folders(files_folder_dict):
    for key, value in files_folder_dict.items():
        print(key, value)

def main():
    file_path = FilePath()
    dbx = dropbox.Dropbox(ACCESS_TOKEN)
    
    while True:
        files_folder_dict = list_file_folders(dbx, file_path.get_path())
        print_files_and_folders(files_folder_dict)
        user_input = get_user_command()
        command_type = user_input.split(" ")[0]

        if command_type == "Download":
            index = int(user_input.split(" ")[1])
            selected_folder = files_folder_dict[index]
            print("Selected")
            print(selected_folder)
        elif command_type == "Forward":
            index = int(user_input.split(" ")[1])
            selected_folder = files_folder_dict[index]

            file_path.set_path(file_path.get_path() + selected_folder)
        elif command_type == "Back":
            new_path = file_path.get_previous_path()
            print("NEW_PATH", new_path)
        elif command_type == "Exit":
            break
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
