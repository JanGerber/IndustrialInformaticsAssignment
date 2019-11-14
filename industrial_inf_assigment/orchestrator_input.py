import time

import explorerhat

from industrial_inf_assigment.orchestrator_rpi import Orchestrator
from industrial_inf_assigment.phone import Phone
from industrial_inf_assigment.phone_color import PhoneColor
from industrial_inf_assigment.phone_shape import PhoneShape


class OrchestratorInput:

    def __init__(self, orchestrator: Orchestrator):
        self.phone = Phone(PhoneShape.FRAME_1, PhoneColor.RED, PhoneShape.KEYBOARD_1, PhoneColor.RED,
                           PhoneShape.SCREEN_1, PhoneColor.RED)
        self.state = 0
        self.selected = False
        self.orchestrator = orchestrator
        self.okButton = 1
        print("New Orchestrator Input Service initiated")

    def startListening(self):
        explorerhat.touch.pressed(self.changeState)
        print("Start Listening to Button Inputs")
        while True:
            if self.state == 0:
                explorerhat.light[0].off()
                time.sleep(0.1)
            elif self.state == 7:
                explorerhat.light[0].on()
                time.sleep(0.2)
                explorerhat.light[0].off()
                time.sleep(0.2)
            elif self.selected:
                explorerhat.light[0].on()
                time.sleep(0.1)
            else:
                explorerhat.light[0].on()
                time.sleep(0.6)
                explorerhat.light[0].off()
                time.sleep(0.6)


    def changeState(self, channel, event):
        print("Button pressed: " + channel)
        if self.state == 0:
            print("State 0")
            if channel == self.okButton:
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
            if channel == self.okButton:
                self.orchestrator.addNewOrder(self.phone)
                self.state = 0

    def state1(self, channel):
        print("Select Frame Shape")
        if channel == self.okButton and self.selected:
            self.state = 2
            self.selected = False
        elif channel == 2:
            self.phone.frameShape = PhoneShape.FRAME_1
            self.selected = True
        elif channel == 3:
            self.phone.frameShape = PhoneShape.FRAME_2
            self.selected = True
        elif channel == 4:
            self.phone.frameShape = PhoneShape.FRAME_3
            self.selected = True

    def state2(self, channel):
        print("Select Frame Color")
        if channel == self.okButton and self.selected:
            self.state = 3
            self.selected = False
        elif channel == 2:
            self.phone.frameColor = PhoneColor.RED
            self.selected = True
        elif channel == 3:
            self.phone.frameColor = PhoneColor.GREEN
            self.selected = True
        elif channel == 4:
            self.phone.frameColor = PhoneColor.BLUE
            self.selected = True

    def state3(self, channel):
        print("Select Screen Shape")
        if channel == self.okButton and self.selected:
            self.state = 4
            self.selected = False
        elif channel == 2:
            self.phone.screenShape = PhoneShape.SCREEN_1
            self.selected = True
        elif channel == 3:
            self.phone.screenShape = PhoneShape.SCREEN_2
            self.selected = True
        elif channel == 4:
            self.phone.screenShape = PhoneShape.SCREEN_3
            self.selected = True

    def state4(self, channel):
        print("Select Screen Color")
        if channel == self.okButton and self.selected:
            self.state = 5
            self.selected = False
        elif channel == 2:
            self.phone.screenColor = PhoneColor.RED
            self.selected = True
        elif channel == 3:
            self.phone.screenColor = PhoneColor.GREEN
            self.selected = True
        elif channel == 4:
            self.phone.screenColor = PhoneColor.BLUE
            self.selected = True

    def state5(self, channel):
        print("Select Keyboard Shape")
        if channel == self.okButton and self.selected:
            self.state = 6
            self.selected = False
        elif channel == 2:
            self.phone.keyboardShape = PhoneShape.KEYBOARD_1
            self.selected = True
        elif channel == 3:
            self.phone.keyboardShape = PhoneShape.KEYBOARD_2
            self.selected = True
        elif channel == 4:
            self.phone.keyboardShape = PhoneShape.KEYBOARD_3
            self.selected = True

    def state6(self, channel):
        print("Select Keyboard Color")
        if channel == self.okButton and self.selected:
            self.state = 7
            self.selected = False
        elif channel == 2:
            self.phone.keyboardColor = PhoneColor.RED
            self.selected = True
        elif channel == 3:
            self.phone.keyboardColor = PhoneColor.GREEN
            self.selected = True
        elif channel == 4:
            self.phone.keyboardColor = PhoneColor.BLUE
            self.selected = True

    def resetPhone(self):
        self.state = 0