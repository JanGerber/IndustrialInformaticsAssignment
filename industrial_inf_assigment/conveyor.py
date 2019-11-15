import json
import logging
import uuid

import requests

from industrial_inf_assigment.zone import Zone


class Conveyor:

    def __init__(self, hostIP):
        self.conveyorID = uuid.uuid4()
        self.hostIP = hostIP
        self.baseService = "/rest/services"
        logging.debug("Initialization: new conveyor  (" + str(self.conveyorID) + ")")

    def movePallet(self, zoneStart: Zone, zoneEnd: Zone):
        url = self.hostIP + self.baseService + "/TransZone" + str(zoneStart.value) + str(zoneEnd.value)
        r = requests.post(url, json={"destUrl": ""})
        if r.status_code == 202:
            logging.debug(
                "Conveyor: move pallet successful (Z" + str(zoneStart.value) + " to " + str(zoneEnd.value) + ")")
        else:
            logging.error(
                "Conveyor: move pallet error (Z" + str(zoneStart.value) + " to " + str(
                    zoneEnd.value) + ") Status Code: " + str(
                    r.status_code))

    def getZoneStatus(self, zone: Zone):
        url = self.hostIP + self.baseService + "/Zone" + str(zone.value)
        r = requests.post(url, json={"destUrl": ""})

        reqMsg = json.loads(r.text)
        palletID = reqMsg["PalletID"]

        return palletID
