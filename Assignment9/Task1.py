import mmap
import os

class AdvancedFileOps:
    def __init__(self, filepath:str):
        self.filepath = filepath
    
    def read_file(self):
        if os.path.exists(self.filepath):
            buffer_size = self.optimize_buffer()
            with open(self.filepath, "r", buffering=buffer_size) as file:
                print(f"read data is: {file.readlines()}")
        else:
            print("File doesn't exist")
            return

    def write_file(self, data:str):
        if os.path.exists(self.filepath):
            buffer_size = self.optimize_buffer()
            with open(self.filepath, "a", buffering=buffer_size) as file:
                file.write(data)
            print(f"file is been appended with {data}")
        else:
            print("file doesn't exist to write data")

    def handle_large_file(self, operation:str, data:str):
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
