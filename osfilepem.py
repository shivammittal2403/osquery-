import os
import datetime

def get_file_info(path):
    """Returns detailed information about a file."""
    file_info = {
        "Path": path,
        "Size (bytes)": os.path.getsize(path),
        "Last Modified": datetime.datetime.fromtimestamp(os.path.getmtime(path)),
        "Last Accessed": datetime.datetime.fromtimestamp(os.path.getatime(path)),
        "Creation Time": datetime.datetime.fromtimestamp(os.path.getctime(path)),
        "Is File": os.path.isfile(path),
        "Is Directory": os.path.isdir(path),
        "Permissions": oct(os.stat(path).st_mode & 0o777),
    }
    return file_info

def explore_directory(directory):
    """Recursively explores a directory and gathers file and directory information."""
    dir_info = {
        "Directory": directory,
        "Contents": []
    }

    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                dir_info["Contents"].append(get_file_info(entry.path))
            elif entry.is_dir():
                sub_dir_info = explore_directory(entry.path)
                dir_info["Contents"].append(sub_dir_info)
    except PermissionError:
        print(f"Permission denied: {directory}")
    
    return dir_info

def print_info(info, indent=0):
    """Pretty prints the collected information."""
    spacing = ' ' * indent
    if 'Directory' in info:
        print(f"{spacing}Directory: {info['Directory']}")
        for item in info["Contents"]:
            if isinstance(item, dict) and 'Path' in item:
                print(f"{spacing}  File: {item['Path']}")
                print(f"{spacing}    Size (bytes): {item['Size (bytes)']}")
                print(f"{spacing}    Last Modified: {item['Last Modified']}")
                print(f"{spacing}    Last Accessed: {item['Last Accessed']}")
                print(f"{spacing}    Creation Time: {item['Creation Time']}")
                print(f"{spacing}    Permissions: {item['Permissions']}")
            elif isinstance(item, dict) and 'Directory' in item:
                print_info(item, indent + 2)

if __name__ == "__main__":
    root_directory = "."  # Change this to the directory you want to explore
    directory_info = explore_directory(root_directory)
    print_info(directory_info)
