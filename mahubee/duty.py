from abc import ABC, abstractmethod


# TODO implement file state
# TODO duty shoud be able to import the feed class 

class Duty(ABC):
    def __init__(self, *args, **kwargs):
        
        self.name = kwargs['name']
        self.depends = kwargs['depends']
        self.class_name = kwargs['class_name']
        self.workspace_path = kwargs['_workspace_path']

        self.config = kwargs

        self.inputs = []

    def set_inputs ( self, inputs = []):
        self.inputs = inputs

    @abstractmethod
    def start(self):
        pass

    
