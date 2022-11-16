
import os
import uuid

from abc import ABC, abstractmethod




class Bee(ABC):
    
    
    # Factory method
    @abstractmethod
    def get_duties(self):
        pass

    # TODO duty running logic here
    # dependency graph
    # need to manage the result of each duties and save it in the workspace

    def run(self):


        assignements = self.get_duties()
        
        # Logic for running duties and chaining the results
        
        # for now running linearly, can make it more smart here?
        result = dict()
        for count,assign in enumerate (assignements):
            
            if count == 0 and assign.depends != []:
                 raise Exception ("the first duty must have no dependency")
            
            if assign.depends != []:
                inputs = [result[x] for x in assign.depends]
                assign.set_inputs(inputs=inputs)
            
            result[assign.name] = assign.start()

        return result


class Worker(Bee):

    def __init__(self,worker_name, worker_folder_path, worker_workspace_path, duties):
        
        self.id = uuid.uuid4()
        self.name = worker_name
        self.worker_path = f"{worker_folder_path}/{self.name}"
        self.worker_workspace_path = worker_workspace_path
        self.duties = duties
        self.worker_dir = f"{self.worker_workspace_path}/{self.name}"
        self.worker_id_dir = f"{self.worker_dir}/{str(self.id)}"
        
        self._set_up_workspace()
      

    def _set_up_workspace(self):
      
        # TODO, One folder per worker?? how should this behave?
        
        if not os.path.exists(self.worker_dir):
            print(f"the {self.name} directory does not exist in workspace: ")
            print(f"creating {self.name} directory in workspace")
            os.mkdir(self.worker_dir)
        
        if os.path.exists(self.worker_id_dir):
            os.removedirs(self.worker_id_dir)
        os.mkdir(self.worker_id_dir)
        
   

    # factory method
    def get_duties(self):
        return self.duties
       
    
