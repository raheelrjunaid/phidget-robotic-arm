from main import servos
from signal import pause

print("Manipulate individual servos for testing angles and calibration.")
try:
    while True:
        servo_selection = input("Servo Index:")
        servo = servos[int(servo_selection)]
        servo.setEngaged(True)
        print("Entering playground, press any letter to exit.")
        while True:
            position = input(f"Servo {servo_selection} Position: ")
            if not position.isnumeric():
                break
            servo.move(int(position))
        servo.setEngaged(False)
except ValueError:
    print("Invalid Servo Index")
except KeyboardInterrupt:
    pass
finally:
    print("\nExiting Program")
    for servo in servos:
        servo.close()
