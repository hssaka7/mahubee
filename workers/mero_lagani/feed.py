import mahubee


class Extract(mahubee.Duty):
    def run():
        print("on extract")


class Transform (mahubee.Duty):
    def run():
        print ("on transform")

class Load (mahubee.Duty):

    def run():
        print("on load")

if __name__ == '__main__':
    a = Extract()
    a.run()