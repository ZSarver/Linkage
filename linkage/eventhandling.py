from pygame.locals import *
from gameelements import *

def dispatch_events(events):
    for event in events:
        #gamepad event
        if event.type == JOYAXISMOTION or event.type == JOYBALLMOTION or event.type == JOYBUTTONDOWN or event.type == JOYBUTTONUP or event.type == JOYHATMOTION:
            handle_joystick_event(event)
        if event.type == QUIT:
            exit()
        #keyboard events
        if event.type == KEYDOWN:
            handle_keyboard_event(event)
    
def handle_joystick_event(event):
    game = Game() #grab the game object
    if event.joy == game.player1.joyid:
        if event.type == JOYAXISMOTION:
            print "blah"
    if event.joy == game.player2.joyid:
        if event.type == JOYAXISMOTION:
            print "blah"

def handle_keyboard_event(event):
    game = Game()
    game.cursor.lock()
    if event.key == K_UP:
        game.cursor.move((-1,0))
    elif event.key == K_DOWN:
        game.cursor.move((1,0))
    elif event.key == K_LEFT:
        game.cursor.move((0,-1))
    elif event.key == K_RIGHT:
        game.cursor.move((0,1))
