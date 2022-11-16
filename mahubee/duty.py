from abc import ABC, abstractmethod
from .workspace import FileState

# TODO implement file state
# TODO duty shoud be able to import the feed class 

class Duty(ABC):
    def __init__(self,*args, **kwargs):
        
        self.name = kwargs['name']
        self.depends = kwargs['depends']
        self.class_name = kwargs['class_name']

        self.config = kwargs

        self.inputs = []

    def set_inputs ( self, inputs = []):
        self.inputs = inputs

    @abstractmethod
    def start(self):
        pass

    
    


class Capture(Duty):
    
    def start(self, url):
        print("Starting duty")
        # this should return the file state

    
