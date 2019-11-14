import explorerhat

from industrial_inf_assigment.orchestrator_rpi import Orchestrator
from industrial_inf_assigment.phone import Phone
from industrial_inf_assigment.phone_color import PhoneColor
from industrial_inf_assigment.phone_shape import PhoneShape


class ButtonInput:

    def __init__(self, orchestrator: Orchestrator):
        self.phone = Phone(PhoneShape.FRAME_1, PhoneColor.RED, PhoneShape.KEYBOARD_1, PhoneColor.RED,
                           PhoneShape.SCREEN_1, PhoneColor.RED)
        self.state = 0
        self.selected = False
        self.orchestrator = orchestrator
        print("New Button Input Service initiated")

    def changeState(self, channel, event):
        print("Button pressed")
        print(channel)
        print(event)
        if self.state == 0:
            print("State 0")
            if channel == 4:
                self.state = 1
        elif self.state == 1:
            self.state1(channel)
        elif self.state == 2:
            self.state2(channel)
        elif self.state == 3:
            self.state3(channel)
        elif self.state == 4:
            self.state4(channel)
        elif self.state == 5:
            self.state5(channel)
        elif self.state == 6:
            self.state6(channel)
        elif self.state == 7:
            if channel == 4:
                self.orchestrator.addNewOrder(self.phone)
                self.resetLight()
                self.state = 0

    def state1(self, channel):
        print("State 1")
        if channel == 4 and self.selected:
            self.state = 2
            self.resetLight()
            self.selected = False
        elif channel == 1:
            self.phone.frameShape = PhoneShape.FRAME_1
            self.changeLight(1)
            self.selected = True
        elif channel == 2:
            self.phone.frameShape = PhoneShape.FRAME_2
            self.changeLight(2)
            self.selected = True
        elif channel == 3:
            self.phone.frameShape = PhoneShape.FRAME_3
            self.changeLight(3)
            self.selected = True

    def state2(self, channel):
        print("State 2")
        if channel == 4 and self.selected:
            self.state = 3
            self.resetLight()
            self.selected = False
        elif channel == 1:
            self.phone.frameColor = PhoneColor.RED
            self.changeLight(1)
            self.selected = True
        elif channel == 2:
            self.phone.frameColor = PhoneColor.GREEN
            self.changeLight(2)
            self.selected = True
        elif channel == 3:
            self.phone.frameColor = PhoneColor.BLUE
            self.changeLight(3)
            self.selected = True

    def state3(self, channel):
        print("State 3")
        if channel == 4 and self.selected:
            self.state = 4
            self.resetLight()
            self.selected = False
        elif channel == 1:
            self.phone.screenShape = PhoneShape.SCREEN_1
            self.changeLight(1)
            self.selected = True
        elif channel == 2:
            self.phone.screenShape = PhoneShape.SCREEN_2
            self.changeLight(2)
            self.selected = True
        elif channel == 3:
            self.phone.screenShape = PhoneShape.SCREEN_3
            self.changeLight(3)
            self.selected = True

    def state4(self, channel):
        print("State 4")
        if channel == 4 and self.selected:
            self.state = 5
            self.resetLight()
            self.selected = False
        elif channel == 1:
            self.phone.screenColor = PhoneColor.RED
            self.changeLight(1)
            self.selected = True
        elif channel == 2:
            self.phone.screenColor = PhoneColor.GREEN
            self.changeLight(2)
            self.selected = True
        elif channel == 3:
            self.phone.screenColor = PhoneColor.BLUE
            self.changeLight(3)
            self.selected = True

    def state5(self, channel):
        print("State 5")
        if channel == 4 and self.selected:
            self.state = 6
            self.resetLight()
            self.selected = False
        elif channel == 1:
            self.phone.keyboardShape = PhoneShape.KEYBOARD_1
            self.changeLight(1)
            self.selected = True
        elif channel == 2:
            self.phone.keyboardShape = PhoneShape.KEYBOARD_2
            self.changeLight(2)
            self.selected = True
        elif channel == 3:
            self.phone.keyboardShape = PhoneShape.KEYBOARD_3
            self.changeLight(3)
            self.selected = True

    def state6(self, channel):
        print("State 6")
        if channel == 4 and self.selected:
            self.state = 7
            self.allLights()
            self.selected = False
        elif channel == 1:
            self.phone.keyboardColor = PhoneColor.RED
            self.changeLight(1)
            self.selected = True
        elif channel == 2:
            self.phone.keyboardColor = PhoneColor.GREEN
            self.changeLight(2)
            self.selected = True
        elif channel == 3:
            self.phone.keyboardColor = PhoneColor.BLUE
            self.changeLight(3)
            self.selected = True

    def resetPhone(self):
        self.state = 0

    def changeLight(self, param: int):
        self.resetLight()
        explorerhat.light[param - 1].on()

    def resetLight(self):
        explorerhat.light[0].off()
        explorerhat.light[1].off()
        explorerhat.light[2].off()

    def allLights(self):
        explorerhat.light[0].on()
        explorerhat.light[1].on()
        explorerhat.light[2].on()