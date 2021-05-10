from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
from time import sleep

class Servo(RCServo):
    def __init__(self, channel, reset_angle=0, engage=True, minLim=0, maxLim=180):
        RCServo.__init__(self)
        self.setChannel(channel)
        self.openWaitForAttachment(1000)
        self.reset_angle = reset_angle
        self.minLim = minLim
        self.maxLim = maxLim
        self.move(reset_angle)

    def move(self, pos):
        if pos > self.maxLim:
            pos = self.maxLim
        elif pos < self.minLim:
            pos = self.minLim
        self.setTargetPosition(pos)

class Arm:
    def __init__(self, servos):
        if len(servos) < 6:
            raise Exception("6 servos are required for the Robotic Arm")

        self.base = servos[0]
        self.shoulder = servos[1]
        self.elbow = servos[2]
        self.wrist = servos[3]
        self.wrist_rotate = servos[4]
        self.claw = servos[5]

        self.servos = [
            self.base,
            self.shoulder,
            self.elbow,
            self.wrist,
            self.wrist_rotate,
            self.claw
        ]

    def engage(self):
        for servo in self.servos:
            servo.setEngaged(True)
        sleep(1)

    def finish(self, reset_state=True):
        if reset_state:
            self.reset()
        for servo in self.servos:
            servo.close()

    def reset(self):
        for servo in self.servos:
            servo.move(servo.reset_angle)
        sleep(2)

    def grasp(self):
        self.claw.move(self.claw.maxLim / 2)
        sleep(1)

    def release(self):
        self.claw.move(self.claw.maxLim)
        sleep(1)

    def grab(self):
        self.release()
        self.drop()
        self.grasp()
        self.lift()

    def turnLeft(self):
        self.base.move(0)
        sleep(1)

    def turnRight(self):
        self.base.move(180)
        sleep(1)

    def turnMiddle(self):
        self.base.move(90)
        sleep(1)

    def lift(self):
        self.wrist.move(self.wrist.minLim)
        sleep(1)
        self.elbow.move(self.elbow.minLim)
        self.shoulder.move(self.shoulder.minLim)
        sleep(1)

    def drop(self):
        self.wrist.move(100)
        self.shoulder.move(70)
        sleep(1)
