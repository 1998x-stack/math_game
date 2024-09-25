# game_main.py (更新版)

import pygame  # 导入pygame库
import sys  # 导入sys库
from text_utils import load_font, render_text  # 从text_utils导入字体加载和文本渲染函数
from input_handler import handle_input  # 从input_handler导入输入处理函数
from game_logic import display_question, check_answer, adjust_difficulty  # 从game_logic导入游戏逻辑相关函数
from question_generator import generate_question  # 从question_generator导入问题生成函数

pygame.init()  # 初始化pygame

WINDOW_WIDTH = 800  # 设置窗口宽度
WINDOW_HEIGHT = 600  # 设置窗口高度
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # 创建游戏窗口
pygame.display.set_caption("加减运算游戏")  # 设置窗口标题

WHITE = (255, 255, 255)  # 定义白色
BLACK = (0, 0, 0)  # 定义黑色

def main_game_loop():
    running = True  # 游戏运行标志
    clock = pygame.time.Clock()  # 创建时钟对象
    font = load_font(48)  # 加载字体

    current_input = ""  # 当前输入
    score = 0  # 初始分数
    question = generate_question(1)  # 生成第一个问题
    difficulty_level = 1  # 初始难度级别
    time_limit = 10  # 每道题目的时间限制（秒）
    timer = time_limit  # 初始化计时器
    wrong_answers = 0  # 错误回答计数
    max_wrong_answers = 3  # 最大错误回答次数

    while running:
        events = pygame.event.get()  # 获取所有事件
        for event in events:
            if event.type == pygame.QUIT:  # 如果是退出事件
                pygame.quit()  # 退出pygame
                sys.exit()  # 退出程序

        # 处理输入
        current_input, submitted = handle_input(events, current_input)
        
        # 检查答案
        if submitted:
            num1, operation, num2, correct_answer = question
            if check_answer(current_input, correct_answer):
                score += 10  # 答对加10分
            else:
                score -= 5  # 答错减5分
                wrong_answers += 1  # 增加错误次数

            # 生成下一道题目
            difficulty_level = adjust_difficulty(score)  # 调整难度
            question = generate_question(difficulty_level)  # 生成新问题
            current_input = ""  # 清空当前输入
            timer = time_limit  # 重置计时器

        # 更新倒计时
        timer -= clock.get_time() / 1000  # 减少计时器时间（转换为秒）

        # 如果时间用完，自动扣分并生成新题目
        if timer <= 0:
            score -= 5  # 超时减5分
            wrong_answers += 1  # 增加错误次数
            difficulty_level = adjust_difficulty(score)  # 调整难度
            question = generate_question(difficulty_level)  # 生成新问题
            timer = time_limit  # 重置计时器
            current_input = ""  # 清空当前输入

        # 检查游戏是否结束
        if wrong_answers >= max_wrong_answers:
            game_over(window, font, score)  # 显示游戏结束界面
            break  # 退出游戏循环

        # 填充背景
        window.fill(WHITE)

        # 显示问题、分数和倒计时
        display_question(window, question, font)  # 显示问题
        render_text(window, f"得分: {score}", font, BLACK, (50, 50))  # 显示得分
        render_text(window, f"剩余时间: {int(timer)}", font, BLACK, (50, 100))  # 显示剩余时间
        render_text(window, f"错误次数: {wrong_answers}/{max_wrong_answers}", font, BLACK, (50, 150))  # 显示错误次数
        render_text(window, current_input, font, BLACK, (300, 300))  # 显示当前输入

        pygame.display.update()  # 更新显示
        clock.tick(60)  # 控制帧率

# 显示游戏结束界面
def game_over(window, font, final_score):
    window.fill(WHITE)  # 填充白色背景
    render_text(window, "游戏结束", font, (255, 0, 0), (300, 200))  # 显示"游戏结束"
    render_text(window, f"最终得分: {final_score}", font, BLACK, (300, 300))  # 显示最终得分
    pygame.display.update()  # 更新显示
    pygame.time.wait(3000)  # 等待3秒后退出游戏

if __name__ == "__main__":
    main_game_loop()  # 运行主游戏循环