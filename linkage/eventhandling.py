from pygame.locals import *

def dispatch_events(events):
    for event in events:
        #gamepad event
        if event.type == JOYAXISMOTION or event.type == JOYBALLMOTION or event.type == JOYBUTTONDOWN or event.type == JOYBUTTONUP or event.type == JOYHATMOTION:
            handle_joystick_event(event)
        if event.type == QUIT:
            exit()
    
def handle_joystick_event(event):
    game = Game() #grab the game object
    if event.joy == game.player1.joyid:
        if event.type == JOYAXISMOTION:
            print "blah"
    if event.joy == game.player2.joyid:
        if event.type == JOYAXISMOTION:
            print "blah"