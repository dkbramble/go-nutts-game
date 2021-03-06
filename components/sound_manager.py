from league import *
import pygame

playing = True

class SoundManager():
    """
    This class manages all the sound in the game, including background 
    and sound effects. 

    https://ozzed.net/music/friendship-adventure.shtml#tune13
    https://nerdparadise.com/programming/pygame/part3
    """

    def __init__(self):
        pygame.mixer.init()
        self.sound_path = '../assets/sounds/'

    #Start the background music on loop using the given file
    def bgm_start(self, file):
        file_path = self.sound_path + file
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play(-1)

    #Toggle on/off the background music
    def bgm_control(self):
        global playing
        if playing:
            pygame.mixer.music.pause()
            playing = False
        else:
            pygame.mixer.music.unpause()   
            playing = True
        return playing

    #Play a sound once using the given file
    def play_sound(self, file):
        file_path = self.sound_path + file
        sound = pygame.mixer.Sound(file_path)
        sound.play()
    
    def get_playing(self):
        return playing

    def set_playing(self, play):
        global playing
        playing = play
