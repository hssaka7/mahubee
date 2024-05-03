from utils import get_argsparser,parse_config, create_workspace_folder



    


# env variables:

WORKSPACE = '/Users/aakashbasnet/development/python/workspace/ml_pipelines'

# manager run 
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
    
    # TODO create dependency graph
    for step in pipeline_config['steps']:
        print(step['name'])
        print(step['depends'])
        print(step['class_name'])
        print("======================")
    
   
    
    
    

if __name__ == "__main__":
    start()

class Manager():
    def __init__(self):
        id = ""
        # create id folder for the pipleline
        
        pass