import pygame
from pygame.locals import *

def main():
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    if not pygame.joystick.get_init():
        pygame.joystick.init()
    gamepads = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    player1id = gamepads[0].get_id()
    if pygame.joystick.get_count() > 1:
        player2id = gamepads[1].get_id()
    else:
        player2id = None

    #main loop
    while True:
        #process events
        dispatch_events(pygame.event.get())
        #get input
        #perform game logic
        #output graphics

def dispatch_event(events):
    for event in events:
        #gamepad event
        if event.type == JOYAXISMOTION or event.type == JOYBALLMOTION
        or event.type == JOYBUTTONDOWN or event.type == JOYBUTTONUP or event.type == JOYHATMOTION:
            handle_joystick_event(event)
    
def handle_joystick_event(event):
    if event.joy == player1id:
        if event.type == JOYAXISMOTION:
    if event.joy == player2id:
        if event.type == JOYAXISMOTION:
