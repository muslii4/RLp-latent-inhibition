# Import third party packages.
import pygame
from minigrid.manual_control import ManualControl

# Import local packages.
from src.environment import RoomEnvironment

# Initialize pygame to avoid error on program exit.
pygame.init()


def main():
    environment = RoomEnvironment(render_mode="human")

    # Enable manual control for testing.
    manual_control = ManualControl(environment, seed=42)
    manual_control.start()


if __name__ == "__main__":
    main()
