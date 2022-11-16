
import argparse
import sys
import os

from .utils import parse_config

from .manager import Manager



def get_argsparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="mode for mahubee to run")

    parser.add_argument("worker_name", help="name of the bee tha needs to run")

    parser.add_argument("--debug", help = "turn on debugging", action="store_true")

    return parser



def run():
    
    print("In main function")
    # get hive config
    if 'mahubee_config' not in os.environ:
        raise Exception("No hive configuration passeed")

    args = vars(get_argsparser().parse_args())

    # TODO set up log directory here
    

    mahubee_config= parse_config(os.environ ['mahubee_config']) # TODO add or 'hive_config.yaml' as default
 



    # get worker config
    worker_name = args['worker_name']
    
    
    # TODO vlaidate both env before passing it to manager
    
    hive_manager = Manager(mahubee_config, worker_name)
    hive_manager.run()
    print("done")

if __name__ == '__main__':
    run()