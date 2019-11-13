import requests

from industrial_inf_assigment.zone import Zone


class Subscriber:
    def __init__(self, ownAdress):
        self.ownAdress = ownAdress
        self.baseService = "/rest/events"
        self.port = ":8080"

    def subscribeToZoneChange(self, hostIP, zone: Zone):
        url = hostIP + self.port + self.baseService + "/Z" + str(zone.value) + "_Changed/notifs"
        r = requests.post(url, json={"destUrl": self.ownIP})

    def subscribeToPenChangeStart(self, hostIP):
        url = hostIP + self.port + self.baseService + "/PenChangeStarted/notifs"
        r = requests.post(url, json={"destUrl": self.ownIP})

    def subscribeToPenChangeEnd(self, hostIP):
        url = hostIP + self.port + self.baseService + "/PenChangeEnd/notifs"
        r = requests.post(url, json={"destUrl": self.ownIP})

    def subscribeToDrawingStart(self, hostIP):
        url = hostIP + self.port + self.baseService + "/DrawStartExecution/notifs"
        r = requests.post(url, json={"destUrl": self.ownIP})

    def subscribeToDrawingEnd(self, hostIP):
        url = hostIP + self.port + self.baseService + "/DrawEndExecution/notifs"
        r = requests.post(url, json={"destUrl": self.ownIP})