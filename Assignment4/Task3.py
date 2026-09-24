"""This file contains system_navigator() which takes a directory path as input and returns a dictionary containing the number of files in the directory and subdirectories, python version, and platform details"""

import os
import sys

def system_navigator(directory_path: str) -> dict:
    """Takes a directory path as input and returns a dictionary containing the number of files, python version, and platform details"""

    num_files = 0
    for root, dirs, files in os.walk(directory_path):
        num_files += len(files)

    python_version = sys.version
    platform_details = sys.platform
    return {
        "num_files": num_files,
        "python_version": python_version,
        "platform_details": platform_details
    }

if __name__ == "__main__":
    given_input = input("enter a directory path: ")
    analytics = system_navigator(given_input)
    print(f"The number of files in the directory is {analytics['num_files']}")
    print(f"The python version is {analytics['python_version']}")
    print(f"The platform details are {analytics['platform_details']}")