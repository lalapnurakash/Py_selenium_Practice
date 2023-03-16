import os
import shutil

class file:
    def createfile(self,directory):
        # if file exists remove and recreate
        if os.path.exists(directory):
            shutil.rmtree(directory)
            os.makedirs(directory)
        else:
            os.makedirs(directory)
            print("file created")

    def moveFiles(self,source,to):
        for file_name in os.listdir(source):
            src_path = os.path.join(source,file_name)
            dst_path = os.path.join(to, file_name)
            shutil.move(src_path, dst_path)
