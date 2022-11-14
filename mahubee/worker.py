import os
import uuid

from .utils import parse_config

class Worker:

    def __init__(self,worker_name, worker_folder_path, worker_workspace_path):
        
        self.worker_id = uuid.uuid4()
        self.worker_name = worker_name
        self.worker_path = f"{worker_folder_path}/{self.worker_name}"
        self.worker_workspace_path = worker_workspace_path
        self._set_up_workspace()
        self.config = self._setup_config()

        print("here")

    def _set_up_workspace(self):
      
        self.worker_dir = f"{self.worker_workspace_path}/{self.worker_name}"
        
        if not os.path.exists(self.worker_dir):
            print(f"the {self.worker_name} directory does not exist in workspace: ")
            print(f"creating {self.worker_name} directory in workspace")
            os.mkdir(self.worker_dir)
        
        self.worker_id_dir = f"{self.worker_dir}/{str(self.worker_id)}"
        
        if os.path.exists(self.worker_id_dir):
            os.removedirs(self.worker_id_dir)
        os.mkdir(self.worker_id_dir)
        
    def _setup_config(self):
        config = parse_config(f'{self.worker_path}/config.yaml')
        return config


    def create_duties_dependency_graph(self):
        # TODO creates the duties dependency graph, but to start with, do all in exact order.
        
        pass


    def run(self):
        # TODO run duties

        pass
