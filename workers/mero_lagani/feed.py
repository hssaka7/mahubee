import mahubee
import requests

class Extract(mahubee.Duty):
    def start():
        print("here")


if __name__ == '__main__':
    a = Extract()
    a.start()