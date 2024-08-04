import os
import platform
import pprint

def query_os_info():
    # Use environment variable to get the user
    username = os.getenv("USERNAME") if platform.system() == "Windows" else os.getenv("USER")
    
    os_info = {
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Machine Type": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version(),
        "Current Directory": os.getcwd(),
        "User": username,
        "Environment Variables": dict(os.environ)
    }
    
    for key, value in os_info.items():
        if key == "Environment Variables":
            print(f"{key}:")
            pprint.pprint(value, indent=4)  # Pretty print the environment variables dictionary
        else:
            print(f"{key}: {value}")

if __name__ == "__main__":
    query_os_info()
