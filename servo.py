from Phidget22.Phidget import *
from signal import pause
from Phidget22.Devices.RCServo import *
from time import sleep

reverse_dir = lambda pos: 180-pos if servos[servo] == "reversed" else pos

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
    servo4: "reversed",
    servo5: "normal"
}

def reset():
    for servo in servos:
        servo.setTargetPosition(reverse_dir(0)) # Reset
    sleep(2)

def testing():
    while True:
        try:
            pos = int(input("pos: "))
        except ValueError:
            return False
        servo.setTargetPosition(reverse_dir(pos))

def program():
    servo3.setTargetPosition(reverse_dir(120))
    servo1.setTargetPosition(reverse_dir(30))
    servo5.setTargetPosition(reverse_dir(65))
    sleep(1)
    servo5.setTargetPosition(reverse_dir(0))

try:
    for num, servo in enumerate(servos):
        print("Initializing servo: " + str(num), end=" ")
        servo.setChannel(num)
        servo.openWaitForAttachment(1000);
        servo.setTargetPosition(reverse_dir(0))
        servo.setEngaged(True)
        print("Done!")
        sleep(1)

    program()
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
