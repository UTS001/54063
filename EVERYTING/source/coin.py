import pygame
from .. import tools, setup
from .. import constants as C

class FlashingCoin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.frames = []
        self.frame_index = 0
        frame_rects = [(108, 199, 25, 41), (139, 199, 25, 41), (172, 200, 25,41), (139, 199, 25, 41)]
        self.load_frames(frame_rects)
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = 723
        self.rect.y = 30
        self.timer = 0

    def load_frames(self, frame_rects):
        sheet = setup. GRAPHICS['item_objectsutslogo']
        for frame_rect in frame_rects:
            self.frames.append(tools.get_image(sheet, *frame_rect, (0, 0, 0), C.BG_MULTI))

    def update(self):
        self.current_time = pygame.time.get_ticks()
        frame_durations = [375, 125, 125, 125]

        if self.timer ==0:
            self.timer = self.current_time
        elif self.current_time - self.timer > frame_durations[self.frame_index]:
            self.frame_index += 1
            self.frame_index %= 4
            self.timer = self.current_time

            self.image = self.frames[self.frame_index]
