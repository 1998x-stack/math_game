# text_utils.py

import pygame

# 定义字体
def load_font(size=36):
    return pygame.font.Font(None, size)

# 渲染文字
def render_text(window, text, font, color, pos):
    text_surface = font.render(text, True, color)
    window.blit(text_surface, pos)
