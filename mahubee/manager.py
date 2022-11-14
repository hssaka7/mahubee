
import os
import uuid
from .utils import parse_config
from .worker import Worker

class Manager():
    def __init__(self,config, worker_name ):

        self.manager_id = uuid.uuid4()
        self.config= config

        # TODO should be allowed to run more than one worker in parallel, but lets implement one first
        self.worker_name = worker_name
        
        self._create_work_space()

        self._set_up_worker()
        
        # TODO create duties,
        # TODO create duties graph
        # TODO create workspace,
        
    def _create_work_space(self):
        
        workspace_path = self.config['workspace']['path']
        print(workspace_path)
  
        # if workspace_path does not exist
        if not os.path.exists(workspace_path):
            print("the workspace directory does not exist")
            exit()
        
        self.worker_workspcae_path = f"{workspace_path}/worker"
        if not os.path.exists(self.worker_workspcae_path):
            print(f"the worker directory does not exist in workspace: ")
            print("creating worker directory in workspace")
            os.mkdir(self.worker_workspcae_path)
    
    def _set_up_worker(self):
        worker_path = self.config['worker']['path']
        worker = Worker(self.worker_name, worker_path,self.worker_workspcae_path)
        print("here")



        
    def create_dependency_graph(self):
        # TODO creates the duties dependency graph, but to start with, do all in exact order.

        pass

        


    def run (self):
        # TODO run Workers
        self._set_up_worker()


