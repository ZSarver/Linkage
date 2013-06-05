import pygame

class StaticSprite (pygame.sprite.Sprite):
    """The simplest of sprite classes. Note that we don't need a draw
    method. A sprite added to any instance of any subclass of
    pygame.sprite.Group will draw self.image to self.rect whenever
    that groups draw() method is called.

    """
    def __init__ (self, image, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = image #a pygame.Surface object
        self.rect = rect #a pygame.Rect object
   
