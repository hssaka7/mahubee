import yaml
import os

def parse_config(config_path):
    with open(config_path) as input_stream:
        try:
            config = yaml.safe_load(input_stream)
        except yaml.YAMLError as exc:
            raise exc

    return config or None


def create_workspace_folder(workspace_path):

    if os.path.exists(workspace_path):
        print("the workspace directory already exist. Deleting and creating agian")
        os.rmdir(workspace_path)
    
    os.mkdir(workspace_path)        
    return True
        
  
