from abc import ABC, abstractmethod
from typing import Tuple, List

from mars_rover import MarsRover


class Grid(ABC):
    @abstractmethod
    def place_new_rover(self) -> None:
        """Places a new rover on the field"""

    @abstractmethod
    def get_rovers(self) -> List[MarsRover]:
        """Get all the rovers on the field"""


def create_empty_grid(dimensions: Tuple[int, int]) -> Grid:
    """Creates an empty grid, on which rovers can be placed."""
    raise NotImplementedError
