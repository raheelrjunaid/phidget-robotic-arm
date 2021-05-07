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

for num, servo in enumerate(servos):
    print("Initializing servo: " + str(num), end=" ")
    servo.setChannel(num)
    servo.openWaitForAttachment(1000);
    servo.setTargetPosition(reverse_dir(0))
    servo.setEngaged(True)
    print("Done!")
    sleep(1)

def testing():
    while True:
        try:
            pos = int(input("pos: "))
        except ValueError:
            return False
        servo.setTargetPosition(reverse_dir(pos))

def program():
    servo2.setTargetPosition(180)
    sleep(1)
    servo0.setTargetPosition(70)
    sleep(1)
    servo1.setTargetPosition(30)
    sleep(1)
    servo3.setTargetPosition(100)
    sleep(1)

try:
    # program()
    while True:
        servo_index = int(input("servo: "))
        servo = list(servos.keys())[servo_index]
        testing()
    pause()

except (Exception, KeyboardInterrupt) as e:
    print("Error:", e, "Exiting")
    for servo in servos:
        servo.setTargetPosition(reverse_dir(0)) # Reset
    for servo in servos:
        servo.close()
