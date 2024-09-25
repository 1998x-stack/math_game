# question_generator.py

import random  # 导入随机模块

# 生成数学问题的函数
def generate_question(level, mode):
    if level == 1:  # 如果是第一级难度
        num1 = random.randint(1, 10)  # 生成1到10之间的随机数
        num2 = random.randint(1, 10)  # 生成另一个1到10之间的随机数
    elif level == 2:  # 如果是第二级难度
        num1 = random.randint(10, 50)  # 生成10到50之间的随机数
        num2 = random.randint(1, 10)  # 生成1到10之间的随机数
    else:  # 如果是其他难度级别
        num1 = random.randint(50, 100)  # 生成50到100之间的随机数
        num2 = random.randint(1, 20)  # 生成1到20之间的随机数

    if mode == 'add':  # 加法模式
        operation = '+'
        correct_answer = num1 + num2
    elif mode == 'subtract':  # 减法模式
        operation = '-'
        correct_answer = num1 - num2
    elif mode == 'multiply':  # 乘法模式
        operation = '×'
        correct_answer = num1 * num2
    elif mode == 'divide':  # 除法模式
        operation = '÷'
        correct_answer = num1
        num1 = num1 * num2  # 确保除法结果为整数
    else:  # 混合模式
        operation = random.choice(['+', '-', '×', '÷'])
        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        elif operation == '×':
            correct_answer = num1 * num2
        else:
            correct_answer = num1
            num1 = num1 * num2  # 确保除法结果为整数

    return num1, operation, num2, correct_answer  # 返回两个数字、运算符和正确答案

# 使用示例
# print(generate_question(2, 'add'))
# print(generate_question(3, 'multiply'))
# print(generate_question(1, 'mixed'))
