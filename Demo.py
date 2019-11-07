from Project.StateMachine import StateMachine
from lib.PepperConfiguration import PepperConfiguration
from lib.Robot import Robot

# config = PepperConfiguration("local", ip="127.0.0.1", port=46793)
config = PepperConfiguration("Amber")
robot = Robot(config)


if __name__ == "__main__":
    machine = StateMachine(robot)
    machine.run()
