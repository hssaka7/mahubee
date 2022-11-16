
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

    def _create_duties(self):

        
        # TODO check if the depends vlaue is in duties name
        # set of depends must be the subser of names
         # TODO the duties can have its own iterator class based on the dependency 
        
        # create_duty

        worker_path = self.config['worker']['path']
        worker_config = parse_config(f'{worker_path}/{self.worker_name}/config.yaml')
        duties_config = worker_config['duties']

        duties_obj = []

        for d_config in duties_config:
            class_name_info= d_config['class_name']
            file_name, class_name,*_= class_name_info.split('.')
            
            if file_name == 'mahubee':
                mod = None
                # TODO generic functions
                pass

            else:
                # TODO workers path must be determined from the mahubee config

                mod = __import__(f'workers.{self.worker_name}.{file_name}')
                mod = getattr(mod,self.worker_name)
                # feed should be parsed from the class name
                mod = getattr(mod,file_name)
                mod = getattr(mod,class_name)
               
            
            duty_instance = mod(**d_config)
            duties_obj.append(duty_instance)

        return duties_obj
    
    def _set_up_workers(self):

       # TODO can have more than one worker if the job is big and assign duties parallely

        worker_path = self.config['worker']['path']
        worker_config = parse_config(f'{worker_path}/{self.worker_name}/config.yaml')

        duties = self._create_duties()
        
        worker = Worker(self.worker_name, worker_path,self.worker_workspcae_path, duties)

        return worker
        

    def run (self):
        
        self._create_work_space()
        worker = self._set_up_workers() 
        r = worker.run()
        
        print("Complete")

    


