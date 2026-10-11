
import os

from Task1 import AdvancedFileOps


class LogAggregator(AdvancedFileOps):

    def __init__(self, log_dir):

        self.log_dir = log_dir
        super().__init__(os.path.join(log_dir, "aggregated_logs.txt"))

    def aggregate_logs(self):
        open(self.filepath, "a").close()
        paths = os.listdir(self.log_dir)
        files = [f for f in paths if os.path.isfile(os.path.join(self.log_dir, f)) and f.endswith(".log")]
        if not files:
            raise FileExistsError("No log files found")
        for file in files:
            file_path = os.path.join(self.log_dir, file)
            with open(file_path, "r") as f:
                data = f.read()
                self.write_file(data=data)

if __name__=="__main__":
    path = input("enter the directory :")
    try:
        log_aggregator = LogAggregator(path)
        log_aggregator.aggregate_logs()
    except FileExistsError as error:
        print(f"File Error: {error}")
    except (IOError, OSError) as error:
        print(f"Access Error: {error}")
    else:
        print("Successfully aggregated logs.")