"""This module provides advanced file operations including reading, writing, and handling large files using memory mapping."""
import mmap
import os

class AdvancedFileOps:
    """Class to perform advanced file operations such as reading, writing, and handling large files."""
    def __init__(self, filepath:str):
        self.filepath = filepath
    
    def read_file(self):
        """Reads the content of the file specified by the filepath. If the file exists, it reads the data using an optimized buffer size and prints the content. If the file does not exist, it prints an error message."""
        if os.path.exists(self.filepath):
            buffer_size = self.optimize_buffer()
            with open(self.filepath, "r", buffering=buffer_size) as file:
                print(f"read data is: {file.readlines()}")
        else:
            print("File doesn't exist")
            return

    def write_file(self, data:str):
        """Writes the provided data to the file specified by the filepath. If the file exists, it appends the data using an optimized buffer size. If the file does not exist, it prints an error message."""
        if os.path.exists(self.filepath):
            buffer_size = self.optimize_buffer()
            with open(self.filepath, "a", buffering=buffer_size) as file:
                file.write(data)
            print(f"file is been appended with {data}")
        else:
            print("file doesn't exist to write data")

    def handle_large_file(self, operation:str, data:str):
        """Handles large files using memory mapping. Depending on the operation specified ('read' or 'write'), it either reads the content of the file or appends data to it. If the operation is invalid, it prints an error message."""
        if operation == "read":
            try:
                with open(self.filepath, "r") as file:
                    with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mmap_file :
                        for line in file:
                            print(line.strip())
            except Exception as e:
                print(f"Error reading large file: {e}")
        elif operation == "write":
            try:
                with open(self.filepath, "r+") as file:
                    with mmap.mmap(file.fileno(), 0) as mmap_file:
                        mmap_file.seek(0, os.SEEK_END)
                        mmap_file.resize(mmap_file.size() + len(data.encode("utf-8")))
                        mmap_file.write(data.encode("utf-8"))
                        mmap_file.flush()
            except Exception as e:
                print(f"Error writing to large file: {e}")
        else:
            print("Invalid operation. Use 'read' or 'write'.")

    def optimize_buffer(self):
        """Optimizes the buffer size for reading and writing files. It calculates the buffer size based on the file size, ensuring it is within a specified range (minimum 8KB, maximum 1MB)."""
        minimum_buffer = 8 * 1024
        maximum_buffer = 1024 * 1024
        file_size = os.path.getsize(self.filepath) if os.path.exists(self.filepath) else 0
        return max(minimum_buffer, min(file_size, maximum_buffer))

if __name__== "__main__":
    path = "data.txt"
    fileOps = AdvancedFileOps(path)
    fileOps.read_file()
    fileOps.write_file("soliton")
    fileOps.handle_large_file("read", "empty")
