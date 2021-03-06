import pygame
import random

class Star():
    def __init__(self, screen, star_x, star_y, i):
        """初始化星星"""
        self.screen = screen
        
        # 加载星星图像，并设置其rect属性
        self.image = pygame.image.load('images/star%s.bmp' % i)
        self.rect = self.image.get_rect()

        # 星星随机位置
        self.rect.x = star_x
        self.rect.y = star_y
        
    def blitme(self):
        """随机绘制星星"""
        self.screen.blit(self.image, self.rect)