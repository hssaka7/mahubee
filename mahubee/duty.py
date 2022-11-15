from abc import ABC, abstractmethod
from .workspace import FileState

# TODO implement file state

class Duty(ABC):
    def __init__(self, *args, **kwargs):
        print("here")
    
    
    @abstractmethod
    def start():
        return FileState([])
        

class Capture(Duty):
    
    def start(self, url):
        print("Starting duty")
        # this should return the file state

    
