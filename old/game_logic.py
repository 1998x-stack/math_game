# game_logic.py

# 导入文本渲染函数
from text_utils import render_text
# 导入问题生成函数
from question_generator import generate_question

# 检查答案是否正确
def check_answer(player_answer, correct_answer):
    try:
        # 尝试将玩家答案转换为整数并与正确答案比较
        return int(player_answer) == correct_answer
    except ValueError:
        # 如果转换失败，返回False
        return False

# 显示问题
def display_question(window, question, font):
    # 解包问题元组
    num1, operation, num2, _ = question
    # 格式化问题文本
    question_text = f"{num1} {operation} {num2} = ?"
    # 在窗口上渲染问题文本
    render_text(window, question_text, font, (0, 0, 0), (300, 200))

# 根据分数调整难度
def adjust_difficulty(score):
    # 根据分数返回相应的难度级别
    if score < 50:
        return 1  # 初级难度
    elif score < 100:
        return 2  # 中级难度
    else:
        return 3  # 高级难度