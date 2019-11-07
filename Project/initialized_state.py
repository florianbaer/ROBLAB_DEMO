from Project.state import state
from Project.waiting_for_face import waiting_for_face


class initialized_state(state):
    def __init__(self, robot):
        self.robot = robot
        self.session = self.robot.session

    def run(self):
        """
        Handle events that are delegated to the current state.
        """
        self.robot.ALTextToSpeech.say("Initialized")

    def next_state(self):
        """
        Sets the next state (or None) for the state machine.
        """
        return waiting_for_face(self.robot)