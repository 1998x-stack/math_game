# input_handler.py

import pygame

# 处理用户输入
def handle_input(events, current_input):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                current_input = current_input[:-1]
            elif event.key == pygame.K_RETURN:
                return current_input, True  # 用户按下回车键，提交输入
            else:
                current_input += event.unicode  # 添加输入字符
    return current_input, False
