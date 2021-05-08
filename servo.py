from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
from signal import pause
from time import sleep

class Servo(RCServo):

    def __init__(self, reverse=False):
        RCServo.__init__(self)
        self.reverse = reverse

    def move(self, pos):
        self.setTargetPosition(pos if self.reverse == False else 180 - pos)

servo0 = Servo()
servo1 = Servo()
servo2 = Servo(True)
servo3 = Servo()
servo4 = Servo()
servo5 = Servo()

servos = [servo0, servo1, servo2, servo3, servo4, servo5]

def reset():
    for servo in servos:
        servo.move(0)
        # move(0, servo=servo)
    sleep(2)

def grasp():
    servo5.move(25)
    sleep(1)
    lift()

def release():
    drop()
    servo5.move(65)
    sleep(1)

def grab():
    servo3.move(120)
    servo5.move(65)
    servo4.move(30)
    drop()
    sleep(2)
    grasp()

def turnLeft():
    servo0.move(0)
    sleep(1)

def turnRight():
    servo0.move(180)
    sleep(1)

def turnMiddle():
    servo0.move(90)
    sleep(1)

def lift():
    servo3.move(80)
    servo1.move(0)
    sleep(1)

def drop():
    servo3.move(120)
    servo1.move(20)
    sleep(1)

def testing():
    while True:
        try:
            pos = int(input("pos: "))
        except ValueError:
            return False
        servo.move(pos)

def program():
    grab()
    turnRight()
    release()
    reset()

try:
    for num, servo in enumerate(servos):
        print("Initializing servo: " + str(num), end=" ")
        servo.setChannel(num)
        servo.openWaitForAttachment(1000);
        servo.move(0)
        servo.setEngaged(True)
        print("Done!")
    sleep(1)

    run = input("Run program [y/n]? ")
    while run.lower() == "y":
        program()
        run = input("Run program [y/n]? ")
    while True:
        servo_index = int(input("servo: "))
        servo = servos[servo_index]
        testing()

    pause()

except (Exception, KeyboardInterrupt) as e:
    print("Error:", e, "Exiting")
    reset()
    for servo in servos:
        servo.close()
