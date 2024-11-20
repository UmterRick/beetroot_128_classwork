import os.path
import shutil
import time


class FileBackupManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.backup_path = filepath + ".bak"


    def __enter__(self):
        if os.path.exists(self.filepath):
            shutil.copy(self.filepath, self.backup_path)
        return open(self.filepath, 'a+')

    def __exit__(self, exc_type, exc_val, exc_tb):
        time.sleep(2)
        if exc_type:
            if os.path.exists(self.backup_path):
                shutil.move(self.backup_path, self.filepath)
        else:
            if os.path.exists(self.backup_path):
                os.remove(self.backup_path)



with FileBackupManager("test_manager.txt") as file:
    content = file.read()
    content += "New data"
    file.write(content)
    # raise ValueError

