# Phidget Robotic Arm
This project adds/abstracts functionality for controlling multiple servos through robotic arm commands. This has been tested and is primarily built for the RC1000 Phidget Motor Controller. Feel free to try it out with other motor controllers, and let me know how it goes!

## Installation
You will have to clone the repository and install the following dependencies to your environment:
```bash
pip install Phidget22
```
You're done!

## Usage

### Calibration
To calibrate the servos, go into [main.py](main.py) and remove all but the first argument.
```python
# The arguments that were placed here before were just my setup :)
servos = [
    Servo(0),
    Servo(1),
    Servo(2),
    Servo(3),
    Servo(4),
    Servo(5),
]
```
The first argument is the channel at which the servo is located. To view all the parameters for the `Servo` class, view [arm.py](arm.py). This was just to reset the servos to their default state. Now you can navigate to [testing.py](testing.py) to find out the required angles:

1. The `reset_angle` is the angle at which the servo navigates to by default when it is engaged.
2. The `minLim` is the minimum angle at which the servo can reach.
3. The `maxLim` is the maximum angle at which the servo can reach.

You find out the angles by running `testing.py` and entering the channel/index of the servo you want to manipulate.

> All of the behind-the-scenes can be found in [arm.py](arm.py) if you are ever confused.

### Path Setting
To set the path that the robot should take, clear the `main` function in [main.py](main.py) and replace it with your own path. Available options:

| Option | Function to Call |
| ----------- | ----------- |
| Engage Motors (required) | engage() |
| Reset Motors | reset() |
| Reset and Close Motors (required) | finish() |
| Grasp object | grasp() |
| Release object | release() |
| Lift claw/object | lift() |
| Drop claw/object | drop() |
| Grasp and Lift object | grab() |
| Spin to left | turnLeft() |
| Spin to center | turnMiddle() |
| Spin to right | turnRight() |

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
- If a new algorithm is added, please add it to the [Read Me](README.md) in [Path Setting](#path-setting).

## License
[GNU](LICENSE)
