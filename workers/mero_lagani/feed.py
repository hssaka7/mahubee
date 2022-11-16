from mahubee import Duty, FileState



class Extract(Duty):
    def start(self):
        print("on extract")
        return 'extract result'

class Save(Duty):
    def start(self):
        print("on save")
        return 'Save result'


class Transform (Duty):
    def start(self):
        print ("on transform")
        return 'Transform result'

class Load (Duty):

    def start(self):
        print("on load")
        return 'Load result'
