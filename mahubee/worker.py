
import os
import uuid

from abc import ABC, abstractmethod




class Bee(ABC):
    
    def __init__(self, *args, **kwargs):
        print("here")

    # Factory method
    @abstractmethod
    def set_duties(self):
        pass

    def run(self):
        assignements = self.set_duties()
        result = assignements.start()
        return result


class Worker(Bee):

    def __init__(self,worker_name, worker_folder_path, worker_workspace_path):
        
        self.id = uuid.uuid4()
        self.name = worker_name
        self.worker_path = f"{worker_folder_path}/{self.name}"
        self.worker_workspace_path = worker_workspace_path
        self._set_up_workspace()
      

    def _set_up_workspace(self):
      
        self.worker_dir = f"{self.worker_workspace_path}/{self.name}"
        
        if not os.path.exists(self.worker_dir):
            print(f"the {self.name} directory does not exist in workspace: ")
            print(f"creating {self.name} directory in workspace")
            os.mkdir(self.worker_dir)
        
        self.worker_id_dir = f"{self.worker_dir}/{str(self.id)}"
        
        if os.path.exists(self.worker_id_dir):
            os.removedirs(self.worker_id_dir)
        os.mkdir(self.worker_id_dir)
        
   

    # factory method
    def set_duties(self, duties):
       
        return duties
       
    
