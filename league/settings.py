import pygame

class Settings:
    """Settings exists to store default values used by the engine.
    These values will be class (static) variables, and are not final
    (Python doesn't support finals) so they are still changeable at runtime
    (though you should do so with great care!).

    Attributes:
    fps - Determines how many frames per second the engine attempts to render.
    key_repeat - How quickly (in milliseconds) to wait before allowing a key to repeat.
    width - The width of the screen in pixels.
    height - The height of the screen in pixels.
    tile_size - The default tile_size for sprites
    gameTimeFactor - Controls how real time relates to game time.
    fill_color - The base window color.
    overlay_color - Color to use for overlay text.
    """
    version = 0.9
    fps = 30
    key_repeat = 50
    width = 766
    height = 390
    tile_size = 128
    gameTimeFactor = 1
    fill_color = (255, 255, 255)
    statistics_color = (0, 0, 0)
    statistics_key = pygame.K_BACKQUOTE
    overlay_color = (0, 0, 0)
    overlay_location = (50, 580)

from enum import IntEnum
class State(IntEnum):
    """State enumerates character states for readability.  Common states
    are predefined, add your own as needed."""
    IDLE = 0
    RUN = 1
    JUMP = 2
    CLIMB = 3
    FALL = 4
    
from enum import IntEnum
class Direction(IntEnum):
    """Direction enumerates character directions for readability.  Cardinal
    directions are predefined, add your own as needed."""
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3
