from Phidget22.Phidget import *
from signal import pause
from Phidget22.Devices.RCServo import *
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

def rev_dir(pos, servo_num=0, servo=None): # Reverse Direction
    if servo != None:
        return pos if servos[servo] != "reversed" else 180 - pos
    else:
        return pos if list(servos.values())[servo_num][1] != "reversed" else 180 - pos

def reset():
    for servo in servos:
        servo.setTargetPosition(rev_dir(0, servo=servo))
    sleep(2)

def testing():
    while True:
        try:
            pos = int(input("pos: "))
        except ValueError:
            return False
        servo.setTargetPosition(rev_dir(pos, servo=servo))

def program():

    def grasp():
        servo5.setTargetPosition(0)
        sleep(1)

    def release():
        servo5.setTargetPosition(65)
        sleep(1)

    def grab():
        servo3.setTargetPosition(rev_dir(120, 3))
        servo1.setTargetPosition(rev_dir(30, 1))
        servo5.setTargetPosition(rev_dir(65, 5))
        servo4.setTargetPosition(rev_dir(30, 4))
        sleep(1)
        grasp()

    def turn180():
        base_pos = abs(servo0.getPosition() - 180)
        servo0.setTargetPosition(rev_dir(base_pos, 0))
        sleep(1)

    grab()
    turn180()
    release()
    reset()

try:

    for num, servo in enumerate(servos):
        print("Initializing servo: " + str(num), end=" ")
        servo.setChannel(num)
        servo.openWaitForAttachment(1000);
        servo.setTargetPosition(rev_dir(0, servo=servo))
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
