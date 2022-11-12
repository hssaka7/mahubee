
import uuid
from .utils import parse_config

class Manager():
    def __init__(self,hive_config, worker_name, worker_config_path ):
        manager_id = uuid.uuid4()
        self.validate_hive_config(hive_config)
        self._create_work_space(worker_name,worker_config_path, manager_id)
        self.validate_worker_config(worker_name, worker_config_path)
        
        # TODO create duties,
        # TODO create duties graph
        # TODO create workspace,
        # TODO run each duty
    def _create_work_space( target_name , duties_config_path, manager_id):
        pass


    def validate_hive_config(self, hive_config):
        pass
        
    
    def validate_worker_config(self, worker_name, worker_config):
        pass

