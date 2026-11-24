# Import standard library packages.
from abc import abstractmethod

# Import third party packages.
from minigrid.core.constants import COLOR_NAMES
from minigrid.core.grid import Grid
from minigrid.core.mission import MissionSpace
from minigrid.core.world_object import Door, Key, Goal
from minigrid.minigrid_env import MiniGridEnv


class RoomEnvironment(MiniGridEnv):
    def __init__(
        self,
        size=8,
        agent_start_pos=(1, 1),
        agent_start_dir=0,
        max_steps: int | None = None,
        **kwargs,
    ) -> None:
        # Set the agent's starting position and direction.
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir

        # Create a MissionSpace instance.
        mission_space = MissionSpace(mission_func=self._gen_mission)

        # Initialize the MiniGridEnv.
        super().__init__(
            mission_space=mission_space,
            grid_size=size,
            max_steps=256,
            **kwargs,
        )

    @staticmethod
    def _gen_mission():
        return ""

    @abstractmethod
    def _gen_grid(self, width, height):
        # Create the enviroment's grid.
        self.grid = Grid(width, height)
        self.grid.wall_rect(0, 0, width, height)

        # Place the agent inside the grid.
        if self.agent_start_pos is not None:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            self.place_agent()

        # Create the exit (goal) of the grid.
        self.put_obj(Goal(), width - 2, height - 2)

        # Add doors and keys.
        self.grid.set(5, 6, Door(COLOR_NAMES[0], is_locked=True))
        self.grid.set(3, 6, Key(COLOR_NAMES[0]))
