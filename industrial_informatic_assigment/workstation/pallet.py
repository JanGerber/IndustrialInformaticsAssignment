import logging
import uuid

from industrial_informatic_assigment.enum.pallet_status import PalletStatus
from industrial_informatic_assigment.workstation.workstation import Workstation
from industrial_informatic_assigment.workstation.phone import Phone
from industrial_informatic_assigment.enum.zone import Zone


class Pallet:

    def __init__(self, phone: Phone, locationWS: Workstation, locationZone: Zone):
        self.palletID = uuid.uuid4()
        self.phone = phone
        self.locationWS = locationWS
        self.locationZone = locationZone
        self.frameDone = False
        self.screenDone = False
        self.keyboardDone = False
        self.status = PalletStatus.WAITING
        logging.debug("Initialization: new pallet  (" + str(self.palletID) + ")")

    def printPalletInfo(self):
        logging.info(
            "Pallet: \tpalletID:" + str(self.palletID) + " Zone: " + str(self.locationZone) + " Status: " + str(
                self.status.name))
