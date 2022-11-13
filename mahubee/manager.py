
import os
import uuid
from .utils import parse_config

class Manager():
    def __init__(self,config, worker_name ):

        self.manager_id = uuid.uuid4()
        self.config= config

        # TODO should be allowed to run more than one worker in parallel, but lets implement one first
        self.worker_name = worker_name

        

        self._create_work_space()
      
        
        # TODO create duties,
        # TODO create duties graph
        # TODO create workspace,
        
    def _create_work_space(self):
        workspace_path = self.config['workspace']['path']
        print(workspace_path)
        print("here")
        
        
        # create workerspace directory

        


    def run ():
        # TODO run each duty
        pass

