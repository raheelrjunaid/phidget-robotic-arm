from signal import pause
from arm import Servo, Arm

servos = [
    Servo(0),
    Servo(1, 55, minLim=45, maxLim=135),
    Servo(2, maxLim=90),
    Servo(3),
    Servo(4, 30, minLim=30),
    Servo(5, maxLim=50),
]

arm = Arm(servos)

def main():
    arm.turnLeft()
    arm.grab()
    arm.turnRight()
    arm.drop()
    arm.release()
    arm.lift()
    arm.reset()

if __name__ == "__main__":
    try:
        arm.engage()
        main()
    except (Exception, KeyboardInterrupt) as e:
        print("\nError:", e, "Exiting")
        arm.finish()
