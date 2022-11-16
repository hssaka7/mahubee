import mahubee


class Extract(mahubee.Duty):
    def start(self):
        print("on extract")

class Save(mahubee.Duty):
    def start(self):
        print("on save")


class Transform (mahubee.Duty):
    def start(self):
        print ("on transform")

class Load (mahubee.Duty):

    def start(self):
        print("on load")
