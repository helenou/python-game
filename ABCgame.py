#!/usr/bin/env python

import random
import pygame, sys, time
from pygame.locals import *

pygame.init()

fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Abcedaire')

redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)

list = ["ant", "ape", "bear", "butterfly", "beaver", "bat", "bee", "buffalo", "cat", "camel", "caribu", "crocodile", "canary", "deer", "donkey", "duck", "dog", "dolphin", "eagle", "elephant", "ermine", "earthworm", "flamingo", "fish", "frog", "fox", "fly", "gazelle", "goose", "giraffe", "gorilla", "goat", "hamster", "hare", "horse", "heron", "hippopotamus", "iguana", "ibis", "isopod", "jaguar", "jellyfish", "jerboa", "kiwi", "koala", "kangaroo", "ladybug", "lion", "lemur", "leopard", "lobster", "meerkat", "mole", "mosquito", "moose", "mouse", "monkey", "nettlefish", "nautilus", "nutcracker", "orangutan", "octopus", "oyster", "ox", "owl", "otter", "panda", "panther", "parrot", "penguin", "pelican", "pig", "quail", "quetzal", "rabbit", "rat", "raccoon", "reindeer", "rhinoceros", "raven", "shark", "scorpion", "salmon", "seastar", "sheep", "snail", "snake", "squirrel", "spider", "sea lion", "tapir", "tarantula", "turkey", "tiger", "turtle", "Ulysses Butterfly", "Umbrella Bird", "urubu","viper", "vampire bat", "vulture", "whale", "wasp", "wallaby", "wolf", "woodpecker", "wolverine", "xerus", "xantus", "xenarthra", "yak", "zebra", "zebu", "zorilla", "zorro"]

running = True
char="a"


while (running):
    for event in pygame.event.get():
        if (event.type == QUIT):
           running = False
           pygame.quit()
           sys.exit()
        elif event.type == KEYDOWN:
           if event.key == K_a:
              char="a"
           if event.key == K_b:
              char="b"
           if event.key == K_c:
              char="c"
           if event.key == K_d:
              char="d"
           if event.key == K_e:
              char="e"
           if event.key == K_f:
              char="f"
           if event.key == K_g:
              char="g"
           if event.key == K_h:
              char="h"
           if event.key == K_i:
              char="i"
           if event.key == K_j:
              char="j"
           if event.key == K_k:
              char="k"
           if event.key == K_l:
              char="l"
           if event.key == K_m:
              char="m"
           if event.key == K_n:
              char="n"
           if event.key == K_o:
              char="o"
           if event.key == K_p:
              char="p"
           if event.key == K_q:
              char="q"
           if event.key == K_r:
              char="r"
           if event.key == K_s:
              char="s"
           if event.key == K_t:
              char="t"
           if event.key == K_u:
              char="u"
           if event.key == K_v:
              char="v"
           if event.key == K_w:
              char="w"
           if event.key == K_x:
              char="x"
           if event.key == K_y:
              char="y"
           if event.key == K_z:
              char="z"
           if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                
        elif event.type == KEYUP:
            # Retrieve words with first character matching char
            newList = [ word for word in list if word[0] == char ]
            # Select one word randomly
            wordpick= random.choice(newList)
    
        # Render word
            # Set font, size, colour and background color of our word box
            font = pygame.font.SysFont("TimesNewRoman, Arial", 60)
            text = font.render(wordpick, True, redColour, greyColour)
            # Set grey background to display text
            window.fill(greyColour)
            # Display the formatted word 
            # window.blit( text, (window_width/2 - text.get_rect().width/2, window_height/2 - 100  ) )
            window.blit( text, (640/2 - text.get_rect().width/2, 480/2 - 100  ) )    
            
            pygame.time.delay(300)
    
            pygame.display.update()
    
    fpsClock.tick(600)