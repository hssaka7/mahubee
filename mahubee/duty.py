from abc import ABC, abstractmethod

class Duty(ABC):
    def __init__(self, *args, **kwargs):
        print("here")
    
    
    @abstractmethod
    def start():
        pass

class Capture(Duty):
    def start(self):
        print("Starting duty")

if __name__ == '__main__':
    d = Capture()
    d.start()
    
