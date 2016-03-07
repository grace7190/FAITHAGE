# Taken from http://pygame.org/wiki/Spritesheet?parent=
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

import pygame


class SpriteSheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error, message:
            print 'Unable to load spritesheet image:', filename
            raise SystemExit, message

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colourkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colourkey is not None:
            if colourkey is -1:
                colourkey = image.get_at((0,0))
            image.set_colorkey(colourkey, pygame.RLEACCEL)
        return image

    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colourkey = None):
        "Loads multiple images, supply a list of coordinates"
        return [self.image_at(rect, colourkey) for rect in rects]

    # Load a whole strip of images
    def load_strip(self, rect, image_count, colourkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colourkey)
