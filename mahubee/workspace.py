from abc import ABC, abstractmethod

# TODO file must be saved on the temp directoly, unless persisted. other should be deleted. How to delete?

class FileState():
    def __init__(self,file_path=None, content=None, metadata = None):
        
        if  not (file_path and content):
            # how to create empty file
            print("Empty file")
        
        self.file_path = file_path
        self.metadata = metadata if bool(metadata) else dict()
        # need workspace folder

        self.save(content)

    
    def save(self, content):
        with open(self.file_path, 'w') as file:
            file.write(content)

    
    def open (self, mode = 'r'):
        return open(self.file_path, mode)
            


# if __name__ == '__main__':
    
    
#     import pandas as pd


#     df = pd.DataFrame([[100,200,300],[123,123,123],[4,5,6],])
    
#     f = FileState('test_file_state.json', df.to_json())
#     with f.open() as input_stream:
#         print(f.file_name)
#         df =pd.read_json(input_stream)

#         print("Success")
        


    