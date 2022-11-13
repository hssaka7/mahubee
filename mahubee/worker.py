import os
import uuid

class Worker:

    def __init__(self,worker_name, worker_path):
        
        self.worker_id = uuid.uuid4()
        self.worker_path = worker_path
        self.worker_name = worker_name
        print("here")

    def set_up_workspace(self):
        # TODO set up the folders needed for the worker
        pass

    def create_duties_dependency_graph(self):
        # TODO creates the duties dependency graph, but to start with, do all in exact order.
        
        pass


    def run(self):
        # TODO run duties

        pass
