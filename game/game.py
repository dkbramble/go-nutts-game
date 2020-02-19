#!/usr/bin/env python3

import pygame
import sys
sys.path.append('..')
import league
from components import *
from player import Player
<<<<<<< HEAD:examples/game.py
from overlay import Overlay
from enemies.spider import Spider
from enemies.bee import Bee
from enemies.ant import Ant
=======
from components.overlay import Overlay
>>>>>>> master:game/game.py


"""This file is garbage. It was a hastily coded mockup
to demonstrate how to use the engine.  We will be creating
a Game class that organizes this code better (and is
reusable).
"""

# Function to call when colliding with zombie

def main():
    e = league.Engine("Go Nutts!")
    e.init_pygame()

    ##sprites = league.Spritesheet('../assets/base_chip_pipo.png', league.Settings.tile_size, 8)
    backgroundMaterial = league.Spritesheet('../assets/woodlandMaterials.png', league.Settings.tile_size, 5)
    t = league.Tilemap('../assets/woodland.lvl', backgroundMaterial, layer = 1)
    b = league.Tilemap('../assets/background.lvl', backgroundMaterial, layer = 0)
    world_size = (t.wide*league.Settings.tile_size, t.high *league.Settings.tile_size)
    e.drawables.add(b.passable.sprites()) 
    e.drawables.add(t.passable.sprites())
    m = SoundManager()
    m.bgm_start('Song_For_Someone.wav')
    p = Player(2, 400, 300)
    o = Overlay(p)
    bu = MusicButton()
    p.blocks.add(t.impassable)
    p.world_size = world_size
    p.rect = p.image.get_rect()

    q = Player(10, 100, 100)
    q.image = p.image

    s = Spider(10, 300, 300, 120)
    s.blocks.add(t.impassable)
    s.world_size = world_size
    s.rect = s.image.get_rect()

    b = Bee(10, 400, 400, 120)
    b.blocks.add(t.impassable)
    b.world_size = world_size
    b.rect = b.image.get_rect()

    a = Ant(10, 500, 300, 120)
    a.blocks.add(t.impassable)
    a.world_size = world_size
    a.rect = a.image.get_rect()

    e.objects.append(p)
    e.objects.append(q)
    e.objects.append(s)
    e.objects.append(b)
    e.objects.append(a)

    e.drawables.add(p)
    e.drawables.add(q)
    e.drawables.add(s)
    e.drawables.add(b)
    e.drawables.add(a)
    e.drawables.add(o)
    e.drawables.add(bu)

    c = league.LessDumbCamera(800, 600, p, e.drawables, world_size)
    #c = league.DumbCamera(800, 600, p, e.drawables, world_size)
    
    e.objects.append(c)
    e.objects.append(o)
    e.objects.append(bu)

    e.collisions[p] = (q, p.ouch) 
    pygame.time.set_timer(pygame.USEREVENT + 1, 1000 // league.Settings.gameTimeFactor)
<<<<<<< HEAD:examples/game.py
    pygame.time.set_timer(pygame.USEREVENT + 2, 150 // league.Settings.gameTimeFactor)
    pygame.time.set_timer(pygame.USEREVENT + 3, 100 // league.Settings.gameTimeFactor)
    pygame.time.set_timer(pygame.USEREVENT + 4, 500 // league.Settings.gameTimeFactor)

    e.key_events[pygame.K_a] = p.move_left
    e.key_events[pygame.K_d] = p.move_right
    e.key_events[pygame.K_w] = p.move_up
    e.key_events[pygame.K_s] = p.move_down
=======
    e.add_key(pygame.K_a, p.move_left)
    e.add_key(pygame.K_d, p.move_right)
    e.add_key(pygame.K_w, p.move_up)
    e.add_key(pygame.K_s, p.move_down)
    e.add_key(pygame.K_b, p.climb_on)
    e.add_key(pygame.K_SPACE, p.climb_off)
>>>>>>> master:game/game.py
    e.events[pygame.USEREVENT + 1] = q.move_right
    e.events[pygame.USEREVENT + 2] = s.move
    e.events[pygame.USEREVENT + 3] = b.move
    e.events[pygame.USEREVENT + 4] = a.move
    e.events[pygame.QUIT] = e.stop
    e.run()

if __name__=='__main__':
    main()