import uuid

from industrial_inf_assigment.conveyor import Conveyor
from industrial_inf_assigment.robot import Robot


class Workstation:

    def __init__(self, baseIp, nextWS):
        self.workstationID = uuid.uuid4()
        self.robot = Robot(baseIp + ".1")
        self.conveyor = Conveyor(baseIp + ".2")
        self.pallets = []
        self.nextWS = nextWS
        print("New workstation initiated (" + str(self.workstationID) + ")")

    def addPallet(self, pallet):
        if len(self.pallets) >= 5:
            print("The workstation reached the maximum amount of pallets!")
            return False
        else:
            self.pallets.append(pallet)
            return True

    def removePallet(self):
        if len(self.pallets) > 0:
            return self.pallets.pop(0)
        else:
            print("The workstation don't contains any pallet!")
            return