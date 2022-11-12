import argparse
import sys
import os

from .utils import parse_config

from .manager import Manager



def get_argsparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="mode for mahubee to run")
    parser.add_argument("worker_name", help="name of the bee tha needs to run")
    parser.add_argument("--config", help="configuration file having duties", default= 'config')
    parser.add_argument("--debug", help = "turn on debugging", action="store_true")

    return parser



def main():
    
    print("In main function")
    args = vars(get_argsparser().parse_args())
    
    # get hive config
    if 'hive_config' not in os.environ:
        raise Exception("No hive configuration passeed")
    hive_config= parse_config(os.environ ['hive_config']) # TODO add or 'hive_config.yaml' as default



    # get worker config
    

    worker_name = args['worker_name']
    worker_config =   f"{args['config']}.yaml"

    hive_manager = Manager(hive_config, worker_name, worker_config)
    

if __name__ == '__main__':
    main()