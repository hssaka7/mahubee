import uuid

from utils import get_argsparser,parse_config, create_workspace_folder



    


# env variables:

WORKSPACE = '/Users/aakashbasnet/development/python/workspace/ml_pipelines'

# manager run 
class Manager:
    def __init__(self, steps):
        id = uuid.uuid4()
        self.steps = steps

        # create id folder for the pipleline
        
        pass
    
def get_steps(p_config):
     # TODO create dependency graph
    step_objs = []
    for step in p_config:
        print(step['name'])
        print(step['depends'])
        print(step['class_name'])
        print("======================")

        _folder, _file, _step = step['class_name'].split('.')
        mod = __import__(f"core.{_folder}.{_file}")
        mod = getattr(mod, _folder)
        mod = getattr(mod, _file)
        mod = getattr(mod, _step)
        obj = mod(**step)
        step_objs.append(obj)


def start():
    # TODO setup loggers

    args = vars(get_argsparser().parse_args())
    pipeline_config= parse_config(f"core/{args['pipeline_config']}")
    
    print (args)
    print(pipeline_config)
    
    # create pipeline folder in workspace
    pipeline_name = pipeline_config['pipeline_name']
    workspace_path = f"{WORKSPACE}/{pipeline_name}"
    create_workspace_folder(workspace_path)

    steps = get_steps(pipeline_config['steps'])
    
    manager = Manager(steps)
   
        
    

if __name__ == "__main__":
    start()

