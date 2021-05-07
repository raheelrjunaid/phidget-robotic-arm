from Phidget22.Phidget import *
from Phidget22.Devices.RCServo import *
from signal import pause
from time import sleep

servo0 = RCServo()
servo1 = RCServo()
servo2 = RCServo()
servo3 = RCServo()
servo4 = RCServo()
servo5 = RCServo()

servos = {
    servo0: "normal",
    servo1: "normal",
    servo2: "reversed",
    servo3: "normal",
    servo4: "normal",
    servo5: "normal"
}

def reset():
    for servo in servos:
        move(0, servo=servo)
    sleep(2)

def move(pos, servo_num=0, servo=None):
    if servo != None:
        servo.setTargetPosition(pos if servos[servo] != "reversed" else 180 - pos)
    else:
        servo = list(servos.keys())[servo_num]
        servo.setTargetPosition(pos if servos[servo] != "reversed" else 180 - pos)

def grasp():
    move(25, 5)
    sleep(1)
    lift()

def release():
    drop()
    move(65, 5)
    sleep(1)

def grab():
    move(120, 3)
    move(65, 5)
    move(30, 4)
    drop()
    sleep(2)
    grasp()

def turnLeft():
    move(0, 0)
    sleep(1)

def turnRight():
    move(180, 0)
    sleep(1)

def turnMiddle():
    move(90, 0)
    sleep(1)

def lift():
    move(80, 3)
    move(0, 1)
    sleep(1)

def drop():
    move(120, 3)
    move(20, 1)
    sleep(1)

def testing():
    while True:
        try:
            pos = int(input("pos: "))
        except ValueError:
            return False
        move(pos, servo=servo)
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
        move(0, servo=servo)
        servo.setEngaged(True)
        print("Done!")
    sleep(1)

    run = input("Run program [y/n]? ")
    while run.lower() == "y":
        program()
        run = input("Run program [y/n]? ")
    while True:
        servo_index = int(input("servo: "))
        servo = list(servos.keys())[servo_index]
        testing()

    pause()

except (Exception, KeyboardInterrupt) as e:
    print("Error:", e, "Exiting")
    reset()
    for servo in servos:
        servo.close()
