from signal import pause
from arm import Servo, Arm

arm = Arm()
arm.engage()

def testing():
    while True:
        try:
            pos = int(input("pos: "))
        except ValueError:
            return False
        servo.move(pos)

def program():
    arm.turnLeft()
    arm.grab()
    arm.turnRight()
    arm.drop()
    arm.release()
    arm.lift()
    arm.reset()

try:
    run = input("\nRun program [y/n]? ")
    while run.lower() == "y":
        program()
        run = input("\nRun program [y/n]? ")

    while True:
        servo_index = int(input("servo: "))
        servo = arm.servos[servo_index]
        testing()
    pause()

except (Exception, KeyboardInterrupt) as e:
    print("Error:", e, "Exiting")
    arm.finish()
