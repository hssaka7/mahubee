from abc import ABC, abstractmethod

# TODO file must be saved on the temp directoly, unless persisted. other should be deleted. How to delete?

class FileState():
    def __init__(self,file_name=None, content=None):
        
        if  not (file_name and content):
            # how to create empty file
            print("Empty file")
        self.file_name = file_name
        
        # need workspace folder
        temp_workspace_folder = '/mnt/e/source/mahuri_hive'
        self._file_path = f'{temp_workspace_folder}/{file_name}'
        self.save(content)

    
    def save(self, content):
        with open(self._file_path, 'w') as file:
            file.write(content)

    
    def open (self, mode = 'r'):
        return open(self._file_path, mode)
            


if __name__ == '__main__':
    import pandas as pd
    df = pd.DataFrame([[100,200,300],[123,123,123],[4,5,6],])
    
    f = FileState('test_file_state.json', df.to_json())
    with f.open() as input_stream:
        print(f.file_name)
        df =pd.read_json(input_stream)

        print("Success")
        


    