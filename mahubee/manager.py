
import os   
import uuid

from .utils import parse_config


from .worker import Worker
from .duty import Capture

class Manager():
    
    def __init__(self,config, worker_name ):

        self.manager_id = uuid.uuid4()
        self.config= config

        # TODO should be allowed to run more than one worker in parallel, but lets implement one first
        self.worker_name = worker_name
        
        self._create_work_space()

        self._set_up_workers() 
        
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
    
    def _set_up_workers(self):

       # TODO can have more than one worker if the job is big and assign duties parallely
        worker_path = self.config['worker']['path']
        worker_config = parse_config(f'{worker_path}/{self.worker_name}/config.yaml')
        worker = Worker(self.worker_name, worker_path,self.worker_workspcae_path)
        
        # TODO the duties can have its own iterator class based on the dependency 
        duties_config = worker_config['duties']


        # TODO check if the depends vlaue is in duties name
        # set of depends must be the subser of names
        duty_result_mapper = dict()

        for d in duties_config:
            # pass
            mod = __import__(f'workers.{self.worker_name}.feed')
            mod = getattr(mod,self.worker_name)
            # feed should be parsed from the class name
            mod = getattr(mod,'feed')

            print("here")

        duty_class_name = [(d_con['name'],dd_con['depends']) for d_con in duties_config]
        
       





        # create_duty
        # assign duty to the worker
        # runt he duty and manang the workspace

        print("here")


    def run (self):
        # TODO run Workers
        pass
    


